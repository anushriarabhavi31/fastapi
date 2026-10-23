from fastapi import FastAPI

app = FastAPI()

@app.get("/student")
def get_student():
    return {
        "name": "Anushree",
        "course": "MCA",
        "skill": "FastAPI"
    }