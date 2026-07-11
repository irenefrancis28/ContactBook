from fastapi import Depends, APIRouter
from contact_book.models import Contact
from contact_book.database import contacts
from sqlalchemy.orm import Session
from contact_book.database import get_db
import contact_book.database_models as database_models

router = APIRouter()

@router.get('/contacts')
def get_all_contacts(db: Session = Depends(get_db)):
    db_contacts = db.query(database_models.Contact).all()
    return db_contacts

@router.get('/contact/{name}')
def get_contact_by_name(name: str,db: Session = Depends(get_db)):
    contact = db.query(database_models.Contact).filter(database_models.Contact.name == name).first()
    if not contact:
        return {"message": "not found"}

    return {
        "name": contact.name,
    "mobileNo": contact.mobileNo}

@router.post('/contact')
def add(contact: Contact, db: Session = Depends(get_db)):
     existing_name=db.query(database_models.Contact).filter(database_models.Contact.name == contact.name).first()
     if existing_name:
          return 'Name already exists. Try again'
     existing_no= db.query(database_models.Contact).filter(database_models.Contact.mobileNo==contact.mobileNo).first()
     if existing_no:
          return 'Number already exists. Try again' 
     db.add(database_models.Contact(**contact.model_dump()))
     db.commit()
     return contact
      

@router.delete('/contact/{name}')
def remove(name):
    for i in contacts:
         if i['name']==name:
              contacts.remove(i)
              return 'the contact was removed'
    return 'contact not found'

@router.put('/contact')
def update(contact: Contact):
     for i in contacts:
               if i['name'] == contact.name:
                    for x in contacts:
                        if x['mobileNo']==contact.mobileNo:
                            return 'Number already exists. Try again'
                    i['mobileNo']=contact.mobileNo
                    return 'contact was successfully updated'
     return 'contact not found'