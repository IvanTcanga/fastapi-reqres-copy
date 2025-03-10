import requests
import pytest


class TestUserData:
    def test_user_data(self):
        url = "http://127.0.0.1:8000/api/users/1"
        id = 1
        email = "janet.weaver@reqres.in"

        response = requests.get(url)
        body = response.json()
        data = body["data"]

        assert response.status_code == 200
        assert data["id"] == id
        assert data["email"] == email

    def test_create_user(self):
        url = "http://127.0.0.1:8000/api/users"
        payload = {
            "name": "morpheus",
            "job": "leader"
        }

        response = requests.post(url, json=payload)
        body = response.json()

        assert response.status_code == 201
        assert body["name"] == payload["name"]
        assert body["job"] == payload["job"]
        assert "id" in body
        assert "createdAt" in body


if __name__ == '__main__':
    test_reqres_copy = TestUserData()
    test_reqres_copy.test_user_data()
    test_reqres_copy.test_create_user()
