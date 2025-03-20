# csv.reader and csv.DictReader
# csv.reader reads CSV files into lists
# csv.DictReader reads CSV files into dictionaries

import csv
from pathlib import Path

CSV_PATH = Path(__file__).parent / 'lesson179.csv'

# Reading CSV as a dictionary
with open(CSV_PATH, 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row['Name'], row['Age'], row['Address'])

# Alternative: Reading CSV as a list
# with open(CSV_PATH, 'r') as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)
