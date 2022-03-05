from pandas import DataFrame
import numpy as np

from config import BOOK_AUTHORS_COLS_OLD_NAMES, BOOK_AUTHORS_COLS


class AuthorPreparation:

    def __init__(self, df_interactions, df_books, alpha, col_author='Author'):
        df_books = df_books[BOOK_AUTHORS_COLS_OLD_NAMES]
        df_books.columns = BOOK_AUTHORS_COLS
        df_books = df_books.drop_duplicates(subset=BOOK_AUTHORS_COLS[0])
        self.df = df_interactions.merge(df_books, how='left', on=BOOK_AUTHORS_COLS[0])
        self.df.fillna('Unknown', inplace=True)  # There are some nulls values in author feature
        self.df.columns = list(df_interactions.columns) + [col_author]
        self.alpha = alpha  # Parameter k in documentation
        self.col_author = col_author

    def put_author_bias(self) -> DataFrame:
        ratings_aut_col = f'ratings_{self.col_author}'
        self.df[ratings_aut_col] = self.df.groupby(
            [self.col_author, 'item_des'])['ratings'].transform(np.mean)
        self.df['ratings'] = (1 - self.alpha) * self.df['ratings'] + self.alpha * self.df[ratings_aut_col]
        return self.df.drop([ratings_aut_col, self.col_author], axis=1)
