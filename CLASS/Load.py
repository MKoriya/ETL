import pandas as pd


class Load:

    def __init__(self):
        print('Load Object is Created!!')

    def totext(self, data, path, option='a'):
        with open(path, option) as file:
            file.write(data)

    def tocsv(self, data, path):
        data.to_csv(path)
