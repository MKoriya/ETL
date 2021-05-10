from CLASS.Extract import Extract
from CLASS.Load import Load
from CLASS.Transform import Transform

import re
import pandas as pd


def main():

    flag = True
    print('---Welcome to ETF console application---')
    reader = Extract()      # Created Extract object to read file
    tranform = Transform()  # Created Transform object
    writer = Load()         # Created Load object to write file

    while flag:

        # Extract Operation
        print('''
        1. Text File
        2. CSV File
        3. Database
        ''')
        file_type = int(input('Choose File Type(1/2/3): ')
                        )             # Taking User Input to choose file type

        # Reading file according to its type
        if file_type == 1:
            file_path = input('Enter file Path: ')
            data = reader.fromtext(file_path)       # Reading .txt file
        elif file_type == 2:
            file_path = input('Enter file Path: ')
            data = reader.fromcsv(file_path)        # Reading .csv file
        elif file_type == 3:
            print('Database Implementataion is yet to complete')
        else:
            print('Error!! You may have entered wrong value. Please Try Again!')

        print('---Extraction Complete---')
        print()

        # Transform Operation
        print('''
        1. Capitalize the Words
        2. Count the Word
        ''')
        trans_fun = int(input('Choose the Transformation(1/2): ')
                        )      # Taking User Input
        if trans_fun == 1:
            data = tranform.wordCap(data)
        elif trans_fun == 2:
            data = tranform.wordCount(data)
        else:
            print('Error!! You may have entered wrong value. Please Try Again!')

        print('---Transformation Complete---')
        print()

        # Load Operation
        print('''
        1. Text File
        2. CSV File
        3. Database
        ''')
        file_type = int(input('Choose File Type(1/2/3): ')
                        )             # Taking user Input

        if file_type == 1:
            file_path = input('Enter file Path: ')
            writer.totext(data, file_path)              # writing to .txt file
        elif file_type == 2:
            file_path = input('Enter file Path: ')
            writer.tocsv(data, file_path)               # writing to .csv file
        elif file_type == 3:
            print('Database Implementataion is yet to complete')
        else:
            print('Error!! You may have entered wrong value. Please Try Again!')

        choice = input('You want to continue?(Y/N): ')
        if choice.lower() == 'n':
            flag = False


if __name__ == '__main__':
    main()
