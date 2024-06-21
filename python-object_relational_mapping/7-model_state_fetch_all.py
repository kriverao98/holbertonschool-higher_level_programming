#!/usr/bin/python3
"""
This script lists all the states from the database using SQLAlchemy.

The script takes three command-line arguments:
    1. The username for the MySQL database
    2. The password for the MySQL database
    3. The name of the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create the engine to connect to the MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    
    # Create all the tables defined in the Base class
    Base.metadata.create_all(engine)
    
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Retrieve all the states from the 'states' table and print them
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    
    # Close the session
    session.close()
