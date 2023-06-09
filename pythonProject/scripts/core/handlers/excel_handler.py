import pandas as pd
from fastapi import FastAPI
from fastapi.responses import FileResponse
from scripts.core.db import mongodb
from scripts.core.db.mongodb import book_db, book_1

from scripts.core.handlers.book_handler import pipeline_agg
from scripts.logging.logger import logger
from scripts.utility.mongo__utility import MongoCollectionBaseClass

app = FastAPI()


def generate_excel():
    logger.info("Handler: Generating excel")
    # Fetching the data for the Excel file
    json_data = pipeline_agg()

    # Create a DataFrame from the data
    booking_details_df = pd.DataFrame(json_data["Book Details"])

    # Create the Excel file
    excel_file = 'book_records.xlsx'
    booking_details_df.to_excel(excel_file, index=False)

    # Return the Excel file as a FileResponse
    return FileResponse(excel_file, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                        filename='book_records.xlsx')


