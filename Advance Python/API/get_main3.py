#get API call with PATH parameter 
from fastapi import FastAPI

app = FastAPI()

@app.get("/product/{id}")
def product_get(id:int):
    return  {"id":id,"Name":"Iphone17" }