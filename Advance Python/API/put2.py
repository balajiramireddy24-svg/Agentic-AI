#put :update the records on the server 
#HTTPException : stop processing at seerver level and generate Error send to client 

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()
class student(BaseModel):
    name : str 
    age : int
student_data ={}

@app.post ("/student/")
def create_student(s:student):
    student_data[s.name]=s.age
    return student_data

@app.put("/student /{name}")
def update_student(name :str ,s:student ):
    if name not in student_data:
        raise HTTPException(status_code=404, detail=" student Not found ")
    student_data[name]=s.age 
    return student_data

