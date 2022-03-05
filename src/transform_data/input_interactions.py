from pandas import DataFrame, read_csv
from config import PATH_INTERACTIONS, INTERACTIONS_LIST_VALUES, RATING_MAP, SURPRISE_DATASET_COLS


class InteractionsReader:
    """
    Class in charge of reading interactions data. (User-item ratings)
    """
    def __init__(self, col_rating='Rating'):
        self.df = self.read_data(PATH_INTERACTIONS, INTERACTIONS_LIST_VALUES)
        self.df[col_rating] = self.df[col_rating].map(RATING_MAP)
        self.df.columns = SURPRISE_DATASET_COLS

    def read_data(self, path: str, list_values: list) -> DataFrame:
        """
        :param path: Path where data is located
        :param list_values: List containing the indexes of csvs
        :return: Whole books dataset with all csvs concatenated
        """
        df = DataFrame()
        for ind, val in enumerate(list_values):
            if (ind + 1) != len(list_values):
                path_read = path.format(val, list_values[ind + 1])
                df = df.append(read_csv(path_read))
        return df

    def get_data(self):
        """
        Method to access the dataframe build in the constructor
        :return: Books dataset
        """
        return self.df
