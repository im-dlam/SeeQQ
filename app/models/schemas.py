from pydantic import BaseModel


class work(BaseModel):
    name : str
    id   : str