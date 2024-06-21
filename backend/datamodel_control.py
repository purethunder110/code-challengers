from pydantic import BaseModel,EmailStr


class source_Code(BaseModel):
    platform:str
    code:str

class LoginValidate(BaseModel):
    EmailID:EmailStr
    Password:str