from __future__ import print_function

import argparse
import os
import pandas as pd

from sklearn.externals import joblib

import joblib
from surprise.prediction_algorithms.matrix_factorization import SVD

# Provided model load function
from src.transform_data.author_preparation import AuthorPreparation
from src.transform_data.input_books import BooksReader
from src.transform_data.input_interactions import InteractionsReader
from src.transform_data.rating import Rating


def model_fn(model_dir):
    """Load model from the model_dir. This is the same model that is saved
    in the main if statement.
    """
    print("Loading model.")

    # load using joblib
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    print("Done loading model.")

    return model


if __name__ == '__main__':
    # All of the model parameters and training parameters are sent as arguments
    # when this script is executed, during a training job

    # Here we set up an argument parser to easily access the parameters
    parser = argparse.ArgumentParser()

    # SageMaker parameters, like the directories for training data and saving models; set automatically
    # Do not need to change
    parser.add_argument('--epochs', type=int, default=15)
    parser.add_argument('--n_factors', type=int, default=3)
    parser.add_argument('--alpha', type=int, default=0.2)
    parser.add_argument('--model-dir', type=str, default='../model')
    args = parser.parse_args()
    # Call args
    alpha = args.alpha
    n_factors = args.n_factors
    epochs = args.n_epochs
    # Do all the process to train the model
    books_df = BooksReader().get_data()
    interactions_df = InteractionsReader().get_data()
    interactions_df = interactions_df[interactions_df.ratings != 0]
    interactions_author_bias_df = AuthorPreparation(alpha=alpha, col_author='Author',
                                                    df_interactions=interactions_df,
                                                    df_books=books_df.drop_duplicates()).put_author_bias()
    int_aut_bias_dataset = Rating(interactions_author_bias_df).get_surprise_dataset()
    model = SVD(n_factors=n_factors, n_epochs=epochs, random_state=1)
    model.fit(int_aut_bias_dataset)

    # Save the trained model
    joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))
