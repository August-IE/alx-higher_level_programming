#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing the letter
a from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a list to store the states to delete
    states_to_delete = []

    # Iterate over the query result and add states to delete list
    for state in session.query(State):
        if "a" in state.name:
            states_to_delete.append(state)

    for state in states_to_delete:
        session.delete(state)

    session.commit()
