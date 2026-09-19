from fastapi import FastAPI, HTTPException, Response
from datetime import datetime
from random import randint

app = FastAPI()

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

@app.get("/campaigns")
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
      
     

        