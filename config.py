PATH_DATA = '../data/'
PATH_BOOKS = PATH_DATA + 'book{0}-{1}k.csv'
PATH_INTERACTIONS = PATH_DATA + 'user_rating_{0}_to_{1}.csv'
BOOKS_LIST_VALUES = [1] + list(range(100, 2000, 100)) + list(range(2000, 5000, 1000))
INTERACTIONS_LIST_VALUES = list(range(0, 6000, 1000)) + [6000, 11000]
RATING_MAP = {"This user doesn't have any rating": 0,
              "did not like it": 1,
              "it was ok": 2,
              "liked it": 3,
              "really liked it": 4,
              "it was amazing": 5}
SURPRISE_DATASET_COLS = ['user_id', 'item_des', 'ratings']

BOOK_AUTHORS_COLS_OLD_NAMES = ['Name', 'Authors']
BOOK_AUTHORS_COLS = ['item_des', 'Authors']
