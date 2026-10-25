# My Home — Real Estate Agency

## About the Project

My Home is an educational web application developed as part of my software development training. The project simulates a real estate agency website where users can browse property listings, search for properties, and view information about properties and brokers.

This project is a work in progress. Its features are implemented for learning and practice, and some functionality, validation, and user interface details may be incomplete or may need further improvement. The application is not intended to be a fully finished commercial product.

## Technologies

- Python
- Django
- SQLite
- HTML
- CSS
- Pillow
- python-dotenv

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

### 4. Configure environment variables (optional for local development)

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

Open the application in your browser:

http://127.0.0.1:8000/

## Project Applications

- `broker` — broker-related functionality.
- `city` — city-related functionality.
- `neighbourhood` — neighbourhood-related functionality.
- `property` — property listings and related functionality.
- `feature` — property features.

## Static and Media Files

- Static files, including CSS, are stored in the `static/` directory.
- Uploaded files, including property and broker images, are stored under `media/`.
- Django uses `STATIC_URL`, `MEDIA_URL`, and `MEDIA_ROOT` to configure these files.

## Project Status

This is a learning project, and development is ongoing. Features may be refined, bugs may still exist, and the code and user interface may change as I continue to practise and improve my Django skills.

## Disclaimer

This application is intended for educational purposes only. It has not been developed or tested as a production-ready real estate platform.
