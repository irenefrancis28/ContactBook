from fastapi import APIRouter
from contact_book.models import Group
from contact_book.database import groups

router = APIRouter()

#groups = [{'groupName': 'family',
           #'members': ['reeta', 'francis']},
           #{'groupName': 'friends',
           #'members': ['rasha', 'nivi']}

           #]
@router.get('/groups')
def get_all_groups():
    return groups

@router.get('/group/{groupName}')
def get_group_by_name(groupName):
    for i in groups:
        if i['groupName']==groupName:
            return i
    return 'group not found'

@router.get('/group/member/{member}')
def get_group_by_member(member):
    for i in groups:
        for x in i['members']:
            if x == member:
                return i['groupName']
    return 'member not found'

@router.post('/group')
def add(group: Group):
     for i in groups:
               if i['groupName'] == group.groupName:
                    return 'group already exists. Try again'
               
     groups.append(group.model_dump())
     return 'group was successfully added'

@router.post('/group/{groupName}')
def add_member(groupName: str, new_members : list[str]):
      for i in groups:
        if i['groupName']==groupName:
             existing_members=i['members']
             existing_members += new_members
             return i
      return 'group does not exist'

@router.delete('/group/{member}/{groupName}')
def delete_member(groupName: str, member: str):
     for i in groups:
        if i['groupName']== groupName:
          for x in i['members']:
              existing_members=i['members']
              if x == member:
                  existing_members.remove(x)
                  return i
          return 'member does not exist'
     return 'group does not exist'
                  
     
@router.delete('/group/{groupName}')
def delete_group(groupName):
    for i in groups:
        if i['groupName']== groupName:
            groups.remove(i)
            return groups
    return 'group was not found'


             
     

