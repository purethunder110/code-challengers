from templateManager import app
from datamodel_control import source_Code

#for recieving the code
@app.post("/api/code-reciever/")
async def recieve_source_code(code_metadata:source_Code):
    judgement_flag=True
    response={
        "judgement":judgement_flag,
    }
    return response

@app.get("/api/new-question/")
async def send_ai_question():
    response={
        "new-question":"this is just a test",
    }
    return response