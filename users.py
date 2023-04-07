from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    last_name: str
    cedula: int

users_list = [User(name="Alejo", last_name="Quintero", cedula= 2112243),
                User(name="Luis", last_name="Lopez", cedula= 1482634),
                User(name="Carlos", last_name="rueda", cedula= 245365465)]

@app.get("/usersjson")
async def users():
    return [{"name": "Alejo", "last_name": "Quintero", "cedula": 2112243},
            {"name": "Luis", "last_name": "Lopez", "cedula": 1482634},
            {"name": "Carlos", "last_name": "rueda", "cedula": 245365465}]

@app.get("/users")
async def users():
    return users_list