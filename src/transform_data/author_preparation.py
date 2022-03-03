from pandas import DataFrame
import numpy as np


class AuthorPreparation:

    def __init__(self, df_interactions, df_books, alpha, col_author='Author'):
        self.df = df_interactions.merge(df_books, how='left', on='item_des')
        self.df.fillna('Unknown', inplace=True)  # There are some nulls values in author feature
        self.df.columns = list(df_interactions.columns) + [col_author]
        self.alpha = alpha  # Parameter k in documentation
        self.col_author = col_author

    def put_author_bias(self) -> DataFrame:
        ratings_aut_col = f'ratings_{self.col_author}'
        self.df[ratings_aut_col] = self.df.groupby(
            [self.col_author, 'item_des'])['ratings'].transform(np.mean)
        self.df['ratings'] = (1 - self.alpha) * self.df['ratings'] + self.alpha * self.df[ratings_aut_col]
        return self.df
