project-root/
├── auth_service/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── config.py
│   ├── utils.py
│   ├── tests/
│   │   └── test_auth.py
├── api_gateway/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── config.py
│   ├── routes.py
│   ├── tests/
│   │   └── test_routes.py
├── microservices/
│   ├── example_service/
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   ├── Dockerfile
│   │   ├── config.py
│   │   ├── utils.py
│   │   ├── tests/
│   │   │   └── test_example.py
│   ├── ...
├── docker-compose.yml
├── README.md
└── .env

Flask==2.0.2
PyJWT==2.3.0
Werkzeug==2.0.2
gunicorn==20.1.0

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

version: '3.8'

services:
  auth_service:
    build:
      context: ./auth_service
    ports:
      - "5000:5000"
    environment:
      - SECRET_KEY=your_secret_key
    networks:
      - app-network

networks:
  app-network:
    driver: bridge

# Project Setup

## Prerequisites
- Docker
- Docker Compose

## Environment Variables
Create a `.env` file in the root directory:

## Build and Run with Docker Compose

- `POST /register` - Register a new user
    - Payload: `{ "username": "your_username", "password": "your_password" }`
- `POST /login` - Login and retrieve a token
    - Payload: `{ "username": "your_username", "password": "your_password" }`
- `GET /protected` - Access a protected route
    - Header: `Authorization: Bearer <your_token>`