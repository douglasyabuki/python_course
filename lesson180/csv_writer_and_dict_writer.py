# csv.writer and csv.DictWriter to write data into CSV files
# csv.reader reads CSV files into lists
# csv.DictReader reads CSV files into dictionaries

import csv
from pathlib import Path

CSV_PATH = Path(__file__).parent / 'lesson180.csv'

customer_list = [
    {'Name': 'John Doe', 'Address': 'Av 1, 22'},
    {'Name': 'Joe Tho', 'Address': 'R. 2, "1"'},
    {'Name': 'Joseph Joestar', 'Address': 'Av B, 3A'},
]

# Writing CSV using DictWriter
with open(CSV_PATH, 'w', newline='', encoding='utf-8') as file:
    column_names = customer_list[0].keys()
    writer = csv.DictWriter(file, fieldnames=column_names)
    writer.writeheader()

    for customer in customer_list:
        print(customer)
        writer.writerow(customer)

# Alternative: Writing CSV using writer with lists
# customer_list = [
#     ['John Doe', 'Av 1, 22'],
#     ['Joe Tho', 'R. 2, "1"'],
#     ['Joseph Joestar', 'Av B, 3A'],
# ]
# with open(CSV_PATH, 'w', newline='', encoding='utf-8') as file:
#     column_names = ['Name', 'Address']
#     writer = csv.writer(file)

#     writer.writerow(column_names)

#     for customer in customer_list:
#         writer.writerow(customer)
