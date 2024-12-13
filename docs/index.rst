========================
Technical Documentation
========================

.. toctree::
   :maxdepth: 2
   :caption: Table of Contents

   introduction
   project_context
   prerequisites_and_installation
   technical_architecture
   configuration
   usage
   api
   testing_and_code_quality
   security
   faq
   appendix
   glossary

Introduction
============

Welcome to the technical documentation of the **MyApp** Django application. This documentation covers all the steps required to understand, install, configure, and maintain the application.

You will find information on the **technical architecture**, **API endpoints**, **project configuration**, as well as guidance for **troubleshooting and security best practices**.

Project Context
===============

The **MyApp** application was developed as part of the **Site Web 2.0** project. The goal of this project is to provide a modern, scalable, and secure solution.

**Main Objectives:**
- Provide users with a smooth web interface.
- Offer user management, statistics, and reporting functionalities.
- Ensure compatibility with production and testing environments.

**Technologies Used:**
- **Framework**: Django 4.x
- **Language**: Python 3.12
- **Database**: SQLite3
- **Others**: Redis (optional), Docker (optional)

Prerequisites and Installation
==============================

Before installing the application, ensure you have the following prerequisites:

**System Requirements**
- Python 3.12 or higher
- SQLite3 (comes pre-installed with Python)
- Redis (optional, for background tasks)
- Docker (optional, but recommended)

**Installation Instructions**
1. **Clone the repository**:
git clone https://github.com/username/myapp.git cd myapp

2. **Create a virtual environment**:
python -m venv venv source venv/bin/activate # On Windows: .\venv\Scripts\activate

3. **Install dependencies**:
pip install -r requirements.txt

4. **Apply database migrations**:
python manage.py migrate

5. **Run the development server**:
python manage.py runserver

6. **Access the app**:
Open a browser and go to: **http://localhost:8000**

Technical Architecture
======================

**Main components of the application:**
- **Django**: Handles HTTP requests, business logic, and templates.
- **SQLite3**: Relational database used to store data locally.
- **Redis (optional)**: Used for asynchronous task queues.
- **Docker (optional)**: Used for containerizing the services.

**Technical Architecture Diagram:**
User <--> Django (Gunicorn) <--> SQLite3


Configuration
=============

To configure the application, create a **.env** file using the provided **.env.example** file.

**Important Variables:**
- `SECRET_KEY`: Django secret key for cryptographic signing.
- `DEBUG`: Indicates if debug mode is enabled (True/False).
- `DATABASE_URL`: SQLite3 database path (optional for advanced usage).
- `REDIS_URL`: URL to connect to Redis (optional).

Usage (User Guide)
==================

This section explains how to use the application in development.

1. **Start the application**
python manage.py runserver

2. **Access the application**
Go to: **http://localhost:8000**

3. **Create a superuser**
python manage.py createsuperuser

API (Endpoints and Examples)
============================

**List of available endpoints:**

| **Method** | **URL**          | **Description**                   |
|------------|-----------------|-------------------------------------|
| **GET**    | /api/users/      | List all users                     |
| **POST**   | /api/users/      | Create a new user                  |
| **GET**    | /api/users/{id}/ | Retrieve a specific user by ID     |
| **PUT**    | /api/users/{id}/ | Update a user's information        |
| **DELETE** | /api/users/{id}/ | Delete a user                      |

**Example API Request:**
```http
POST /api/users/
Content-Type: application/json

{
 "username": "john_doe",
 "password": "securepassword123"
}
