#!/usr/bin/python3

"""
script that lists all State objects that contain the letter a from
the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
""" importing required modules"""

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:\
{sys.argv[2]}@localhost:3306/{sys.argv[3]}', echo=False)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    a_state = session.query(State).order_by(State.id)\
        .filter(State.name.like('%a%'))
    for row in a_state:
        print(f'{row.id}: {row.name}')
    session.close()
