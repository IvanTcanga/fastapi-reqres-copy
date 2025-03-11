import requests
import pytest


class TestUserData:
    def test_user_data(self):
        url = "http://127.0.0.1:8000/api/users/1"
        id = 1
        email = "janet.weaver@reqres.in"
        # Сначала проверяем статус-код
        response = requests.get(url)
        assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
        # Только после проверки парсим JSON
        body = response.json()
        data = body["data"]

        assert data["id"] == id
        assert data["email"] == email

    def test_create_user(self):
        url = "http://127.0.0.1:8000/api/users"
        payload = {
            "name": "morpheus",
            "job": "leader"
        }

        response = requests.post(url, json=payload)
        # Проверяем статус до работы с телом
        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        # Парсим JSON только после успешной проверки статуса
        body = response.json()

        assert body["name"] == payload["name"]
        assert body["job"] == payload["job"]
        assert "id" in body
        assert "createdAt" in body
