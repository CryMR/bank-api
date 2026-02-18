from pydantic import BaseModel, EmailStr
from datetime import date

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone_number: str | None
    date_of_birth: date
    age: int

    class Config:
        from_attributes = True


class CardResponse(BaseModel):
    id: int
    owner_id: int
    card_number: str
    value: float
    type: str

    class Config:
        from_attributes = True