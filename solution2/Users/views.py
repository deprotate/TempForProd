from fastapi import APIRouter
from Users.schemas import User
from Users.CRUD import addUser
users_router  = APIRouter(prefix="/api/user", tags= ["User"])


@users_router.post("/add_user")
def add_user(user: User):
    return addUser(user = user)