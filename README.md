# Django REST API for User Registration and Car Management

This repository contains a Django project that provides REST API endpoints for user registration, login, and management of cars by authenticated users.

## Features

- User registration with username and password.
- Token-based authentication for user login.
- User authentication and permissions for managing cars.
- Retrieving a list of cars owned by the authenticated user.

## Setup Instructions

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mert679/TaskRestApi.git
   ```

2. **Navigate to the project directory:**
   ```
   cd task_api
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```
   python manage.py migrate
   ```

5. **Run the development server:**
   ```
   python manage.py runserver
   ```

6. **Access the API endpoints:**
   - User Registration: `http://127.0.0.1:8000/register/`
   - User Login: `http://127.0.0.1:8000/login/`
   - User's Cars: `http://127.0.0.1:8000/cars/`

## API Endpoints

- `POST /register/`: Endpoint for user registration. Requires a username and password. Returns user details along with a token upon successful registration.

- `POST /login/`: Endpoint for user login. Requires a username and password. Returns a token upon successful login.

- `GET /cars/`: Endpoint for retrieving cars owned by the authenticated user. Requires a valid authentication token.

## Technologies Used

- Django: A high-level Python web f
