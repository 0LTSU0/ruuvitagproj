import mysql.connector
from mysql.connector import Error
import pandas as pd
import time


def create_db_connection(host_name, user_name, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as e:
        print("Error:", e)

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as e:
        print("Error querying:", e)


def ruuvi_to_db(table, datadict):
    connection = create_db_connection("localhost", "pi", "ruuvidata")
    insert_q = "INSERT INTO {} (humidity, temperature, pressure, battery, timestamp) VALUES ({}, {}, {}, {}, {});".format(table, datadict.get("humidity"), datadict.get("temperature"), datadict.get("pressure"), datadict.get("battery"), time.time())
    if connection:
        execute_query(connection, insert_q)

if __name__ == "__main__":
    connection = create_db_connection("localhost", "pi", "ruuvidata")

    if connection:
        test_insert = "INSERT INTO olohuone (humidity, temperature, pressure, battery) VALUES (12.34, 56.78, 67.89, 1234);"
        execute_query(connection, test_insert)