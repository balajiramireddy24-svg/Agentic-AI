from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()
item_db={
    1:{"Name ": "Laptop","Price":75000,"is_offer": False },
    2:{"Name":"IPhone","Price":65000, "is_offer": True }
}
class Item(BaseModel):
    name:str 
    price:float
    is_offer:bool

@app.delete("/item/{item_id}")
def delete_item(item_id : int):
    if item_id in item_db:
        raise HTTPException(status_code=404, detail="Item not found ")
    delete_item = item_db.pop(item_id)
    return delete_item