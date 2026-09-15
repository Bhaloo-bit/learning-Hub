from typing import list, Optional
from pydantic import BaseModel

class Addreess(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Addreess # referance to upper class

class comments(BaseModel):
    id : int
    content: str
    # forward refrecening
    replies: Optional[list['comments']] = None  # reference to self/ own class

comments.model_rebuild() # very very import 

Add = Addreess(
    street = "123 Something",
    city = " Delhi",
    postal_code = "110011"
)

user = User(
    id = 1,
    name = "Bipul",
    address = Addreess
)

comment= comments(
    id = 1,
    content = "videos",
    replies= [
        comments(id=1, content="replies1"),
        comments(id=2, content="replies2"),
        comments(id=3, content="replies3")
        ]
)

# Todo : Create Course model
# Each model has modules
# Each modules has lessons

class Lesson(BaseModel):
    lesson_id: int
    topic : str

class Module(BaseModel):
     module_id: int
     name: str
     lessons: list[Lesson]    

class Course(BaseModel):
    id : int
    title: str
    modules: list[Module]     
    

