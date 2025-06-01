from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Привет, FastAPI!"}

class Item(BaseModel):
    name: str
    value: int

@app.post("/items/")
async def create_item(item: Item):
    return {"message": f"Получен объект: {item.name} со значением {item.value}"}
