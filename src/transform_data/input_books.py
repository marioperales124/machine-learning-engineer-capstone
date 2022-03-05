from pandas import DataFrame, read_csv
from config import PATH_BOOKS, BOOKS_LIST_VALUES


class BooksReader:
    """
    Class in charge of reading books data
    """

    def __init__(self):
        """
        PATH_BOOKS, BOOKS_LIST_VALUES are constants of config.py
        """
        self.df = self.read_data(PATH_BOOKS, BOOKS_LIST_VALUES)

    def read_data(self, path: str, list_values: list) -> DataFrame:
        """
        :param path: Path where data is located
        :param list_values: List containing the indexes of csvs
        :return: Whole books dataset with all csvs concatenated
        """
        df = DataFrame()
        for ind, val in enumerate(list_values):
            if ind == 0:
                path_read = path.format(str(val), list_values[ind+1])
                df = df.append(read_csv(path_read))
            elif (ind + 1) != len(list_values):
                path_read = path.format(str(val)+'k', list_values[ind+1])
                df = df.append(read_csv(path_read))
        return df

    def get_data(self) -> DataFrame:
        """
        Method to access the dataframe build in the constructor
        :return: Books dataset
        """
        return self.df
