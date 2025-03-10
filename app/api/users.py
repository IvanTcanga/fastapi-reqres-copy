from fastapi import APIRouter, HTTPException
from app.models.user import UserResponse, UserCreateRequest, UserCreateResponse
from datetime import datetime

router = APIRouter(prefix="/api/users", tags=["users"])

# Пример данных (обычно это будет запрос к базе данных или внешнему API)
fake_db = {
    1: {
        "data": {
            "id": 1,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
            "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
        }
    }
}


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    user = fake_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserCreateResponse, status_code=201)
async def create_user(user: UserCreateRequest):
    user_id = len(fake_db) + 1
    created_at = datetime.utcnow()
    response_data = user.dict()  # Преобразование модели в словарь
    response_data["id"] = user_id  # Добавление ID
    response_data["createdAt"] = created_at.isoformat()  # Добавление даты создания
    fake_db[user_id] = response_data
    return response_data