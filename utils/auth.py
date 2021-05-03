import jwt
import datetime
import os
from functools import wraps
from .config import Settings

# Generate JWT Token

settings = Settings()


async def generateJWT(user):
    SECRET_KEY = settings.jwt_secret
    timeLimit = datetime.datetime.utcnow() + datetime.timedelta(minutes=180)

    payload = {
        "_id": str(user["_id"]),
        "username": user['username'],
        "email": user['email'],
        "first_name": user['first_name'],
        "last_name": user['last_name'],
        "role": user['role'],
        "exp": timeLimit
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    token_data = {
        "token": token.decode("UTF-8"),
        "elapse_time": f"{timeLimit}"
    }

    return token_data


# Generator Function to require JWT Token on routes

# def require_admin(function):
#     @wraps(function)
#     def wrap():

#         SECRET_KEY = os.environ.get("SECRET_KEY")

#         if request.headers['Authorization'] != '' and request.headers['Authorization'] != None:
#             token = request.headers['Authorization'].split("Bearer ")[1]
#             try:
#                 data = jwt.decode(token, SECRET_KEY,
#                                   algorithms=['HS256'])
#                 if data["admin"] == False:
#                     return make_response(jsonify(errors={"unauthorized": "401", "message": "Not an Admin"}), 401)
#                 else:
#                     return function()
#             except jwt.exceptions.ExpiredSignatureError:
#                 return_data = {
#                     "error": "1",
#                     "message": "Expired Token"
#                 }
#                 return make_response(jsonify(return_data), 401)

#             except jwt.exceptions.InvalidTokenError:
#                 return_data = {
#                     "error": "1",
#                     "message": "Invalid Token"
#                 }
#                 return make_response(jsonify(return_data), 401)
#         else:
#             return_data = {
#                 "error": "2",
#                 "message": "Token required",
#             }
#             return make_response(jsonify(return_data), 401)

#     return wrap
