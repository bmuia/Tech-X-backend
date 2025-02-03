# Tech X

This is a Django-based project that provides user authentication and newsletter subscription functionality. It uses Django REST Framework (DRF) for building APIs and Simple JWT for token-based authentication.

## Features

1. **User Authentication**:
   - User registration with JWT token generation.
   - Login and token refresh endpoints.
   
2. **Newsletter Subscription**:
   - Users can subscribe or unsubscribe from the newsletter.
   - Email notifications are sent upon subscription.

3. **Admin Panel**:
   - Django admin interface for managing users and newsletter subscriptions.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.12.1
- PostgreSQL >= 14.13
- `pip` (Python package manager)

---

## Installation

### 1. Clone the repository

```bash
git clone git@github.com:bmuia/Tech-X-backend.git
cd Tech
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a .env file in the root directory and add the following variables:

```bash
SECRET_KEY=your_secret_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_email_password
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

# API Endpoints

## Authentication

- Register a new user:

  - URL: http://localhost:8000/api/auth/register/

  - Method: POST

  - Body:

```json
{
  "username": "your_username",
  "email": "your_email@example.com",
  "password": "your_password"
}

```
  - Response:
```json
{
  "username": "your_username",
  "email": "your_email@example.com",
  "access": "access_token",
  "refresh": "refresh_token"
}
```
- Login:

  - URL: http://localhost:8000/api/auth/token/login/

  - Method: POST

  - Body:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

  - Response:

```json
{
  "access": "access_token",
  "refresh": "refresh_token"
}
```

- Refresh Token:

  - URL: http://localhost:8000/api/auth/token/login/refresh/

  - Method: POST

  - Body:

```json
{
  "refresh": "refresh_token"
}
```

  - Response:

```json

{
  "access": "new_access_token"
}
```

### Newsletter Subscription
- Subscribe/Unsubscribe:

  - URL: http://localhost:8000/newsletter/subscribe/

  - Method: POST

  - Headers:

```plaintext
Authorization: Bearer <access_token>
```

  - Body:

```bash
{
  "subscribed": true  # or false to unsubscribe
}
```

  - Response:

```bash
{
  "message": "Subscription updated successfully."
}
```
- Check Subscription Status:

  - URL: http://localhost:8000/newsletter/subscribe/

  - Method: GET

  - Headers:

```plaintext
Authorization: Bearer <access_token>
```
  - Response:

```bash
{
  "subscribed": true  # or false
}
```

## Admin Panel
You can access the Django admin panel at `/admin/`. Use the superuser credentials you created earlier to log in.

## Contributing
If you'd like to contribute to this project, please follow these steps:
   1. Fork the repository.

   2. Create a new branch for your feature or bugfix.

   3. Commit your changes and push to your branch.

   4. Submit a pull request.

## License
his project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.




