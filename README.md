# Django Blog Platform

A blog web application built with Python and Django. The project allows users to publish posts, interact through comments, and find content using the search functionality.

## Features

- **User authentication** — user registration, login, and logout.
- **User profiles** — personal user pages and profile information.
- **Post management** — create and publish blog posts.
- **Comments** — leave comments under publications.
- **Search** — find posts by search query.
- **Web interface** — a user-friendly interface for browsing and interacting with blog content.

## Tech Stack

- Python
- Django
- HTML and CSS
- SQL database

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Linux / macOS**
```bash
source .venv/bin/activate
```

**Windows**
```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

If the repository contains a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Project Purpose

The project was developed to practice web application development with Django, including user authentication, database operations, CRUD functionality, and search implementation.

## Future Improvements

- Improve the user interface and responsive layout.
- Add automated tests.
- Strengthen input validation and access control.
- Improve search functionality.
- Prepare the application for deployment.

## Status

The project is under development.
