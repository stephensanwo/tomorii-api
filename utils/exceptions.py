from pydantic import BaseModel, Field


class Exceptions(BaseModel):
    msg: str
    loc: str
    type: str = Field("error")
