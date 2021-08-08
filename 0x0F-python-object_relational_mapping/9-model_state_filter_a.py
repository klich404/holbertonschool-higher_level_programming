#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import session, sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@127.0.0.1/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for i in session.query(State).filter(State.name.like('%a%')):
        print("{:d}: {}".format(i.id, i.name))
