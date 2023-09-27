# tests/test_functional_main.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_contact():
    fake_contact = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone_number": "123456789",
        "birthday": "1990-01-01",
        "additional_data": "Some additional data"
    }
    response = client.post("/contacts/", json=fake_contact)
    assert response.status_code == 201

def test_read_contact():
    response = client.get("/contacts/1")
    assert response.status_code == 200

def test_update_contact():
    updated_data = {
        "first_name": "UpdatedName",
        "last_name": "UpdatedLastName"
    }
    response = client.put("/contacts/1", json=updated_data)
    assert response.status_code == 200

def test_get_contacts():
    response = client.get("/contacts/")
    assert response.status_code == 200

def test_delete_contact():
    response = client.delete("/contacts/1")
    assert response.status_code == 204
    response = client.get("/contacts/1")
    assert response.status_code == 404

def test_get_upcoming_birthdays():
    response = client.get("/upcoming_birthdays/")
    assert response.status_code == 200

def test_user_registration():
    fake_user = {
        "email": "newuser@example.com",
        "password": "newuserpassword"
    }
    response = client.post("/register/", json=fake_user)
    assert response.status_code == 201

def test_user_authentication():
    credentials = {
        "username": "newuser@example.com",
        "password": "newuserpassword"
    }
    response = client.post("/login/token/", data=credentials)
    assert response.status_code == 200
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/me/", headers=headers)
    assert response.status_code == 200

def test_update_user_profile():
    new_profile_data = {
        "full_name": "Updated User",
        "avatar_url": "https://example.com/avatar.jpg"
    }
    token = "your_auth_token_here"
    headers = {"Authorization": f"Bearer {token}"}
    response = client.put("/users/me/", headers=headers, json=new_profile_data)
    assert response.status_code == 200
