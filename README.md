# BackendDevProject3 - Secure Authentication System

## Description

This project is a FastAPI-based authentication system that allows users to register, log in, and access protected routes using JWT (JSON Web Tokens).

Passwords are securely hashed using bcrypt before being stored in a SQLite database.

## Features

- User Registration
- User Login
- Password Hashing with bcrypt
- JWT Authentication
- Protected Routes
- SQLAlchemy ORM
- SQLite Database
- Environment Variables with python-dotenv

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Passlib (bcrypt)
- Python-JOSE
- Pydantic
- Uvicorn

## Installation

Clone the repository:

```bash
git clone <repository-[Secure Autentication System](https://github.com/Abigailajk/BackendDevelopmentTask3.git)>
```

Navigate into the project:

```bash
cd BackendDevProject3
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
python -m uvicorn main:app --reload
```

## API Endpoints

### POST /register

Registers a new user.

### POST /login

Authenticates a user and returns a JWT access token.

### GET /protected

A protected endpoint that requires a valid JWT token.

## Project Structure

```
BackendDevProject3/
│── auth.py
│── crud.py
│── database.py
│── main.py
│── models.py
│── schemas.py
│── requirements.txt
│── README.md
```

## Author

Adediran Olusaanumi
