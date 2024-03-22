#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python 4-cities_by_state.py <mysql_username>\
              <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    # Get the command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to retrieve cities of the given state
    cursor.execute("SELECT cities.id, cities.name, states.name \
                   FROM cities JOIN states ON cities.state_id = states.id \
                   WHERE states.name = %s ORDER BY cities.id ASC",
                   (state_name,))

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
