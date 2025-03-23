# PyMySQL - a MySQL client written in pure Python
# Docs: https://pymysql.readthedocs.io/en/latest/
# PyPI: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os
from typing import cast

import dotenv
import pymysql
import pymysql.cursors

TABLE_NAME = 'customers'
CURRENT_CURSOR = pymysql.cursors.DictCursor

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=CURRENT_CURSOR,
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(  # type: ignore
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        # WARNING: THIS CLEARS THE TABLE
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  # type: ignore
    connection.commit()

    # Start manipulating data from here

    # Inserting a value using placeholders and an iterable
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%s, %s) '
        )
        data = ('Luiz', 18)
        cursor.execute(sql, data)  # type: ignore
    connection.commit()

    # Inserting a value using placeholders and a dictionary
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data2 = {
            "age": 37,
            "name": "Le",
        }
        cursor.execute(sql, data2)  # type: ignore
    connection.commit()

    # Inserting multiple values using placeholders and a tuple of dictionaries
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data3 = (
            {"name": "Sah", "age": 33},
            {"name": "Julia", "age": 74},
            {"name": "Rose", "age": 53},
        )
        cursor.executemany(sql, data3)  # type: ignore
    connection.commit()

    # Inserting multiple values using placeholders and a tuple of tuples
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%s, %s) '
        )
        data4 = (
            ("Siri", 22),
            ("Helen", 15),
            ("Luiz", 18),
        )
        cursor.executemany(sql, data4)  # type: ignore
    connection.commit()

    # Reading values using SELECT
    with connection.cursor() as cursor:
        # min_id = int(input('Enter minimum id: '))
        # max_id = int(input('Enter maximum id: '))
        min_id = 2
        max_id = 4

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s'
        )

        cursor.execute(sql, (min_id, max_id))  # type: ignore
        data5 = cursor.fetchall()  # type: ignore

        # for row in data5:
        #     print(row)

    # Deleting using DELETE with WHERE and placeholders in PyMySQL
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s'
        )
        cursor.execute(sql, (1,))  # type: ignore
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')  # type: ignore
        # for row in cursor.fetchall():  # type: ignore
        #     print(row)

    # Updating using UPDATE with WHERE and placeholders in PyMySQL
    with connection.cursor() as cursor:
        cursor = cast(CURRENT_CURSOR, cursor)

        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET name=%s, age=%s '
            'WHERE id=%s'
        )
        cursor.execute(sql, ('Eleonor', 102, 4))

        cursor.execute(
            f'SELECT id from {TABLE_NAME} ORDER BY id DESC LIMIT 1'
        )
        last_id_from_select = cursor.fetchone()

        result_from_select = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        data6 = cursor.fetchall()

        for row in data6:
            print(row)

        print('result_from_select', result_from_select)
        print('len(data6)', len(data6))
        print('rowcount', cursor.rowcount)
        print('lastrowid', cursor.lastrowid)
        print('manual lastrowid', last_id_from_select)

        cursor.scroll(0, 'absolute')
        print('rownumber', cursor.rownumber)

    connection.commit()
