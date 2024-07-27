from .templateManager import app
from .datamodel_control import LoginValidate,SignupValidate
from . import EmailService
from . import DBmanage


@app.post("/auth/login/")
async def authenticate(auth:LoginValidate):
    print(f"email:{auth.EmailID},pass:{auth.Password}")


@app.post("/auth/create/")
async def create_account(data:SignupValidate):
    DBmanage.create_user(username=data.Username,email=data.EmailID,password=data.Password)
    print(f"email:{data.EmailID},username:{data.Username},password:{data.Password}")

@app.post("/auth/2FA/")
async def authorise_account():  
    print("this is a test")