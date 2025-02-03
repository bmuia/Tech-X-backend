# Tech Project

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

- Python 3.x
- PostgreSQL
- `pip` (Python package manager)

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd Tech
```

### 2. Set up a virtual environment

```bash
python3 -m venv venv
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





