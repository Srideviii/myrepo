class Book_Ends:
    welcome = "/"
    create_book = "/books/book_id"
    read_book = "/get_all"
    update_book = "/book/{book_id}"
    delete_book = "/books/{book_id}"
    send_email = "/send_email"
    pipeline_agg = "/Total_price"


class Mydb_constants:
    uri = "mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23"
    db_name = "interns_b2_23"
    db_collection = "Sridevi"
