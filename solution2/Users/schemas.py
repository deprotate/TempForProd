from pydantic import BaseModel, EmailStr
from typing import Annotated
from fastapi import Path, Query

class User(BaseModel):
    id: Annotated[int, Path(gt=0)]
    name: Annotated[str, Query(max_length=50) ]
    email: EmailStr