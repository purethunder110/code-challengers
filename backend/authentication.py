from .templateManager import app
from fastapi import Request
from .datamodel_control import LoginValidate


@app.post("/auth/login/")
async def authenticate(request:Request,auth:LoginValidate):
    print("this is a test")
    print(f"email:{auth.EmailID},pass:{auth.Password}")