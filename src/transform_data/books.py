from config import InitConstants
from src.transform_data.csv_source import CsvSource


class Books(InitConstants, CsvSource):

    def __init__(self):
        InitConstants.__init__(self)
        CsvSource(self.books_path).__init__(self)
        
    def transform(self):
        self.df['author_id'] = self.df['authors'].apply(lambda l: self._get_author_id(l))
        return self.df

    def _get_author_id(self, line):
        try:
            for dictionary_authors in line:
                if dictionary_authors['role'] == '':
                    return str(dictionary_authors['author_id'])
            return str(line[0]['author_id'])
        except IndexError:
            return 'Anonymous'
