PATH_DATA = '/data/'
PATH_BOOKS = PATH_DATA + 'books_info.csv'
PATH_INTERACTIONS = PATH_DATA + 'ratings.csv'
RATING_MAP = {"This user doesn't have any rating": 0,
              "did not like it": 1,
              "it was ok": 2,
              "liked it": 3,
              "really liked it": 4,
              "it was amazing": 5}
SURPRISE_DATASET_COLS = ['user_id', 'item_des', 'ratings']

BOOK_AUTHORS_COLS_OLD_NAMES = ['Name', 'Authors']
BOOK_AUTHORS_COLS = ['item_des', 'Authors']
