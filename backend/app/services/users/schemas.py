from pydantic import BaseModel, ConfigDict, Field

class UserBase(BaseModel):
    username: str = Field(min_length=2, max_length=128)

class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=256)

class UserLogin(UserBase):
    password: str = Field(min_length=8, max_length=256)

class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
