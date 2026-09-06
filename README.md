# ABC Airline

A full-stack airline management prototype built with Django REST Framework and React.

## Features

- Flight and route data
- Passenger and booking workflows
- Travel classes, luggage, meals, and pricing models
- Payment and pickup/drop-off service records
- REST API serializers and viewsets
- React pages for flight listing, booking, payment, and user bookings

## Architecture

```text
React frontend → Django REST API → SQLite
```

## Local setup

### Backend

```bash
git clone https://github.com/BryanFinnon/abc_airline.git
cd abc_airline
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export DJANGO_SECRET_KEY="replace-with-a-local-secret"
export DJANGO_DEBUG=True
cd backend
python manage.py migrate
python manage.py runserver
```

### Frontend

In another terminal:

```bash
cd frontend
npm ci
npm start
```

The frontend uses `http://127.0.0.1:8000/api` by default. Set `REACT_APP_API_BASE_URL` to use a different API.

## Configuration

See `.env.example` for the supported development variables. Production deployments must use a unique secret, `DJANGO_DEBUG=False`, restricted hosts, and restricted CORS origins.

## Project status

This is a portfolio prototype. Authentication, production payment integration, deployment configuration, and comprehensive automated testing remain future work. A few UI placeholders are intentionally retained for later implementation.

## Author

Bryan Finnon — MSc Computer Science (Distinction), focused on applied AI and software engineering.
