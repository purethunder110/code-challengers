from .templateManager import app
from .datamodel_control import LoginValidate
from .EmailHandler import EmailMessenger


@app.post("/auth/login/")
async def authenticate(auth:LoginValidate):
    print("this is a test")
    print(f"email:{auth.EmailID},pass:{auth.Password}")


@app.post("/auth/create/")
async def create_account():
    print("this is a test")

@app.post("/auth/2FA/")
async def authorise_account():
    print("this is a test")