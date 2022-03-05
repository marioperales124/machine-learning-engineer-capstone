import pandas as pd
from surprise import Dataset, Reader

from config import SURPRISE_DATASET_COLS


class Rating:
    """
    Here we build the Dataset to be ready to the surprise model
    """
    def __init__(self, df, rating_scale=(1, 5)):
        """

        :param df: input dataframe
        :param rating_scale: Rating scale in dataset
        """
        self.df = df
        self.rating_scale = rating_scale

    def get_surprise_dataset(self) -> Dataset:
        """

        :return: Surprise Dataset to use surprise models.
        """
        try:
            self.df.columns = SURPRISE_DATASET_COLS
        except:
            raise ValueError
        reader = Reader(rating_scale=self.rating_scale)
        return Dataset.load_from_df(self.df, reader)
