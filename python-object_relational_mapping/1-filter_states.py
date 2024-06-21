#!/usr/bin/python3

"""
This script lists all the states with a name starting with N
from the hbtn_0e_0_usa database.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, username=argv[1], password=argv[2], db_name=argv[3])

    cursor = db.cursor()
    cursor.execute=("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC");

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
