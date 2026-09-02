# Get API call: to recieve the data from Server to client

#importing the fast API library
from fastapi import FastAPI


#Creating fastapi Object 
app = FastAPI()

@app.get("/")
def hello():
    return "Welcome to FastAPI"

