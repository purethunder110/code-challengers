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

@app.get("/account/login",response_class=HTMLResponse)
async def login(request:Request):
    message={}

    return templates.TemplateResponse(
        request=request,
        name="loginpage.html",
        context=message
    )