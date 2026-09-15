from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id : int
    name: str
    email: str
    is_active: bool = True
    createdAt : datetime
    address: Address
    tags: list[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime
                       ('%d-%m-%Y %H:%M:%S')}
    )
# create a user instance

user  = User(
       id = 1,
       name = "bipul",
       email = "bipul@gmail.com",
       is_active = True,
       createdAt = datetime(2026,9,15,5),
       address = Address(
          street = "gali no1",
          city = "Delhi",
          zip_code= "gh8989" 
      ),
    tags= ["premiun" ,"suscriber"]
)


# Using model_dump -> dict

python_dict = user.model_dump()
print(python_dict)

# Using model_dump_json()
json_str = user.model_dump_json
print(json_str)
