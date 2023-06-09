from schemas.models import Book
from scripts.core.db.mongodb import book_1
from scripts.exceptions.exception_codes import Book_handling_exceptions
from scripts.logging.logger import logger
from scripts.constants.app_constants import Mydb_constants
from scripts.utility.mongo__utility import MongoCollectionBaseClass


class BookHandler:
    """
    class to handle the items in mongo
    """

    def __init__(self):
        self.user_mongo_obj = MongoCollectionBaseClass(database=Mydb_constants.db_name,
                                                       collection=Mydb_constants.db_collection)


# creating new book mongodb collection
def create_book(book: Book):
    try:
        logger.info("handler: creating a book")
        book_1.insert_one(book.dict())
        return {"message": "Book created successfully"}
    except Exception as e:
        logger.error(Book_handling_exceptions.Ex01.format(error=str(e)))
        return {"Failed to create book"}


# getting books from the collection
def read_all():
    try:
        logger.info("Handler: Reading all books")
        books = book_1.find({})
        all_books = []
        for new_book in books:
            all_book = {"book_id": new_book["book_id"], "title": new_book["title"], "category": new_book["category"],
                        "cost": new_book["cost"], "quantity": new_book["quantity"],
                        "borrower_name": new_book["borrower_name"]}
            all_books.append(all_book)
        return {"book details": all_books}
    except Exception as e:
        logger.error(Book_handling_exceptions.Ex02.format(error=str(e)))
        return {"error: Failed to get book"}


def read_book(book_id: int):
    try:
        logger.info("Handler: Getting a specific book")
        books = book_1.find({})
        all_books = []
        for new_book in books:
            if new_book['book_id'] == book_id:
                all_book = {"book_id": new_book["book_id"], "title": new_book["title"],
                            "category": new_book["category"],
                            "cost": new_book["cost"], "quantity": new_book["quantity"],
                            "borrower_name": new_book["borrower_name"]}
                all_books.append(all_book)
        return {"book details": all_books}
    except Exception as e:
        logger.error(Book_handling_exceptions.Ex03.format(error=str(e)))
        return {"error": "Failed to get book"}


# updating the existing books in the collection
def update_book(book_id: int, book: Book):
    try:
        logger.info("Handler: Updating books")
        book_1.update_one({'book_id': book_id}, {'$set': book.dict()})
        return {"message": "Book updated successfully"}
    except Exception as e:
        logger.error(Book_handling_exceptions.Ex04.format(error=str(e)))
        return {"error: Failed to update the book"}


# deletes book from the collection
def delete_book(book_id: int):
    try:
        logger.info("Handler: Deleting books")
        book_1.delete_one({'book_id': book_id})
        return {"message": "Book deleted successfully"}
    except Exception as e:
        logger.error(Book_handling_exceptions.Ex05.format(error=str(e)))
        return {"error: Failed to delete the book"}


def pipeline_agg():
    logger.info("Handler: Creating pipeline")
    pipeline = [
        {
            '$project': {
                '_id': 0
            }
        }
    ]
    data = book_1.aggregate(pipeline)
    data = list(data)
    return {"Book Details": data[0:6]}
