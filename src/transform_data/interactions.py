from config import InitConstants
from src.transform_data.csv_source import CsvSource


class Interactions(CsvSource, InitConstants):

    def __init__(self):
        InitConstants.__init__(self)
        CsvSource(self.interactions_path).__init__(self)
