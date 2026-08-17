# Django Website

A simple Django website with Home, About, and Contact pages.

## Features

- Home page
- About page
- Contact form with submission storage

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django_website.git
   cd django_website
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirment.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000/`

## Tech Stack

- Django 5.2
- SQLite
- Bootstrap
