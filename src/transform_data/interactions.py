from config import InitConstants
from src.transform_data.csv_source import CsvSource


class Interactions(CsvSource):

    def __init__(self):
        interactions_path = InitConstants().interactions_path
        super().__init__(interactions_path,cols=['user_id', 'book_id', 'rating'])
