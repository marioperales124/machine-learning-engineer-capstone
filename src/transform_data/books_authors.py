from pandas import DataFrame

from config import BOOK_AUTHORS_COLS_OLD_NAMES, BOOK_AUTHORS_COLS


class BookAuthors:

    def __init__(self, df):
        df = df[BOOK_AUTHORS_COLS_OLD_NAMES]
        self.df = df[BOOK_AUTHORS_COLS]

    def get_book_authors(self) -> DataFrame:
        return self.df
