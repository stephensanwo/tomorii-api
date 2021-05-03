from pydantic import BaseModel, Field, EmailStr, ValidationError, validator, root_validator
from bson import ObjectId
from database.users_db import find_user_by_email
import bcrypt
import datetime


class User(BaseModel):
    username: str = Field(title="The username of the user")
    email: str = Field(
        title="The email address of the user")
    password: str = Field(title="The password of the user")
    confirm_password: str = Field(
        title="The password confirmation of the user")
    first_name: str = Field(
        title="The last name of the user")
    last_name: str = Field(title="The first name of the user")
    role: str = Field(default="user")

    def user_output(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": str(bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "role": self.role
        }

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "tomorii_123",
                "email": "tomorii@tomorii.com",
                "first_name": "Tomorii",
                "last_name": "Gbenle",
                "password": "password123",
                "confirm_password": "password123"
            }
        }
