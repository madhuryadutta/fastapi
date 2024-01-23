from typing import Union

from fastapi import FastAPI ,Request
from pydantic import BaseModel

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import ipaddress

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root(request: Request):
    client_host = request.client.host
    return {"client_host": client_host}

@app.get("/request")
def read_root(request: Request):
    user_agent = request.headers
    outputdict={}
    for x in user_agent:
        print(x+' : '+request.headers.get(x))
        outputdict[x]=request.headers.get(x)
    json_compatible_data = jsonable_encoder(outputdict)
    return JSONResponse(content=json_compatible_data)

@app.get("/v1/")
def read_root_v1():
    return {"Hello": "World"}

@app.get("/v1//cidr2ipv4/{cidr_block}")
def cidr_to_ip_v4(cidr_block: str ):
    IP_Addr = ipaddress.ip_interface(cidr_block.replace('%2F', '/'))
    Net_Addr = IP_Addr.network
    pref_len = IP_Addr.with_prefixlen
    Mask = IP_Addr.with_netmask
    wildcard = IP_Addr.hostmask
    broadcast_address = Net_Addr.broadcast_address
    return {"Network_Address ": str(Net_Addr).split('/')[0],
            "Broadcast_Address" :  broadcast_address,
            "CIDR_Notation": pref_len.split('/')[1],
            "Subnet_Mask":  Mask.split('/')[1],
            "Wildcard_Mask" :  wildcard,
            "First_IP":  list(Net_Addr.hosts())[0],
            "Last_IP":  list(Net_Addr.hosts())[-1] }


@app.get("/v1//items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("v1/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}