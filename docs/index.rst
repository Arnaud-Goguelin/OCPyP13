========================
Technical Documentation
========================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   introduction
   prerequisites
   installation
   architecture
   api

Introduction
============

Welcome to the technical documentation of the **oc_lettings_app** Django application. 
This documentation covers all the steps required to understand, install, and run the application locally.

Project Context
===============

The **oc_lettings_app** goal is to provide a modern, scalable, and maintenable solution.

**Main Objectives:**
- Provide users with a smooth web interface.
- Ensure compatibility with production and testing environments.
- Implements a CI/CD pipeline to automate the deployment process.
- Ensure a modular and scalable architecture.

**Technologies Used:**
- **Framework**: Django 4.x
- **Language**: Python 3.12
- **Database**: SQLite3
- **Others**: Docker, Flake8, Pytest

Project Online
===============

You can access the project online at the following URL: https://ocpyp13.onrender.com/ .

| (may take few minutes to load, as server workers might be sleeping)

Configuration
=============

To configure the application, create a **.env** file using the provided **.envTemplate** file,
and set your own values for the environment variables.
Default values are already set in **settings.py** file to run the app locally.


Prerequisites, Installation and Usage
==============================

Before installing the application, ensure you have the following prerequisites:

**System Requirements**
| - Python 3.12 or higher
| - SQLite3 (comes pre-installed with Python)
| - **Or**: Docker (https://www.docker.com/)

**Installation Instructions on a local environment**
|
1. **Clone the repository**:

| git clone https://github.com/Arnaud-Goguelin/OCPyP13.git

2. **Create a virtual environment**:

| # On Windows: 
| python -m venv venv
| env\Scripts\activate

| # On macOS/Linux:
| python3 -m venv venv
| source venv/bin/activate

3. **Install dependencies**:

| pip install -r requirements.txt

5. **Run the development server**:

| python manage.py runserver

6. **Access the app**:
| Open a browser and go to: **http://127.0.0.1:8000/**

**Installation Instructions in a docker container**
|
1. **Clone the repository**:

| git clone https://github.com/Arnaud-Goguelin/OCPyP13.git

2. **Launch docker container:**

| Be sur to be at the root of the project.
| Lauch the following command:
| docker-compose up --build

3. **Access the app**:
| Open a browser and go to: **http://127.0.0.1:8000/**



Technical Architecture
======================

**Main components of the application:**
- **Django**: Handles HTTP requests, business logic, and templates.
- **SQLite3**: Relational database used to store data locally.
- **Docker**: Used for containerizing the services (db, and server) and set up the development or the production environment.


API (Endpoints details)
============================

**List of available endpoints:**

+------------+-------------------------------------+---------------------------------------+
| **Method** | **URL**                             | **Description**                       |
+------------+-------------------------------------+---------------------------------------+
| **GET**    | /                                   | display landing page: index.html      |
+------------+-------------------------------------+---------------------------------------+
| **GET**    | /profiles/                          | display profiles page                 |
+------------+-------------------------------------+---------------------------------------+
| **GET**    | /profiles/{str:username}/           | display selected user                 |
+------------+-------------------------------------+---------------------------------------+
| **GET**    | /lettings/                          | display lettings page                 |
+------------+-------------------------------------+---------------------------------------+
| **GET**    | /lettings/{int:letting_id}/         | display selected letting              |
+------------+-------------------------------------+---------------------------------------+
| **GET**    | /asentry-debug/                     | to test Sentry                        |
+------------+-------------------------------------+---------------------------------------+
