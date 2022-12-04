from pydantic import BaseModel


class Item(BaseModel):
    first_name: str
    last_name: str
    patronymic: str
    phone: str
    message: str
    
    class Config:
        orm_mode=True