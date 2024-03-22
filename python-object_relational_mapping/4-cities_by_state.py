#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    # Get the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query
    cursor.execute("SELECT cities.id, cities.name, states.name "
                   "FROM cities JOIN states ON cities.state_id = states.id "
                   "ORDER BY cities.id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
