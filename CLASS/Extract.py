import pandas as pd


class Extract:

    def __init__(self):
        print('Extract Object is Created!!')

    def fromcsv(self, path):
        return pd.read_csv(path)

    def fromtext(self, path):
        with open(path, 'r') as file:
            return file.read()
