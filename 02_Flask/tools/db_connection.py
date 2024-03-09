import sqlite3

from settings import DB_NAME


def db_query(query: str) -> list[tuple]:
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        response = cursor.fetchall()
    return response
