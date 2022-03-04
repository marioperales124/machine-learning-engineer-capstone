from pandas import DataFrame, read_csv
from config import PATH_INTERACTIONS, INTERACTIONS_LIST_VALUES


class InteractionsReader:

    def __init__(self):
        self.books = self.read_data(PATH_INTERACTIONS, INTERACTIONS_LIST_VALUES)

    def read_data(self, path: str, list_values: list) -> DataFrame:
        df = DataFrame()
        for ind, val in enumerate(list_values):
            if ind != len(list_values):
                path_read = path.format(val, list_values[ind + 1])
                df = df.append(read_csv(path_read))
        return df
