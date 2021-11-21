from config import InitConstants
from src.transform_data.csv_source import CsvSource


class Books(InitConstants, CsvSource):

    def __init__(self):
        InitConstants.__init__(self)
        CsvSource(self.books_path).__init__(self)

