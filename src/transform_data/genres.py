from src.transform_data.json_gz_source import JsonGzSource
from config import InitConstants


class Genres(JsonGzSource):

    def __init__(self, head=None):
        genres_path = InitConstants().genres_path
        super().__init__(genres_path, head)
        
    def transform(self):
        self.df['genres_mode'] = self.df['genres'].apply(
            lambda d: max(d, key=lambda k: d[k]) if len(d) != 0 else 'No genre')
        self.df['genres_mode_conf'] = self.df['genres'].apply(
            lambda d: max(d.values()) / sum(d.values()) if ((len(d) != 0) and (sum(d.values()) != 0))
            else 0)
        return self.df[['book_id', 'genres_mode', 'genres_mode_conf']]
