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

## 📂 Project Structure

```text
.
├── app/
│   ├── main.py          # Application entry point
│   ├── models.py        # SQLAlchemy database models
│   ├── schemas.py       # Pydantic validation schemas
│   └── database.py      # Database connection and session management
├── requirements.txt     # Project dependencies
└── .env                 # Environment variables (Database URLs, API keys)