from pydantic import BaseModel


class Book(BaseModel):
    # pydantic model
    book_id: int
    title: str
    category: str
    cost: int
    quantity: int
    borrower_name: str


class Email(BaseModel):
    receiver_email: str
    subject: str
