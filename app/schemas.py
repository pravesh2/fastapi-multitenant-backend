from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class TripCreate(BaseModel):
    start_location: str
    end_location: str