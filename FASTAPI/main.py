from fastapi import FastAPI, HTTPException, Response, Depends, Query
from datetime import datetime
from random import randint
from typing import Any, Annotated, Generic, TypeVar
from contextlib import asynccontextmanager
from pydantic import BaseModel


from sqlmodel import Field, Session, SQLModel, create_engine, select

class Campaign(SQLModel, table=True):
     camapaign_id : int | None = Field(default=None, primary_key=True)
     name : str = Field(index= True)
     due_date: datetime | None = Field(default=None, index= True)
     created_at: datetime  = Field(default_factory=lambda: datetime.now(), nullable=True, index= True)

class CampaignCreate(SQLModel):
     name: str
     due_date: datetime | None = None
          

sqlite_file_name = "database.db"   #file name 
sqlite_url = f"sqlite:///{sqlite_file_name}" # fileUrl

connect_args = {"check_same_thread": False} #engine to make the connections
engine = create_engine(sqlite_url, connect_args=connect_args) # engine itself

def create_db_and_table():
     SQLModel.metadata.create_all(engine)

def get_session():
     with Session(engine)as session:
          yield session  

SessionDep = Annotated[Session, Depends(get_session)]

@asynccontextmanager
async def lifespan(app: FastAPI):
     create_db_and_table()
     with Session(engine) as session:
          if not session.exec(select(Campaign)).first():
               session.add_all([
                    Campaign(name="summer Launch", due_date= datetime.now()),
                    Campaign(name="pre-winter Launch", due_date= datetime.now())
               ])
               session.commit()
     yield
     

app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    return {'message': "Welcome to basics of fast api"}

# multi line response in fast api

data = [
    { 
        "campaign_id": 1,
        "name": "Summer Lauch",
        "due_date": datetime.now(),
        "created_at": datetime.now()
    },
    { 
        "campaign_id": 2,
        "name": "Winter Lauch",
        "due_date": datetime.now(),
        "created_at": datetime.now()
    }
    ]

T = TypeVar("T")
class Responsee(BaseModel, Generic[T]):
        data : T

@app.get("/campaigns", response_model=Responsee[list[Campaign]])
async def read_campaigns(session: SessionDep):
     data = session.exec(select(Campaign)).all()
     return {"data": data}

@app.get("/campaigns/{id}", response_model= Responsee[Campaign])
async def read_campaign(id: int , session: SessionDep):
     data = session.get(Campaign, id)
     if not data:
         raise HTTPException(status_code=404,detail="code nhi chalega")
     return {"data": data}

@app.post("/campaigns", status_code=201, response_model=Responsee[Campaign])
async def create_campaign(campaign: CampaignCreate, session= SessionDep):
     db_campaign = Campaign.model_validate(campaign)
     session.add(campaign)
     session.commit()
     session.refresh(campaign)
     return {"data": db_campaign}

@app.put("/campaigns/{id}", response_class=Responsee[Campaign])
async def update_campaign(campaign_id: int , campaign: CampaignCreate, session: SessionDep):
     data = session.get("campaign", campaign_id)
     if not data:
          raise HTTPException(status_code=404,detail="lala tera code fatt gaya")
     data.name = campaign.name   
     data.due_date = campaign.due_date
     session.add(data)
     session.commit
     session.refresh(data)

     return {"campaign": data}

@app.delete("/campaings/{id}", status_code=204)
async def delete_campaings(id : int, session: SessionDep):
     data = session.get(Campaign, id)
     if not data:
          raise HTTPException(status_code=404, detail="lala company me job lagegi teri")
     session.delete(data) 
     session.commit()



"""@app.get("/campaigns")
def campaings():
    return {"message": data}

# to return collection of data in Obj
@app.get("/campaigns/{id}")
async def read_campaigns(id: int):
        for campaign in data:
            if campaign.get("campaign_id") == id:
                return {"capaigns": campaign}
        raise HTTPException(status_code=404, detail="! invalid or not found")    

# to crate data and send data
@app.post("/campaigns")
async def create_campaign(body: dict[str, Any]):
     user_input : Any = {
            "campaign_id": randint(100,1000),
            "name": body.get("name"),
            "due_date": datetime.now(),
            "created_at": datetime.now()
        }

     data.append(user_input)
     return {"campaigns": user_input}

@app.put("/campaigns/{id}")
async def update_campaigns(id : int, body : dict[str, Any]):
     for index, capgin in enumerate(data):
          if capgin.get("campaign_id") == id:
               updated : Any = {
                           "campaign_id": id,
                           "name": body.get("name"),
                           "due_date": datetime.now(),
                           "created_at": capgin.get("created_at")
                       }
          data[index] = updated
          return {"campaigns": updated}
     raise HTTPException(status_code=404, detail="updated data")

@app.delete("/campaigns/{id}")
async def delete_campain(id: int):
     for index , campain in enumerate(data):
          if campain.get("campaign_id") == id:
               data.pop(index)
               return Response(status_code=200)
          raise HTTPException(status_code=404, detail="Something went wrong")
      
     """
