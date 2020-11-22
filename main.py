from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    phone: str = Query(None, min_length=11, max_length=11, regex="^09")
 
@app.post("/")
def user(user: User):
    return user
    
@app.get("/div/")
async def divition(a: int, b: int):
    div = a/b
    return int(div)