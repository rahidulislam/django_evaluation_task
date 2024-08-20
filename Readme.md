# Objective

Develop a basic user management backend project using Django Rest Framework (DRF) with JWT authentication.

# Tasks

- Initialize a Django project with DRF [25 Points].
- Create a sign-up API endpoint that returns a JWT token upon successful registration. The JWT token should contain the user id and email [25 Points].
- Develop API endpoints to add and list users [25 Points].
- Develop API endpoints to update and delete a user [25 Points].

# Instructions

## Step 1 - Initialize this django project

```python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Step 2 - Create superuser

```python
python manage.py createsuperuser
```

## Step 3 - Run server

```python
python manage.py runserver
```

# API Endpoints

## Home Page

- URL: http://127.0.0.1:8000/

## Sign Up

- method: POST
- URL: http://127.0.0.1:8000/api/v1/auth/users/
- body:

```json
{
  "first_name": "Rahidul",
  "last_name": "islam",
  "email": "rahi2@gmail.com",
  "password": "r@12345678"
}
```

## Token

- method: POST
- type: JWT Bearer Token
- URL: http://127.0.0.1:8000/api/v1/auth/token/
- body:

```json
{
  "email": "admin@gmail.com",
  "password": "r@12345678"
}
```

## Token Refresh

- method: POST
- URL: http://127.0.0.1:8000/api/v1/auth/token/refresh/

## User List

- method: GET
- URL: http://127.0.0.1:8000/api/v1/auth/users/
- permission: IsAuthenticated

## User Detail

- method: GET
- URL: http://127.0.0.1:8000/api/v1/auth/users/1/
- permission: IsAuthenticated

## Update User

- method: PATCH
- URL: http://127.0.0.1:8000/api/v1/auth/users/1/
- permission: IsAuthenticated and Same User
- body:

```json
{
  "first_name": "Rahidul",
  "last_name": "islam",
  "password": "r@12345678"
}
```

## Delete User

- method: DELETE
- URL: http://127.0.0.1:8000/api/v1/auth/users/1/
- permission: IsAuthenticated, Superuser or Same User
