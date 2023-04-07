from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel

from data import lleverInfo
from extract import *
import os


SECRET = os.getenv("SECRET")

#
app = FastAPI()

class Msg(BaseModel):
    msg: str
    secret: str

# url local http://127.0.0.1:8000/

@app.get("/")
async def root():
    return "<h1>Hola Mundo</h1>"

# url local http://127.0.0.1:8000/url

class Dato(BaseModel):
    dato1: str
    dato2: str
    dato3: str
    dato4: str

list = []

lista = lleverInfo(list)

datos_list = [Dato(dato1 = lista[0], dato2 = lista[1], dato3 = lista    [2])]

@app.get("/datos")
async def root():
    return datos_list

@app.get("/url")
async def url():
    return {"url_curso": "https://mouredev.com/python"}


@app.get("/homepage")
async def demo_get():
    driver=createDriver()

    homepage = getGoogleHomepage(driver)
    driver.close()
    return homepage

@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}

