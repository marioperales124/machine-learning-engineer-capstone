class InitConstants:

    def __init__(self):
        self.s3_bucket = 'recommendation-books-data'
        folder_raw = 'raw_data'
        self.books_path = f's3://{self.s3_bucket}/{folder_raw}/goodreads_books.json.gz'
        self.interactions_path = f's3://{self.s3_bucket}/{folder_raw}/goodreads_interactions.csv'
        self.users_path = f's3://{self.s3_bucket}/{folder_raw}/user_id_map.csv'
        self.books_author_path = f's3://{self.s3_bucket}/{folder_raw}/goodreads_book_authors.json.gz'
        self.genres_path = f's3://{self.s3_bucket}/{folder_raw}/goodreads_book_genres_initial.json.gz'

        folder_transform = 'transformed_data/'
        self.s3_transform_books_path = f's3://{self.s3_bucket}/{folder_transform}/books.csv'
        self.s3_transform_interactions_path = f's3://{self.s3_bucket}/{folder_transform}/goodreads_interactions.csv'
        self.s3_transform_users_path = f's3://{self.s3_bucket}/{folder_transform}/user_id_map.csv'
        self.s3_transform_books_author_path = f's3://{self.s3_bucket}/{folder_transform}/book_authors.csv'
        self.s3_transform_genres_path = f's3://{self.s3_bucket}/{folder_transform}/book_genres.csv'
