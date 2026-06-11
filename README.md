HRMS - Human Resource Management System

A secure and scalable Human Resource Management System (HRMS) built with Django REST Framework.

This project was developed to demonstrate enterprise-level backend development concepts including authentication, authorization, employee management, attendance tracking, leave management, reporting, dashboard analytics, API documentation, search, and filtering.

⸻

Project Overview

HRMS is a RESTful API-based Human Resource Management System designed to streamline HR operations and provide secure access to organizational data.

The system enables administrators and employees to manage departments, employee records, attendance, leave requests, reports, and dashboard analytics through a secure JWT-based authentication mechanism.

⸻

Key Features

Authentication & Security

•⁠  ⁠JWT Authentication
•⁠  ⁠Access Token & Refresh Token Support
•⁠  ⁠Protected API Endpoints
•⁠  ⁠User-Based Data Isolation
•⁠  ⁠Role-Based Access Control (RBAC)

Employee Management

•⁠  ⁠Create Employees
•⁠  ⁠Retrieve Employee Records
•⁠  ⁠Update Employee Information
•⁠  ⁠Delete Employees
•⁠  ⁠Employee Profile Management

Department Management

•⁠  ⁠Create Departments
•⁠  ⁠Update Departments
•⁠  ⁠Delete Departments
•⁠  ⁠Department-Based Organization

Attendance Management

•⁠  ⁠Check-In / Check-Out Tracking
•⁠  ⁠Attendance History
•⁠  ⁠Attendance CRUD Operations
•⁠  ⁠User-Specific Attendance Records

Leave Management

•⁠  ⁠Leave Request Submission
•⁠  ⁠Leave Approval Workflow
•⁠  ⁠Leave Status Tracking
•⁠  ⁠Employee Leave History

Dashboard & Reporting

•⁠  ⁠Dashboard Summary APIs
•⁠  ⁠Employee Statistics
•⁠  ⁠Department Statistics
•⁠  ⁠Attendance Metrics
•⁠  ⁠Leave Analytics

API Usability Enhancements

•⁠  ⁠Search Functionality
•⁠  ⁠Filtering Functionality
•⁠  ⁠Interactive Swagger Documentation
•⁠  ⁠OpenAPI Schema Generation

⸻

Implemented Backend Features

JWT Authentication

Secure authentication using JSON Web Tokens.

Endpoints:

POST /api/token/
POST /api/token/refresh/

User Profile Endpoint

Retrieve authenticated user information.

GET /api/me/

Search

Implemented using DRF SearchFilter.

Example:

GET /employees/?search=anas
GET /employees/?search=Software

Filtering

Implemented using Django Filter Backend.

Example:

GET /employees/?department=1
GET /employees/?salary=10000

API Documentation

Interactive Swagger UI available for testing all endpoints.

/api/docs/

⸻

System Architecture

The project follows a modular Django application architecture.

Apps:

users
employees
departments
attendance
leave
dashboard
reports

Each module is isolated and responsible for a specific business domain.

⸻

Technology Stack

Backend

•⁠  ⁠Python
•⁠  ⁠Django
•⁠  ⁠Django REST Framework

Authentication

•⁠  ⁠Simple JWT

Database

•⁠  ⁠SQLite (Development)

API Documentation

•⁠  ⁠DRF Spectacular
•⁠  ⁠Swagger UI
•⁠  ⁠OpenAPI 3.0

Filtering & Search

•⁠  ⁠Django Filter
•⁠  ⁠DRF SearchFilter

Development Tools

•⁠  ⁠VS Code
•⁠  ⁠Thunder Client
•⁠  ⁠Git
•⁠  ⁠GitHub

⸻

API Documentation

Swagger UI:

http://127.0.0.1:8002/api/docs/

OpenAPI Schema:

http://127.0.0.1:8002/api/schema/

⸻

Project Structure

HRMS_Project/
│
├── users/
├── employees/
├── departments/
├── attendance/
├── leave/
├── dashboard/
├── reports/
│
├── manage.py
├── requirements.txt
└── README.md

⸻

Setup & Installation

Clone Repository

git clone <repository-url>

Create Virtual Environment

python -m venv venv

Activate Environment

Mac/Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Run Migrations

python manage.py migrate

Create Superuser

python manage.py createsuperuser

Start Development Server

python manage.py runserver

⸻

Learning Objectives Demonstrated

This project demonstrates practical experience with:

•⁠  ⁠REST API Development
•⁠  ⁠Backend System Design
•⁠  ⁠Authentication & Authorization
•⁠  ⁠Role-Based Access Control
•⁠  ⁠Database Modeling
•⁠  ⁠Search & Filtering
•⁠  ⁠API Documentation
•⁠  ⁠Dashboard APIs
•⁠  ⁠Reporting APIs
•⁠  ⁠Git & GitHub Workflow
•⁠  ⁠Enterprise Backend Development Practices

⸻

Future Enhancements

•⁠  ⁠React Frontend
•⁠  ⁠Advanced Dashboard Visualizations
•⁠  ⁠Email Notifications
•⁠  ⁠Export Reports (PDF / Excel)
•⁠  ⁠Audit Logs
•⁠  ⁠Pagination
•⁠  ⁠Unit Testing
•⁠  ⁠Docker Deployment
•⁠  ⁠PostgreSQL Production Database

⸻

Author

Anas Alharbi

Software Engineering Graduate

Backend Development | APIs | System Design | Digital Transformation.
