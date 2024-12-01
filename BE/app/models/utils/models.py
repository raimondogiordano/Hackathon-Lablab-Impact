from pydantic import BaseModel


class ResponseModel(BaseModel):
    status: bool=True
    body: dict |str| None|list=None
    status_code:str|int


class ErrorModel(BaseModel):
    status: bool=False
    message: str
    status_code:str|int

    
    
template=ResponseModel|ErrorModel