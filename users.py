from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    last_name: str
    cedula: int

users = [User("Alejo", "Quintero", 2112243)]

@app.get("/usersjson")
async def users():
    return [{"name": "Alejo", "last_name": "Quintero", "cedula": 2112243},
            {"name": "Luis", "last_name": "Lopez", "cedula": 1482634},
            {"name": "Carlos", "last_name": "rueda", "cedula": 245365465}]

@app.get("/usersclass")
async def users():
    return User(name= "Alejo", last_name= "Quintero", cedula= 2112243)