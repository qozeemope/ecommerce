# E-commerce Product API

## Overview

This project is a backend REST API for managing products in an e-commerce platform.

It was built using Django and Django REST Framework as part of the ALX Backend Engineering Capstone Project.

The API allows authenticated users to create and manage products and categories, while public users can browse, search, and filter products.

---

## Features

### User Management

- User registration
- Token-based authentication
- CRUD operations on users (restricted to authenticated users)

### Product Management

- Create, update, delete products (authenticated users only)
- Retrieve all products
- Retrieve individual product details
- Automatic association of product owner

### Category Management

- Create, update, delete categories (authenticated users only)
- Public read access for categories
- Products linked to categories

### Search, Filtering & Pagination

- Search products by name or category (partial match supported)
- Filter products by:

- Category
- Price range
- Stock availability
- Pagination enabled for product listings

### API Documentation

- Swagger UI available
- OpenAPI schema provided
- Redoc documentation available

---

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (development)
- PostgreSQL (production ready)
- Token Authentication
- drf-spectacular (API docs)

---

## Project Structure

```
ecommerce_api/│├── accounts/        # user logic & auth├── products/        # products & categories logic├── config/          # project settings & urls├── manage.py├── requirements.txt└── README.md
```

---

## Installation & Setup

### 1. Clone repository

```
git clone <repo_url>cd ecommerce_api
```

### 2. Create virtual environment

```
python -m venv venvvenv\Scripts\activate   # Windows# orsource venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run migrations

```
python manage.py migrate
```

### 5. Create superuser (optional)

```
python manage.py createsuperuser
```

### 6. Start server

```
python manage.py runserver
```

---

## Authentication

This API uses Token Authentication.

### Register

POST `/api/auth/register/`

```
{  "username": "user1",  "email": "user@email.com",  "password": "password123"}
```

Response includes a token.

### Login

POST `/api/auth/login/`

```
{  "username": "user1",  "password": "password123"}
```

### Using the token

Add header to requests:

```
Authorization: Token YOUR_TOKEN
```

---

## API Endpoints

### Authentication

- POST `/api/auth/register/`
- POST `/api/auth/login/`

### Users

- GET `/api/users/`
- GET `/api/users/{id}/`
- PUT/PATCH `/api/users/{id}/`
- DELETE `/api/users/{id}/`

### Categories

- GET `/api/categories/`
- GET `/api/categories/{id}/`
- POST `/api/categories/` (auth required)
- PUT/PATCH `/api/categories/{id}/` (auth required)
- DELETE `/api/categories/{id}/` (auth required)

### Products

- GET `/api/products/`
- GET `/api/products/{id}/`
- POST `/api/products/` (auth required)
- PUT/PATCH `/api/products/{id}/` (auth required)
- DELETE `/api/products/{id}/` (auth required)

---

## Search & Filtering Examples

### Search by name or category

```
/api/products/?search=iphone/api/products/?search=electronics
```

### Filter by category

```
/api/products/?category=1
```

### Filter by price range

```
/api/products/?min_price=100&max_price=1000
```

### Filter by stock availability

```
/api/products/?in_stock=true
```

### Pagination

```
/api/products/?page=2
```

---

## API Documentation

Swagger UI:

```
/api/docs/
```

Redoc:

```
/api/redoc/
```

---

## Deployment

The API is deployment-ready for:

- Heroku
- PythonAnywhere

Environment variables required:

- SECRET_KEY
- DEBUG
- ALLOWED_HOSTS
- DATABASE_URL (for production)

---

## Author

ALX Backend Engineering Capstone Project

Built by: *[Qozeem Opeyemi Salami]*