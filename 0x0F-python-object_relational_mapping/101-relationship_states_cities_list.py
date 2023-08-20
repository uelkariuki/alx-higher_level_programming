#!/usr/bin/python3

"""
script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import State, Base
from relationship_city import City
""" importing required modules"""

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:\
{sys.argv[2]}@localhost:3306/{sys.argv[3]}', echo=False)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).all()

    for state in all_states:
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    session.commit()
    session.close()
