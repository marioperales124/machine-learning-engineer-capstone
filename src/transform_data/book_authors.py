from config import InitConstants
from src.transform_data.json_gz_source import JsonGzSource


class BookAuthors(InitConstants, JsonGzSource):

    def __init__(self):
        InitConstants.__init__(self)
        JsonGzSource(self.books_author_path, None).__init__(self)