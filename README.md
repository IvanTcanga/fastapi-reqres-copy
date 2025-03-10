# User Microservice

Микросервис на FastAPI для работы с пользователями. Предоставляет API для:
- Получения данных пользователя по ID
- Создания новых пользователей

## 🚀 Быстрый старт

### Требования
- Python 3.8+
- pip

### Установка и запуск
1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/user-microservice.git
cd user-microservice
Установите зависимости:
```bash
pip install fastapi uvicorn requests pytest
Запустите сервер:
```bash
uvicorn app.main:app --reload
Сервер будет доступен по адресу: http://127.0.0.1:8000
```

## 📚 Документация API

### Эндпоинты

1. Получить пользователя
Метод: GET
URL: `/api/users/{user_id}`
Пример запроса:
```bash
curl http://localhost:8000/api/users/1
Пример ответа:
```json
{
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
```

2. Создать пользователя
Метод: POST
URL: `/api/users`
Пример запроса:
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"name": "morpheus", "job": "leader"}' \
http://localhost:8000/api/users
Пример ответа:
```json
{
  "name": "morpheus",
  "job": "leader",
  "id": 2,
  "createdAt": "2024-03-10T12:34:56.789Z"
}
```

## 🧪 Запуск тестов
Убедитесь, что сервер запущен
```bash
python -m pytest tests/test_user.py -v
Пример успешного выполнения:
```
```bash
============================= test session starts ==============================
collected 2 items

tests/test_user.py::TestUserData::test_user_data PASSED
tests/test_user.py::TestUserData::test_create_user PASSED

============================== 2 passed in 0.15s ==============================
```

## 📂 Структура проекта
```bash
user-microservice/
├── app/
│   ├── __init__.py
│   ├── main.py               # Точка входа приложения
│   ├── models/
│   │   └── user.py           # Pydantic модели данных
│   └── api/
│       └── users.py          # Реализация эндпоинтов
├── tests/
│   └── test_user.py          # Интеграционные тесты
├── README.md
└── requirements.txt          # Список зависимостей
```

## 🔧 Технические детали

### Модели данных
- UserData: Основные данные пользователя
- Support: Информация о поддержке
- UserResponse: Ответ для GET-запроса
- UserCreateRequest: Тело запроса для создания пользователя
- UserCreateResponse: Ответ на создание пользователя

### Зависимости
- FastAPI - Веб-фреймворк для создания API
- Uvicorn - ASGI-сервер для запуска приложения
- Pydantic - Валидация и сериализация данных
- Requests - HTTP-клиент для тестирования
- pytest - Фреймворк для тестирования

## ⚙️ Рекомендации по разработке
1. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
```
2. Для автоматической генерации requirements.txt:
```bash
pip freeze > requirements.txt
```