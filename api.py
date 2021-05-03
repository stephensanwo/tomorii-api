from fastapi import FastAPI
from utils.config import Settings
from routes.auth import auth_route
import uvicorn

settings = Settings()
api = FastAPI()
api.include_router(auth_route)


@api.get("/test")
async def root():
    return 'Success'


if __name__ == "__main__":
    uvicorn.run("api:api", host="127.0.0.1", port=8123, reload=True)
