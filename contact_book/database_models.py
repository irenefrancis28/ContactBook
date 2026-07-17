from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
Base= declarative_base()

class Contact(Base):

    __tablename__ = 'contact_book'
    name = Column(String, primary_key=True, index=True)
    mobileNo = Column(Integer)

class Group(Base):
    __tablename__ = 'groups'
    groupName = Column(String, primary_key=True, index=True)
    members = Column(JSONB)
