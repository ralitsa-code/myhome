# My Home

## Project Overview

**My Home** is a Django web application for a real estate agency. It provides a web interface for managing property listings and the related information needed by a real estate business.

## Features

- Create and manage brokers.
- Manage cities and their neighbourhoods.
- Manage property features.
- Create, view, and edit property listings.
- Activate and deactivate property listings.
- Search for properties by city.
- Validate uploaded images by file type and file size.
- Validate property prices based on property area.

## Technologies

- Python
- Django
- HTML5
- CSS3
- Pillow
- SQLite or PostgreSQL

## Project Structure

The project is organized into the following Django applications:

- `broker` — broker information and contact details.
- `city` — city management.
- `neighbourhood` — neighbourhoods associated with cities.
- `property` — property listings and their details.
- `feature` — property features.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ralitsa-code/myhome.git
cd myhome
```

### 2. Create and activate a virtual environment

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root directory, alongside `manage.py`.

Use the `.env.example` file as a reference and configure the variables required by the project.

Do not commit real passwords or secret keys to version control.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open the local development address shown in the terminal in your browser.

## Database Configuration

The project can be tested with SQLite for local development. PostgreSQL can also be used by configuring the database connection variables in the `.env` file.

Make sure the selected database configuration matches the settings in `settings.py`.

## Environment Variables

The `.env.example` file documents the environment variables used by the project, including:

- `SECRET_KEY` — Django secret key.
- `DEBUG` — enables or disables debug mode.
- `ALLOWED_HOSTS` — allowed host names.
- `DB_NAME` — database name.
- `DB_USER` — database user.
- `DB_PASSWORD` — database password.
- `DB_HOST` — database host.
- `DB_PORT` — database port.

Use appropriate values for your local environment. Do not publish sensitive credentials.

## Notes

This project was developed as part of a Django learning project and demonstrates Django models, forms, views, templates, validation, and database integration.
