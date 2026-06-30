#!/usr/bin/python3
"""State Script"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_states(username, password, database):
    """Prints the state objects in database"""
    engine = create_engine('mysql://{}:{}@localhost/{}'.format(
        username, password, database
    ), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionamker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()


if name == '__main__':
    print_states(argv[0], argv[1], argv[2])
