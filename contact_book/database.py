contacts=[{'name': 'irene', 'mobileNo':944},
          {'name': 'melvyn', 'mobileNo': 845}]

groups = [{'groupName': 'family',
           'members': ['reeta', 'francis']},
           {'groupName': 'friends',
           'members': ['rasha', 'nivi']}

           ]

favourites = [{'name': 'irene'},
              {'name': 'melvyn'}]

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import contact_book.database_models as database_models

db_url = "postgresql://postgres:NCSP@localhost:5432/contact_book"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit= False, autoflush = False, bind=engine)

def get_db():
   db = SessionLocal()
   try:
      yield db
   finally:
      db.close()

def init_db():
    db = SessionLocal()
    try:
        count = db.query(database_models.Contact).count()

        if count == 0:
            for contact in contacts:
                db.add(database_models.Contact(**contact))

            db.commit()

    finally:
        db.close()


