from templateManager import app
from datamodel_control import source_Code

@app.post("/api/code-reciever/")
async def recieve_source_code(code_metadata:source_Code):
    print("test")