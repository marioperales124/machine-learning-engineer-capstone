import pandas as pd
from src.transform_data.transform_table import TransformTable


class CsvSource(TransformTable):

    def __init__(self, path):
        super().__init__(path)
        self.df = self.__read_table()

    def __read_table(self):
        return pd.read_csv(self.path)