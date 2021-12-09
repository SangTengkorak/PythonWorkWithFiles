import csv
import pandas as pd


def display_csv_reader():
    with open('monsters.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print(row[2])  # Print specific column in .csv


def display_csv_reader_dict():
    with open('monsters.csv', 'r') as f:
        dictReader = csv.DictReader(f, delimiter=',')
        for row in dictReader:
            # call column contents by column name
            print(row["monsterName"] + " is priced at " + row["price"])


def display_csv_pandas():
    df = pd.read_csv('monsters.csv', index_col='imageFile')
    print(df)


if __name__ == "__main__":
    # display_csv_reader()
    # display_csv_reader_dict()
    display_csv_pandas()
