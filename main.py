from fastapi import FastAPI
app=FastAPI()

@app.get("/user")
def user():
    return {"message": "Hello, User!"}