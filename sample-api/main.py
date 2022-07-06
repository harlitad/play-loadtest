from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import uuid

'''keni is learning FastAPI'''

app = FastAPI()

class GuestBase(BaseModel):
    name: str
    email: str

class GuestRequest(GuestBase):
    pass

class Guest(GuestBase):
    id: str

class Guests(BaseModel):
    data: List[Guest]

guests = Guests(data = [])

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/guests/", response_model=Guests)
async def list_guests():
    return guests

@app.post("/guests/", response_model=Guest, status_code=201)
async def create_guest(guest: GuestRequest):
    data = Guest(**guest.dict(), id = str(uuid.uuid4().hex))
    guests.data.append(data)
    return data