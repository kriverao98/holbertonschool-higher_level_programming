#!/usr/bin/python3
    """
    Creates a database using SQLAlchemy and the provided arguments.
    """
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)

def create_database():
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_database()
