import re
import pandas as pd


class Transform():

    def __init__(self):
        print('Tranform Object is Created!!')

    def wordCap(self, data):
        return data.upper()

    def wordCount(self, data: str):
        li = re.findall('[\w]+', data)
        unique = set(li)
        df = pd.DataFrame(0, columns=['total'], index=unique)
        for word in unique:
            for i in li:
                if word == i:
                    df.loc[word]['total'] += 1

        return df
