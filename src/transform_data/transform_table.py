import boto3
import os

from config import InitConstants


class TransformTable(InitConstants):

    def __init__(self, path):
        super().__init__()
        self.path = path

    def persist_s3(self, path):
        boto3.Session().resource('s3').Bucket(self.s3_bucket).Object(
            os.path.join('reseller', 'reseller_sm.csv')).upload_file('reseller_sm.csv')

    def transform(self):
        pass

    def create_sql_table(self):
        pass
