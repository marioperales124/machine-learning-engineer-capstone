from config import InitConstants
from src.transform_data.csv_source import CsvSource


class Users(InitConstants, CsvSource):

    def __init__(self):
        InitConstants.__init__(self)
        CsvSource(self.users_path).__init__(self)
