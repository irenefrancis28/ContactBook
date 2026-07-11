from pydantic import BaseModel

class Contact(BaseModel):
    name: str
    mobileNo: int

class Group(BaseModel):
    groupName : str
    members : list[str]

class Favourite(BaseModel):
    name : str