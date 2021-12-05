from surprise.prediction_algorithms.knns import KNNWithMeans
from surprise import Dataset, Reader
from surprise.model_selection import cross_validate
from pandas import DataFrame


class IBCFModel:

    def __init__(self, input_df: DataFrame, k: int, scale_tuple: tuple = (1, 5)):
        self.k = k
        reader = Reader(rating_scale=scale_tuple)
        self.surprise_df = Dataset.load_from_df(input_df, reader)
        self.model = self.__modelate()

    def __modelate(self):
        return KNNWithMeans(self.k)

    def cross_validate(self, measures_list: list = ['RMSE', 'MAE'], cv=5, verbose=False):
        return cross_validate(self.model,
                              self.surprise_df,
                              measures=measures_list,
                              cv=cv,
                              verbose=verbose)
