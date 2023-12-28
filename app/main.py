from typing import Union

from fastapi import FastAPI ,Request
from pydantic import BaseModel

import requests

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root(request: Request):
    client_host = request.client.host
    return {"client_host": client_host}

@app.get("/v1/")
def read_root():
    return {"Hello": "World"}

@app.get("/v1/")
def read_root():
    return {"Hello": "World"}


@app.get("/v1//items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("v1/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}