# Django Website

A beginner-friendly Django website with three pages: **Home, About Us, and Contact Us**.

The project demonstrates the fundamentals of Django web development, including URL routing, views, templates, models, forms, database migrations, Django Admin, and the Messages Framework.

## Features

* Modern responsive design using Bootstrap 5
* Home page with:

  * Hero section
  * Features section
  * Call-to-action
* About Us page with:

  * Company introduction
  * Services
  * Mission
* Contact Us page with:

  * Contact form
  * Form validation
  * Database storage
  * Success notifications
* Django Admin panel for managing contact submissions
* Django Messages Framework for success notifications
* SQLite database for development

## Technologies Used

* Python
* Django
* Bootstrap 5
* HTML
* SQLite
* Django Templates
* Django Forms
* Django Admin

## Project Structure

```text
django_website/
│
├── manage.py
├── db.sqlite3
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── website/
│   ├── migrations/
│   ├── templates/
│   │   └── website/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── about.html
│   │       └── contact.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
└── venv/
```

## Pages

| Page       | URL         | Description                      |
| ---------- | ----------- | -------------------------------- |
| Home       | `/`         | Main landing page                |
| About Us   | `/about/`   | Company information and services |
| Contact Us | `/contact/` | Contact form                     |
| Admin      | `/admin/`   | Django administration panel      |

## Contact Form

The contact form collects:

* Name
* Email
* Subject
* Message
* Submission date/time

Submitted messages are stored in the SQLite database through the `ContactSubmission` model.

Administrators can view and manage submissions from the Django Admin panel.

## Django Messages

The Django Messages Framework is used to display a success notification after a contact form is successfully submitted.

Example:

```text
Your message has been sent successfully!
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd django_website
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install django
```

### 5. Apply migrations

```powershell
python manage.py migrate
```

### 6. Create an admin user

```powershell
python manage.py createsuperuser
```

### 7. Start the development server

```powershell
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Admin Panel

After creating a superuser, access the Django Admin panel at:

```text
http://127.0.0.1:8000/admin/
```

From there, administrators can manage contact submissions.

## Database

This project currently uses **SQLite**, which is suitable for development and learning.

The database is created automatically after running:

```powershell
python manage.py migrate
```

## Learning Objectives

This project was built to understand the fundamental Django workflow:

```text
Browser
   ↓
URL
   ↓
View
   ↓
Template
   ↓
Response
```

For the contact form:

```text
User
   ↓
HTML Form
   ↓
Django Form
   ↓
Validation
   ↓
Model
   ↓
SQLite Database
   ↓
Django Admin
```

## Future Improvements

Future versions may include:

* User authentication
* PostgreSQL database
* Search functionality
* Improved contact management
* Email notifications
* Environment variables
* Production deployment
* Custom domain
* Security hardening
* Automated testing
* CI/CD

## License

This project is created for learning and educational purposes.
