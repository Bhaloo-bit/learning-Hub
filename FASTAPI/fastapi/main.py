from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Welcome Home"}


data = [
    { 
        "campaign_id": 1,
        "name": "Summer Lauch",
        "due_date": datetime.now(),
        "created_at": datetime.now()
    },
    { 
        "campaign_id": 2,
        "name": "Monsoon Lauch",
        "due_date": datetime.now(),
        "created_at": datetime.now()
    }]

# path parameters
@app.get('/campaign')
async def list_campaign(data = list[data]):
    return {"database": data}


