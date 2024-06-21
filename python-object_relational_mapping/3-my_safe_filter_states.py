#!/usr/bin/python3
import MySQLdb
from sys import argv


# The code should only be executed when run directly, not when imported
if __name__ == '__main__':

    # Establish a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    # Create a cursor object to interact with the database
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
            WHERE name LIKE BINARY %(name)s\
            ORDER BY states.id ASC", {'name': argv[4]})
    # Fetch all the rows returned by the query
    rows = cur.fetchall()
    # Print each row and closes process
    if rows is not None:
        for row in rows:
            print(row)
    cur.close()
    db.close()
