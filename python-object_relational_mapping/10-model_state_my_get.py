#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def print_state_by_name(mysql_username, mysql_password, database_name, state_name):
    """
    Prints the State object with the name passed as argument from the database.

    Args:
        mysql_username (str): The MySQL username.
        mysql_password (str): The MySQL password.
        database_name (str): The name of the database.
        state_name (str): The name of the state to search for.

    Returns:
        None
    """
    # Create engine and session
    engine = create_engine('mysql+mysqldb://{}:{}\
                           @localhost:3306/{}'.format
                           (mysql_username, mysql_password, database_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for the state name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the result
    if state:
        print(state.id)
    else:
        print("Not found")

if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function
    print_state_by_name(mysql_username, mysql_password, database_name, state_name)
