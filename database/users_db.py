import motor.motor_asyncio
from pydantic import EmailStr


# from bson import ObjectId
# from decouple import config

def create_db_connection():
    client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
    #client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
    db = client.tomorii
    users = db.get_collection('users')
    return db, users


def close_db_connection(db):
    db.close()


async def find_user_by_email(email: EmailStr) -> dict:
    db, users = create_db_connection()
    user = await users.find_one({"email": email})
    return user


async def find_user_by_username(username: str) -> dict:
    db, users = create_db_connection()
    user = await users.find_one({"username": username})
    return user


async def create_new_user(user: dict) -> dict:
    db, users = create_db_connection()
    # Validate that the user doesnt exist
    user = await users.insert_one(user)
    new_user = await users.find_one({"_id": user.inserted_id})
    return new_user


async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students


async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


async def retrieve_student(id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)


async def delete_student(id: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(id)})
        return True


async def update_student_data(id: str, data: dict):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        student_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True
