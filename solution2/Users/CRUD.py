from Users.schemas import User

def addUser(user: User) -> dict:
    responce = user.model_dump()
    result = True
    return {
        "result": result,
        "User": responce,

    }
