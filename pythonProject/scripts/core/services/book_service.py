from fastapi import APIRouter
from schemas.models import Email
from scripts.core.handlers.book_handler import *
from scripts.core.handlers.email_handler import send_email
from scripts.core.handlers.excel_handler import *

app = APIRouter()


@app.post("/book/{book_id}")
def create_books(book: Book):
    return create_book(book)


@app.get("/get_all")
def read_all_books():
    return read_all()


@app.get("/books/{book_id}")
def read_books(book_id: int):
    return read_book(book_id)


@app.put("/books/{book_id}")
def update_books(book_id: int, book: Book):
    return update_book(book_id, book)


@app.delete("/books/{book_id}")
def delete_books(book_id: int):
    return delete_book(book_id)


@app.post("/send_email")
def send_emails(email: Email):
    return send_email(email)


@app.get("/Book_details")
def pipeline():
    return pipeline_agg()


@app.get("/generate_excel")
def excel():
    return generate_excel()

