import pandas as pd
from surprise import Dataset, Reader

from config import SURPRISE_DATASET_COLS


class Rating:
    def __init__(self, df, rating_scale=(1, 5)):
        self.df = df
        self.rating_scale = rating_scale

    def get_surprise_dataset(self) -> Dataset:
        try:
            self.df.columns = SURPRISE_DATASET_COLS
        except:
            raise ValueError
        reader = Reader(rating_scale=self.rating_scale)
        return Dataset.load_from_df(self.df, reader)
