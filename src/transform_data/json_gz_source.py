import gzip
import json
import pandas as pd
from src.transform_data.transform_table import TransformTable


class JsonGzSource(TransformTable):

    def __init__(self, path, head=None):
        super().__init__(path)
        self.df = self.__read_table(head)

    def __read_table(self, head=None):
        count = 0
        data = []
        with gzip.open(self.path) as fin:
            for line in fin:
                dict = json.loads(line)
                count += 1
                data.append(dict)

                # break if reaches the 100th line
                if (head is not None) and (count > head):
                    break
        return pd.DataFrame.from_dict(data)
