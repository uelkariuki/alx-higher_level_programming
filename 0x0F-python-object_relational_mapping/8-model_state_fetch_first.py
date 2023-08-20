#!/usr/bin/python3

"""
script that prints the first State object from the database hbtn_0e_6_usa
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

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f'{first_state.id}: {first_state.name}')
    else:
        print("Nothing")

    session.close()
