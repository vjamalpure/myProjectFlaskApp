from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_migrate import Migrate
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ROOT#123@localhost:5432/userinfo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)
CORS(app)  # Enable CORS
password = 'test'  # replace with your desired password
hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

print(hashed_password)
# User model
class User(db.Model):
    __tablename__ = 'User'  # Explicitly define the table name

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    modified_by = db.Column(db.String(50))
    modified_on = db.Column(db.DateTime, default=datetime.utcnow)

# Routes
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    print(data)
    username = data['username']
    password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    phone_number = data['phone_number']
    gender = data['gender']

    new_user = User(username=username, password=password, phone_number=phone_number, gender=gender)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity={'username': user.username})
        return jsonify({'token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {
            'id': user.id,
            'username': user.username,
            'phone_number': user.phone_number,
            'gender': user.gender,
            'modified_by': user.modified_by,
            'modified_on': user.modified_on
        }
        output.append(user_data)
    return jsonify(output), 200

@app.route('/users', methods=['POST'])
@jwt_required()
def add_user():
    data = request.get_json()
    username = data['username']
    password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    phone_number = data['phone_number']
    gender = data['gender']
    current_user = get_jwt_identity()

    new_user = User(username=username, password=password, phone_number=phone_number, gender=gender, modified_by=current_user['username'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added successfully'}), 201

@app.route('/users/<int:id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    data = request.get_json()
    user = User.query.get(id)

    if not user:
        return jsonify({'message': 'User not found'}), 404

    user.username = data['username']
    user.phone_number = data['phone_number']
    user.gender = data['gender']
    user.modified_by = get_jwt_identity()['username']
    user.modified_on = datetime.utcnow()

    db.session.commit()

    return jsonify({'message': 'User updated successfully'}), 200

@app.route('/users/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    user = User.query.get(id)

    if not user:
        return jsonify({'message': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)