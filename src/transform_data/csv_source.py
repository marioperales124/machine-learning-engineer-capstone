import pandas as pd
from src.transform_data.transform_table import TransformTable


class CsvSource(TransformTable):

    def __init__(self, path, cols=None):
        super().__init__(path)
        self.df = self.__read_table(cols=cols)

    def __read_table(self, cols):
        return pd.read_csv(self.path, usecols=cols, nrows=1000) if cols is not None else pd.read_csv(self.path, nrows=1000)

    def transform(self):
        return self.df
