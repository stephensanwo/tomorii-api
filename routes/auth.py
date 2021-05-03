from fastapi import APIRouter
from fastapi import FastAPI, HTTPException, status, Response, BackgroundTasks
from fastapi.responses import JSONResponse
from schema.Users import User
from database import users_db
from utils.exceptions import Exceptions
from utils import validators
from utils import auth
from utils.config import Settings

auth_route = APIRouter()
settings = Settings()

# @route   POST /signup
# @desc    Create New Application User
# @access  Public


@auth_route.post("/signup", status_code=201)
async def signup(user: User, background_tasks: BackgroundTasks):

    # Validate user input
    errors, valid = validators.validateRegistrationInput(user.dict())

    if not valid:
        raise HTTPException(status_code=400, detail=errors)

    # Check if user email already exists
    user_email = await users_db.find_user_by_email(user.email)
    print(user_email)
    if user_email != None:
        raise HTTPException(status_code=409, detail={
                            "email":  Exceptions(
                                loc="email",
                                msg="Email already exists"
                            ).dict()})

    # Check if username has been taken
    user_username = await users_db.find_user_by_username(user.username)
    print(user_username)
    if user_username != None:
        raise HTTPException(status_code=409, detail={
                            "username":  Exceptions(
                                loc="username",
                                msg="Username already taken"
                            ).dict()})

    user = await users_db.create_new_user(user.user_output())
    print(user)

    # Generate JWT
    jwt_token = await auth.generateJWT(user)

    return jwt_token


if __name__ == "__main__":
    uvicorn.run("api:api", host="127.0.0.1", port=8123, reload=True)
