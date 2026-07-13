Contact Book API

A backend REST API built using FastAPI and PostgreSQL.

Features

Create, view, update, and delete contacts

Manage contact groups

Add and remove favorite contacts

Store data in PostgreSQL

Validate requests using Pydantic

Test APIs using Swagger/OpenAPI

Technologies Used

Python

FastAPI

PostgreSQL

SQLAlchemy

Pydantic

How to Run

pip install -r requirements.txt

uvicorn contact_book.main:app --reload

API Documentation

After starting the server, open:

http://127.0.0.1:8000/docs

Current Status

PostgreSQL integration has been implemented for selected endpoints. Remaining endpoints are being migrated from in-memory storage to database-backed operations as part of ongoing backend development practice.

Author

Irene Francis
