# # import pandas as pd
# #
# # from scripts.core.handlers.book_handler import pipeline_agg
# #
# # json_data = pipeline_agg()
# # booking_details_df = pd.DataFrame(json_data["Book Details"])
# # print(booking_details_df)
# #
# # # booking_details_df.to_excel("reports/book_records.xlsx")
#
#
# import pandas as pd
# from fastapi import FastAPI
# from fastapi.responses import FileResponse
#
# from scripts.core.handlers.book_handler import pipeline_agg
#
# app = FastAPI()
#
#
# def generate_excel():
#     # Fetching the data for the Excel file
#     json_data = pipeline_agg()
#
#     # Create a DataFrame from the data
#     booking_details_df = pd.DataFrame(json_data["Book Details"])
#
#     # Create the Excel file
#
#     excel_file_path = "C:\\Users\\sridevi.p\\PycharmProjects\\pythonProject\\reports\\book_records.xlsx")
#     booking_details_df.to_excel(excel_file_path, index=False)
#
#     # Return the Excel file as a FileResponse
#     return FileResponse(excel_file_path, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
