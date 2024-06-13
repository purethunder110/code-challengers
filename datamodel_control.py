from pydantic import BaseModel


class source_Code(BaseModel):
    platform:str
    code:str