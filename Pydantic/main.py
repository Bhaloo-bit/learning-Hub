from pydantic import BaseModel, Field 
from typing import List, Dict, Optional
# why? pydantic  ..pydan
class User(BaseModel):
    id : int
    name: str
    is_active: bool


input_data ={'id': 101, 'name': "Bipul Nirala", 'is_active': True }

user = User(**input_data)
print(user)    

# TODO : Create Product model with id , name, price, in_stock

data = {
    'id': 1,
    'name': 'Apple',
    'price': 30.5,
    'in_stock' : True
}     

class Product(BaseModel):
    id : int
    name : str
    price: float
    in_stock:bool

product = Product(**data)


print(product)

# more

class Cart(BaseModel):
    user_id : int
    items: list[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    title : str
    content : str
    image_url: Optional[str] = None

# todo Create Employee model
# Fields
# -id : int
# name: str(min 3 chars)
# - department : Optional str( Default 'General')
# - salary: Float (must be >= 10000)

class Employee(BaseModel):
    id : int
    name : str = Field(
                    ..., 
                    min_lenght = 3,
                    max_length = 40,
                    description= "Employee Name",
                    examples= "Bipul name"

                    )
    department: Optional[str] = 'General'
    salary: float = Field(..., ge=10000)


from fastapi import FastAPI
from pydantic import BaseModel, field_validator, model_validator,computed_field

class User(BaseModel):
    username : str

    @field_validator('username') # mode before
    def username_length(cls, v):  # cls - class, v = values
        if len(v) < 4:
            raise ValueError("Username must be at least u char")
        return v

class SignupData(BaseModel):
    password: str
    confirm_password : str

    @model_validator(mode='after') # to apply custom field validator
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("password did not match")
        return values

class Product(BaseModel):
    price: float
    quantity: int


    @computed_field  # on the go fields
    @property
    def total_price(self) -> float:
        return self.price * self.quantity


    # todo : Create Booking model
    # fields
    # - user_id: int
    # - room_id: int
    # - night: int(must be >=1)
    # - rate_per_night : float
    # Also , add computed field : total_amount = night * rate_per_night

class Booking(BaseModel):
    user: int
    room: int
    night: int 

    @field_validator(night)
    def night_spends(cls, values):
        if len(values) < 1:
            raise ValueError("night spends must be greater then 1 ")
        return values

    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.night * self.rate_per_night



            


