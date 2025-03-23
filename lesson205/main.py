import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Create Read Update Delete
# SQL - INSERT SELECT UPDATE DELETE

# WARNING: deleting without WHERE clause
# cursor.execute(
#     f'DELETE FROM {TABLE_NAME}'
# )

# Safer DELETE
# cursor.execute(
#     f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
# )
connection.commit()

# Create table if it doesn't exist
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Insert values into the table columns
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:name, :weight)'
)
# cursor.execute(sql, ['Joseph', 4])
# cursor.executemany(
#     sql,
#     (
#         ('Joseph', 4), ('Joestar', 5)
#     )
# )
cursor.execute(sql, {'name': 'No name', 'weight': 3})
cursor.executemany(sql, (
    {'name': 'John', 'weight': 3},
    {'name': 'Doe', 'weight': 2},
    {'name': 'Joe', 'weight': 4},
    {'name': 'Tho', 'weight': 5},
))
connection.commit()


if __name__ == '__main__':
    print(sql)

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = 1'
    )
    connection.commit()

    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="ANY", weight=67.89 '
        'WHERE id = 2'
    )
    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    connection.close()
