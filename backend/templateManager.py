from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from . import app,templates
#import uuid



#additional conf variables

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

#page after loging in
@app.get("/home/")
async def homepage():
    return "this is the homepage after login"

#signup page
@app.get("/account/signup",response_class=HTMLResponse)
async def signup(request:Request):
    message={}
    return templates.TemplateResponse(
        request=request,
        name="signuppage.html",
        context=message
    )