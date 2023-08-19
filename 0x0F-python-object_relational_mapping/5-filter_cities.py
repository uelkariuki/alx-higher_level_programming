#!/usr/bin/python3

"""
script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys
""" Importing the sys module"""


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    search_name = sys.argv[4]
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

    query = "SELECT cities.name FROM states\
            JOIN cities ON states.id = cities.state_id\
            WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (search_name,))

    cities_list = cursor.fetchall()
    print(', '.join(row[0] for row in cities_list))

    cursor.close()
    db_conn.close()
