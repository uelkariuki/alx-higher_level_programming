#!/usr/bin/python3

"""
script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys
""" Importing the sys module"""


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    MySQL_host = "localhost"
    MySQL_port = 3306

    db_conn = MySQLdb.connect(
            host=MySQL_host,
            port=MySQL_port,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name

            )

    cursor = db_conn.cursor()

    query = "SELECT cities.id, cities.name, states.name\
            FROM states JOIN cities ON cities.state_id = states.id\
            ORDER BY cities.id ASC"
    cursor.execute(query)

    cities_list = cursor.fetchall()
    for row in cities_list:
        print(row)

    cursor.close()
    db_conn.close()
