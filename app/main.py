from fastapi import FastAPI
from app.api.users import router as users_router

app = FastAPI(
    title="User Microservice",
    description="A simple microservice to fetch user data",
    version="1.0.0",
)

app.include_router(users_router)


@app.get("/")
async def root():
    return {"message": "Welcome to the User Microservice!"}