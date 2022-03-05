from pandas import DataFrame, read_csv
from config import PATH_BOOKS, BOOKS_LIST_VALUES


class BooksReader:

    def __init__(self):
        self.df = self.read_data(PATH_BOOKS, BOOKS_LIST_VALUES)

    def read_data(self, path: str, list_values: list) -> DataFrame:
        df = DataFrame()
        for ind, val in enumerate(list_values):
            if ind == 0:
                path_read = path.format(str(val), list_values[ind+1])
                df = df.append(read_csv(path_read))
            elif (ind + 1) != len(list_values):
                path_read = path.format(str(val)+'k', list_values[ind+1])
                df = df.append(read_csv(path_read))
        return df

    def get_data(self):
        return self.df
