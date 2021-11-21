from config import InitConstants
from src.transform_data.json_gz_source import JsonGzSource


class Genres(InitConstants, JsonGzSource):

    def __init__(self):
        InitConstants.__init__(self)
        JsonGzSource(self.genres_path, None).__init__(self)

    def transform(self):
        self.df['genres_mode'] = self.df['genres'].apply(
            lambda d: max(d, key=lambda k: d[k]) if len(d) != 0 else 'No genre')
        self.df['genres_mode_conf'] = self.df['genres'].apply(
            lambda d: max(d.values()) / sum(d.values()) if ((len(d) != 0) and (sum(d.values()) != 0))
            else 0)
        return self.df[['book_id', 'genres_mode', 'genres_mode_conf']]
