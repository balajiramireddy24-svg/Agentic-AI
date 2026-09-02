#get API call with QUERY PARAMETER 

from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def greet_user(name:str = "Prabhas "):
    return {f"Hello Mr.{name}, Which is  your lastest release Movie "}