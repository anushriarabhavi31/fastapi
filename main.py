from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/about")
def about():
    return {"message": "This page is About page!"}

@app.get("/user")
def user():
    return {"message": "this page is user page"}