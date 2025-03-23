import sqlite3

from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Fetch all records from the table
cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

print()

# Fetch a single record where id = 3
cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "2"'
)
row = cursor.fetchone()
_id, name, weight = row
print(_id, name, weight)

cursor.close()
connection.close()
