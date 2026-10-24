# My Home — Real Estate Agency

## Overview

My Home is a Django web application for a real estate agency. It allows visitors to browse property listings, search for properties, and view information about properties and brokers.

The application is built with Django and uses SQLite as its default database.

## Technologies

- Python
- Django
- SQLite
- HTML and CSS
- Pillow for image handling
- python-dotenv for environment variable loading

## Requirements

- Python compatible with the Django version specified in `requirements.txt`
- pip

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ralitsa-code/myhome.git
cd myhome
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Environment variables (optional for local development)

The project loads environment variables from a `.env` file when one is present.

For the default local SQLite configuration, a `.env` file is not required. The application uses fallback values for `SECRET_KEY` and `ALLOWED_HOSTS`, and `DEBUG` defaults to `False` when the environment variable is not set.

For local development, you may create a `.env` file in the project root:

```dotenv
SECRET_KEY=replace-with-a-local-development-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Keep `.env` out of version control. Do not use the development fallback secret key in production.

### 5. Apply database migrations

```bash
python manage.py migrate
```

The project uses SQLite by default. Django creates the database file when migrations are applied.

### 6. Start the development server

```bash
python manage.py runserver
```

Open the following address in your browser:

http://127.0.0.1:8000/

## Static and Media Files

- Static files, including CSS, are stored in the `static/` directory.
- Uploaded files, including property and broker images, are stored under `media/`.
- Django uses `STATIC_URL`, `MEDIA_URL`, and `MEDIA_ROOT` to configure these files.

## Project Applications

The project includes the following Django applications:

- `broker` — broker-related functionality.
- `city` — city-related functionality.
- `neighbourhood` — neighbourhood-related functionality.
- `property` — property listings and related functionality.
- `feature` — property features.

## Notes

This project is configured for local development. Before deploying it to production, review Django's security settings, use a secure secret key, configure allowed hosts, and configure static and media file serving appropriately.
