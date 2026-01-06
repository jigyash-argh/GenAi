from pydantic import BaseModel, EmailStr, Field
from models import PyObjectId

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: PyObjectId = Field(alias="_id")
    email: EmailStr

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
