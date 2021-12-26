from config import InitConstants
from src.transform_data.json_gz_source import JsonGzSource


class BookAuthors(JsonGzSource):

    def __init__(self):
        JsonGzSource(InitConstants().books_author_path, None).__init__(self)