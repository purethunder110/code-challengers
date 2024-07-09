from .templateManager import app
from .datamodel_control import LoginValidate,SignupValidate
from .EmailHandler import EmailMessenger
from DB.DBmanager import DBmanagerclass

conn=DBmanagerclass()


@app.post("/auth/login/")
async def authenticate(auth:LoginValidate):
    print("this is a test")
    print(f"email:{auth.EmailID},pass:{auth.Password}")


@app.post("/auth/create/")
async def create_account(data:SignupValidate):
    print("this is a test")
    print(f"email:{data.EmailID},username:{data.Username},password:{data.Password}")

@app.post("/auth/2FA/")
async def authorise_account():  
    print("this is a test")