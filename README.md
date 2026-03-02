# 🚀 FastAPI Backend Project

A high-performance, asynchronous REST API built with **Python**, featuring robust data validation and ORM integration for PostgreSQL.

---

## 🛠 Tech Stack

The project is built using the following modern tools:

* **[FastAPI](https://fastapi.tiangolo.com/)** – High-performance web framework for building APIs.
* **[Pydantic](https://docs.pydantic.dev/)** – Data validation and settings management.
* **[SQLAlchemy](https://www.sqlalchemy.org/)** – A powerful Object Relational Mapper (ORM).
* **[Psycopg2](https://www.psycopg.org/)** – PostgreSQL database adapter for Python.
* **[Uvicorn](https://www.uvicorn.org/)** – A lightning-fast ASGI server implementation.

---

## 📄 Setup Instructions

**1. Clone the repository:**
```
git clone https://github.com/CryMR/bank-api
cd bank-api
```
or
```
git clone https://github.com/CryMR/bank-api && cd bank-api
```

**2. Create a ```.env``` file:**
In the root directory of the project, create a file named .env to store your environment variables. This file will help configure the database connection settings.

Here's an example ```.env``` file:
```
DB_USER=example
DB_PASSWORD=example
DB_NAME=example

DATABASE_URL=postgresql://${DB_USER}:${DB_PASSWORD}@db:5432/${DB_NAME}
```
* ```DB_USER```: Your PostgreSQL database username.
* ```DB_PASSWORD```: Your PostgreSQL database password.
* ```DB_NAME```: The name of your PostgreSQL database.
* ```DATABASE_URL```: The complete connection URL for your PostgreSQL database.

**3. Start the application using Docker Compose:**
```
docker compose up --build
```
This Will:
* Build the Docker images if needed.
* Start the FastAPI app and PostgreSQL in separate containers.

**4. Acces the app:**
After the containers are up and running, you can access the FastAPI application at ```http://localhost:8000```.

## 📂 Project Structure

```
.
├── app/
│   ├── main.py          # Application entry point
│   ├── models.py        # SQLAlchemy database models
│   ├── schemas.py       # Pydantic validation schemas
│   └── database.py      # Database connection and session management
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables
├── Dockerfile           # Dockerfile for building the FastAPI app image
└── docker-compose.yml   # Docker Compose configuration for multi-container setup
```