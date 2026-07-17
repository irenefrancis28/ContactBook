from fastapi import APIRouter, Depends
from contact_book.models import Group
from contact_book.database import groups
from sqlalchemy.orm import Session
from contact_book.database import get_db
import contact_book.database_models as database_models


router = APIRouter()

#groups = [{'groupName': 'family',
           #'members': ['reeta', 'francis']},
           #{'groupName': 'friends',
           #'members': ['rasha', 'nivi']}

           #]
@router.get('/groups')
def get_all_groups(db: Session = Depends(get_db)):
    db_groups = db.query(database_models.Group).all()
    return db_groups

@router.get('/group/{groupName}')
def get_group_by_name(groupName: str,db: Session = Depends(get_db) ):
     group = db.query(database_models.Group).filter(database_models.Group.groupName == groupName).first()
     if not group:
        return {"message": "not found"}

     return {
        "Group name": group.groupName,
    "members": group.members}

@router.get("/group/member/{member}")
def get_group_by_member(member: str, db: Session = Depends(get_db)):

    existing_member = db.query(database_models.Group).filter(
        database_models.Group.members.contains([member])
    ).all()

    if existing_member:
        return [
            {
                "Group name": group.groupName,
                "members": group.members
            }
            for group in existing_member
        ]

    return {"message": f"{member} not present in any group"}

@router.post('/group')
def add(group: Group, db: Session = Depends(get_db)):
     existing_group = db.query(database_models.Group).filter(database_models.Group.groupName == group.groupName).first()
     if  existing_group:
         return 'group already exists. Try again'
     db.add(database_models.Group(**group.model_dump()))
     db.commit()
     return group

@router.post('/group/{groupName}')
def add_member(groupName: str, new_members : list[str], db: Session = Depends(get_db)):
     group = db.query(database_models.Group).filter(database_models.Group.groupName == groupName).first()
     if not group:
        return 'Group does not exist. Try again'
     existing_members = list(group.members)
     for member in new_members:
        if member not in existing_members:
            existing_members.append(member)
 
     group.members = existing_members.copy()
     db.commit()
     db.refresh(group)
     return {
        "message": "Members added successfully",
        "groupName": group.groupName,
        "members": group.members
    }

@router.delete('/group/{member}/{groupName}')
def delete_member(groupName: str, member: str, db: Session = Depends(get_db) ):
     group = db.query(database_models.Group).filter(database_models.Group.groupName == groupName).first()
     if not group:
        return "Group does not exist."

     existing_members = list(group.members)
 
     if member not in existing_members:
        return "Member does not exist in this group."

     existing_members.remove(member)

     group.members = existing_members

     db.commit()
     db.refresh(group)

     return {
        "message": "Member has been deleted",
        "groupName": group.groupName,
        "members": group.members
    }
     
@router.delete('/group/{groupName}')
def delete_group(groupName, db: Session = Depends(get_db)):
    group = db.query(database_models.Group).filter(database_models.Group.groupName == groupName).first()
    if not group:
        return "Group was not found"

    db.delete(group)
    db.commit()

    return {
        "message": "Group deleted successfully",
        "groupName": groupName
    }


             
     

