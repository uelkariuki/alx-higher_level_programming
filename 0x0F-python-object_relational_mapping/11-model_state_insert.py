#!/usr/bin/python3

"""
script that adds the State object “Louisiana” to the database
hbtn_0e_6_usa
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

    add_state = State(name="Louisiana")

    session.add(add_state)
    session.commit()
    print(f'{add_state.id}')
    session.close()
