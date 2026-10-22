# Gharam's Flask Portfolio

A personal portfolio website built with Python, Flask, HTML, Jinja, and CSS.

## Features
- Navigation between page sections
- About, skills, projects, and contact sections
- Project cards rendered dynamically from a Python list using Jinja
- Responsive layout for desktop and mobile screens

## Requirements
- Python 3.10 or newer
- pip

## Run locally

### Windows (Command Prompt)
```bat
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Before submission
1. Replace the example projects in `app.py` with projects you have actually completed.
2. Add a real GitHub repository URL to each project's `github_url` field.
3. Replace `your.email@example.com` and the GitHub/LinkedIn profile links in `templates/index.html` with your real contact details.
4. Edit the skills list so it accurately describes your skills.
5. Replace the placeholder project illustration with screenshots of your real projects if available.
6. Never upload your `venv` folder, passwords, API keys, or `.env` files.

## Deployment
This application can be deployed on a Python-capable web host. A typical Gunicorn start command is `gunicorn app:app`. Install dependencies from `requirements.txt`. Check the selected host's current Python-version and deployment instructions before deploying.
