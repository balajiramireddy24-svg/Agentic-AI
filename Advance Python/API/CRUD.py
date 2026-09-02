from fastapi import FastAPI,HTTPException
from pydantic import BaseModel


app= FastAPI()

item_db ={
    1:{"Name":"Biryani", "Price":150,"is_offer": True },
    2:{"Name":"Mutton","Price":400,"is_offer": False },
    3:{"Name":"Bagara rice","price":100,"is_offer": False }

}

class ITEM(BaseModel):
    name: str
    price:int
    is_offer :bool

@app.post("/item/")
def create_item(item:ITEM):
    new_id= max(item_db.keys(), default=0)+ 1
    item_db[new_id]= item.dict()
    return item_db[new_id]

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in item_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return item_db[item_id]

@app.put("/item/{item_id}")
def update_item(item_id : int,item :ITEM):
    if item_id not in item_db:
        raise HTTPException(status_code=404,detail="Item Not Found")
    return item_db[item_id]

@app.delete("/item/{item_id}")
def delete_item(item_id : int):
    if item_id not in item_db:
        raise HTTPException(status_code=404,detail="Item Not Found ")
    deleted_item=item_db.pop(item_id)
    return deleted_item
