from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
#import uuid


app= FastAPI()
#additional conf variables
templates=Jinja2Templates(directory="frontend/templates")
app.mount("/node",StaticFiles(directory="frontend/node_modules/"),name="node_modules")
app.mount("/static",StaticFiles(directory="frontend/static/"),name="static")

#main coding page
@app.get("/session/{shareID}",response_class=HTMLResponse)
async def code_cave_center(request:Request,shareID):
    message={
        "Theme":"valentine",
        "test":shareID,
        "Question_screen":"this is the test content",
        "code_data":"console.log('code here')"
    }

    #return html
    return templates.TemplateResponse(
        request=request,
        name="codespace.html",
        context=message
    )

#login page
@app.get("/account/login",response_class=HTMLResponse)
async def login(request:Request):
    message={}

    return templates.TemplateResponse(
        request=request,
        name="loginpage.html",
        context=message
    )

#index page
@app.get("/")
async def index():
    return "this is tehe index page"

#
@app.get("/home/")
async def homepage():
    return "this is the homepage after login"

@app.get("/account/signup")
async def signup():
    return "this is going to be signup"