from src.transform_data.csv_source import CsvSource


class Interactions(CsvSource):

    def __init__(self, path):
        super().__init__(path)