from fastapi import FastAPI

app = FastAPI()


@app.get("/user/{user_id}")
def user(user_id):
    return {"message": user_id}