from fastapi import FastAPI

app = FastAPI()

@app.get("/user")
def get_user(name):
    return{
        "name": name
    }

@app.get("/skill")
def get_skill(name: str=None, skill: str=None):
    return {
        "name": name,
        "skill": skill
    }

@app.get("/product")
def get_product(limit: int=10):
    return {"limit": limit}

@app.get("/student")
def get_student():
    return {
        "name": "anushri",
        "course": "MCA",
        "skill": "FastAPI"
    }

