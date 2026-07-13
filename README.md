Contact Book API

This is a backend project built using FastAPI and PostgreSQL.
The API allows users to manage contacts, create groups, and maintain a list of favorite contacts.

What I implemented

Create, view, update, and delete contacts
Create and manage groups
Add and remove favorite contacts
PostgreSQL database integration for selected endpoints
Request validation using Pydantic

Tech Stack

Python
FastAPI
PostgreSQL
SQLAlchemy
Pydantic

Run the project

pip install -r requirements.txt
uvicorn contact_book.main:app --reload

API Documentation

After starting the server, open:
http://127.0.0.1:8000/docs

Current Status

The project is still in progress. Some endpoints are already connected to PostgreSQL, and I’m currently working on the remaining endpoints and the favorites feature.
Author

Irene Francis
