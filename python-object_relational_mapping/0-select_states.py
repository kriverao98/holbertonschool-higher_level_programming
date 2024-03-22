#!/usr/bin/python3
import MySQLdb
from sys import argv

""" This script lists all states from the database hbtn_0e_0_usa """

# The code should only be executed when run directly, not when imported
if __name__ == '__main__':

    # Establish a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor object to interact with the database
    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    # Fetch all the rows from the query result
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up resources
    cur.close()
    db.close()
