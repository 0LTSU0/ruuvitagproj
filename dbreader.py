import mysql.connector
from mysql.connector import Error
from dbwriter import create_db_connection


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


def get_last_row(table):
    connection = create_db_connection("localhost", "pi", "ruuvidata")
    get_last_q = "SELECT * FROM {} ORDER BY timestamp DESC LIMIT 1".format(table)
    if connection:
        return read_query(connection, get_last_q)


def get_history(table):
    connection = create_db_connection("localhost", "pi", "ruuvidata")
    get_last_q = "SELECT * FROM {} ORDER BY timestamp DESC LIMIT 50".format(table)
    if connection:
        return read_query(connection, get_last_q)


if __name__ == "__main__":
    connection = create_db_connection("localhost", "pi", "ruuvidata")
    if connection:
        test_insert = "SELECT * FROM olohuone ORDER BY timestamp DESC LIMIT 1"
        print(read_query(connection, test_insert))