# Flask User Management API

This is a Flask application for managing user information. It includes features for user signup, login, and CRUD operations on user data. The application uses SQLAlchemy for ORM, Flask-Bcrypt for password hashing, Flask-JWT-Extended for JWT authentication, and Flask-Migrate for database migrations. It also supports CORS for cross-origin requests.

## Features

- User signup
- User login
- JWT-based authentication
- CRUD operations on user data
- Password hashing
- Database migrations

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
- [Database](#database)
- [Docker](#docker)
- [License](#license)

## Getting Started

### Prerequisites

- Python 3.11
- PostgreSQL
- Docker (optional, for containerization)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/vjamalpure/myProjectFlaskApp.git
   cd flask-user-management


2. **Create a virtual environment and activate it:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the PostgreSQL database:**

   ```sql
   CREATE DATABASE userinfo;
   CREATE USER postgres WITH ENCRYPTED PASSWORD 'ROOT#123';
   GRANT ALL PRIVILEGES ON DATABASE userinfo TO postgres;
   ```

5. **Run the database migrations:**

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Set up environment variables:**

   Create a `.env` file and add the following:

   ```env
   SQLALCHEMY_DATABASE_URI=postgresql://postgres:ROOT#123@localhost:5432/userinfo
   JWT_SECRET_KEY=your_jwt_secret_key
   ```

## Usage

### Running the Application

1. **Run the Flask application:**

   ```bash
   flask run
   ```

   The application will be available at `http://localhost:5000`.

### API Endpoints

- **Signup**

  ```http
  POST /signup
  ```

  Request body:

  ```json
  {
    "username": "string",
    "password": "string",
    "phone_number": "string",
    "gender": "string"
  }
  ```

- **Login**

  ```http
  POST /login
  ```

  Request body:

  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```

- **Get Users**

  ```http
  GET /users
  ```

  Requires JWT token in the `Authorization` header.

- **Add User**

  ```http
  POST /users
  ```

  Requires JWT token in the `Authorization` header.

  Request body:

  ```json
  {
    "username": "string",
    "password": "string",
    "phone_number": "string",
    "gender": "string"
  }
  ```

- **Update User**

  ```http
  PUT /users/{id}
  ```

  Requires JWT token in the `Authorization` header.

  Request body:

  ```json
  {
    "username": "string",
    "phone_number": "string",
    "gender": "string"
  }
  ```

- **Delete User**

  ```http
  DELETE /users/{id}
  ```

  Requires JWT token in the `Authorization` header.

## Database

The application uses PostgreSQL as the database. Below is the `User` table schema:

```sql
CREATE TABLE "User" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(60) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    modified_by VARCHAR(50),
    modified_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Docker

To containerize the Flask application, use the provided Dockerfile:

### Build the Docker Image

```bash
docker build -t flask-app .
```

### Run the Docker Container

```bash
docker run -d -p 5000:5000 flask-app
```

The application will be available at `http://localhost:5000`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This `README.md` file provides a comprehensive guide to setting up, running, and using your Flask application. Adjust the repository URL and any other specific details as needed.
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the PostgreSQL database:**

   ```sql
   CREATE DATABASE userinfo;
   CREATE USER postgres WITH ENCRYPTED PASSWORD 'ROOT#123';
   GRANT ALL PRIVILEGES ON DATABASE userinfo TO postgres;
   ```

5. **Run the database migrations:**

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Set up environment variables:**

   Create a `.env` file and add the following:

   ```env
   SQLALCHEMY_DATABASE_URI=postgresql://postgres:ROOT#123@localhost:5432/userinfo
   JWT_SECRET_KEY=your_jwt_secret_key
   ```

## Usage

### Running the Application

1. **Run the Flask application:**

   ```bash
   flask run
   ```

   The application will be available at `http://localhost:5000`.

### API Endpoints

- **Signup**

  ```http
  POST /signup
  ```

  Request body:

  ```json
  {
    "username": "string",
    "password": "string",
    "phone_number": "string",
    "gender": "string"
  }
  ```

- **Login**

  ```http
  POST /login
  ```

  Request body:

  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```

- **Get Users**

  ```http
  GET /users
  ```

  Requires JWT token in the `Authorization` header.

- **Add User**

  ```http
  POST /users
  ```

  Requires JWT token in the `Authorization` header.

  Request body:

  ```json
  {
    "username": "string",
    "password": "string",
    "phone_number": "string",
    "gender": "string"
  }
  ```

- **Update User**

  ```http
  PUT /users/{id}
  ```

  Requires JWT token in the `Authorization` header.

  Request body:

  ```json
  {
    "username": "string",
    "phone_number": "string",
    "gender": "string"
  }
  ```

- **Delete User**

  ```http
  DELETE /users/{id}
  ```

  Requires JWT token in the `Authorization` header.

## Database

The application uses PostgreSQL as the database. Below is the `User` table schema:

```sql
CREATE TABLE "User" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(60) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    modified_by VARCHAR(50),
    modified_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Docker

To containerize the Flask application, use the provided Dockerfile:

### Build the Docker Image

```bash
docker build -t flask-app .
```

### Run the Docker Container

```bash
docker run -d -p 5000:5000 flask-app
```

The application will be available at `http://localhost:5000`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This `README.md` file provides a comprehensive guide to setting up, running, and using your Flask application. Adjust the repository URL and any other specific details as needed.
