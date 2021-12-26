from config import InitConstants
from src.transform_data.json_gz_source import JsonGzSource


class Books(JsonGzSource):

    def __init__(self, head=None):
        super().__init__(InitConstants().books_path, head)

    def transform(self):
        selected_vars_book = ['book_id', 'is_ebook', 'average_rating', 'num_pages',
                              'authors', 'publication_year', 'text_reviews_count',
                              'ratings_count']

        self.df = self.df[selected_vars_book]

        selected_vars_book_names = ['book_id', 'is_ebook', 'average_rating_book', 'num_pages',
                                    'authors', 'publication_year', 'text_reviews_count_book',
                                    'ratings_count_book']

        self.df.columns = selected_vars_book_names
        self.df['author_id'] = self.df['authors'].apply(lambda l: self._get_author_id(l))
        return self.df

    @staticmethod
    def _get_author_id(line):
        try:
            for dictionary_authors in line:
                if dictionary_authors['role'] == '':
                    return str(dictionary_authors['author_id'])
            return str(line[0]['author_id'])
        except IndexError:
            return 'Anonymous'
