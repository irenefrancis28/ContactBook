from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
Base= declarative_base()

class Contact(Base):

    __tablename__ = 'contact_book'
    name = Column(String, primary_key=True, index=True)
    mobileNo = Column(Integer)