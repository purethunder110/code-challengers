from .templateManager import app
from fastapi import Request


app.post("/api/login/")
async def authenticate(request:Request):
    print("this is a test")