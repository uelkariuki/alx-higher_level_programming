#!/usr/bin/python3

"""
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
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
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY\
            states.id ASC".format(search_name)
    cursor.execute(query)

    states_list = cursor.fetchall()
    for row in states_list:
        print(row)

    cursor.close()
    db_conn.close()
