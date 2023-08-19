#!/usr/bin/python3

"""
script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa
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
    cursor.execute("SELECT * FROM states WHERE name\
        LIKE 'N%' ORDER BY states.id ASC")

    states_list = cursor.fetchall()
    for row in states_list:
        print(row)

    cursor.close()
    db_conn.close()
