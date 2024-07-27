from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from DB.DBmanager import DBmanagerclass

from .EmailHandler import EmailMessenger

app= FastAPI()

templates=Jinja2Templates(directory="frontend/templates")
app.mount("/node",StaticFiles(directory="frontend/node_modules/"),name="node_modules")
app.mount("/static",StaticFiles(directory="frontend/static/"),name="static")

DBmanage=DBmanagerclass()

EmailService=EmailMessenger()