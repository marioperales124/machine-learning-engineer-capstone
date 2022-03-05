from pandas import DataFrame

from config import BOOK_AUTHORS_COLS_OLD_NAMES, BOOK_AUTHORS_COLS


class BookAuthors:
    """
    This class is build to take the columns of books dataset that we need
    BOOK_AUTHORS_COLS_OLD_NAMES: Columns that we need with original names
    BOOK_AUTHORS_COLS: New columns names for the selected columns
    """

    def __init__(self, df):
        df = df[BOOK_AUTHORS_COLS_OLD_NAMES]
        self.df = df[BOOK_AUTHORS_COLS]

    def get_book_authors(self) -> DataFrame:
        return self.df
