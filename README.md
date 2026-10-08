# ABC Airline

A Django REST and React prototype modelling airline operations, bookings and passenger services.

## Features

- Routes, flights, travel classes and pricing
- Passenger and booking management
- Luggage and meal selections
- Payment and pickup/drop-off service records
- Reviews and employee action tracking
- REST endpoints implemented with Django REST Framework viewsets
- React pages for flight listings, bookings, payments and user bookings

## Architecture

```text
React client  →  Django REST API  →  SQLite
frontend/         backend/
```

## Technology

Python · Django 5 · Django REST Framework · SQLite · React 19 · Axios

## Local development

### Backend

```bash
git clone https://github.com/BryanFinnon/abc_airline.git
cd abc_airline
python -m venv .venv
source .venv/bin/activate
pip install "Django>=5.2,<5.3" "djangorestframework>=3.15,<4" "django-cors-headers>=4.4,<5"

export DJANGO_SECRET_KEY=replace-with-a-local-secret
export DJANGO_DEBUG=True

cd backend
python manage.py migrate
python manage.py runserver
```

### Frontend

In a second terminal:

```bash
cd frontend
npm install
npm start
```

The frontend uses `http://127.0.0.1:8000/api` by default. Override it with `REACT_APP_API_BASE_URL`.

## Project status

The domain models, serializers and API viewsets are implemented. Authentication, production payment processing, deployment configuration and broader automated test coverage remain future work.
