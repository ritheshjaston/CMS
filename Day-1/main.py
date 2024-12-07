from fastapi import FastAPI
import asyncio
app = FastAPI()


@app.get("/")
def root():
    return "Hello world"

@app.get("/users")
def user():
    a=10
    b=20
    return a+b

@app.post("/postdata")
def postdata(firstname:str, lastname: str):
    return firstname+" "+ lastname


@app.put("/updatedata")
def update(firstname:str, lastname:str):
    return firstname +""+lastname


@app.get("/login")
async def login(username,password):
    await asyncio.sleep(2) 
    if(username=="rithesh"):
        return "Authentic User"
    else:
        return {
            "error":"Not an Authentic User",
            "username":username,
            "password":password
        }
    

@app.get("/log")
async def log(username: str, password: str):
    print(username)  
    result = await login(username, password)  
    print(result)
    print("Completion") 
    return result 

@app.get("/logs")
def logs(username: str, password: str):
    print(username)
    result = login(username, password)  
    print(result)
    print("Completion")
    return result
