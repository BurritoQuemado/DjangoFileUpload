# Django File Upload API

This Django-based API allows users to securely upload files with support for token-based authentication and configurable storage options. It includes built-in security, redundancy, and high availability features, making it a robust choice for production environments.

## Features

- **Token-Based Authentication**: Securely manage access using tokens.
- **File Storage Options**: Supports local storage, Amazon S3, and other S3-compatible storage (e.g., MinIO).
- **High Availability and Redundancy**: Designed with load balancing and distributed storage options for optimal uptime.
- **Environment Variable Management**: Uses `.env` for secure configuration and sensitive data handling.

---

## Prerequisites

- Python 3.6 or newer
- Django 3.0 or later
- Required libraries: `djangorestframework`, `django-storages`, `boto3`, and `python-dotenv`
  
To install the dependencies:

```bash
pip install django djangorestframework django-storages boto3 python-dotenv python-magic-bin==0.4.14 django-redis

```

## Getting Started

1. Clone repository

````bash
git clone https://github.com/BurritoQuemado/DjangoFileUpload
cd DjangoFileUpload
````

2. Setup Environment Variables

```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_NAME=your-database-name
DATABASE_USER=your-database-user
DATABASE_PASSWORD=your-database-password
AWS_ACCESS_KEY_ID=your-aws-access-key-id
AWS_SECRET_ACCESS_KEY=your-aws-secret-access-key
AWS_STORAGE_BUCKET_NAME=your-s3-bucket-name
```

## API Setup and Configuration

1. Database Migrations

```bash
python manage.py migrate
```

2. Create superuser

```bash
python manage.py createsuperuser
```

3. Running the API Server

```bash
python manage.py runserver
```

## API Endpoints

### Token Generation
**Endpoint**  POST /api-token-auth/

**Body (form-data):**
- username: Username registered in database
- password: Password of the username

**Response**:
```json
{
    "token": "generated token"
}
```

### File Upload

**Endpoint** POST /api/upload/

**Headers:**
- Authorization: Token <user-token>

**Body (form-data):**
- user: user info (auto send from frontend)
- file: File to upload

**Response:**
```json
{
    "file": "path-to-file",
    "uploaded_at": "2024-11-07T15:32:08.123456Z",
}
```


