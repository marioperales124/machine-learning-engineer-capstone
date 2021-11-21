from src.transform_data.book_authors import BookAuthors
from src.transform_data.books import Books
from src.transform_data.genres import Genres
from src.transform_data.interactions import Interactions


class TransformRun:

    def __init__(self):
        pass

    def run(self):
        # Instance objects
        books = Books()
        genres = Genres()
        authors = BookAuthors()
        interactions = Interactions()
        # Get transformed dataframes
        books_df = books.transform()
        genres_df = genres.transform()
        authors_df = authors.transform()
        interactions_df = interactions.transform()
