#!/usr/bin/python3

"""
script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
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
    search_name = sys.argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()

    arg_state = session.query(State).filter_by(name=search_name).first()
    if arg_state:
        print(f'{arg_state.id}')
    else:
        print("Not found")
    session.close()
