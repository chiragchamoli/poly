from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    profile_url: str = None
    status: str = None
    last_login: str
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True