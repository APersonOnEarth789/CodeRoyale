import pytest

def test_signup(client):
    # Test new user signup
    signup_data = {
        "username": "Lemon",
        "password": "Lime123"
    }
    signup_response = client.post("/auth/signup", json=signup_data)
    assert signup_response.status_code == 200
    signup_json = signup_response.get_json()
    assert signup_json["username"] == "Lemon"
    assert "hashed_password" not in signup_json # Ensure password isn't exposed

    # Test existing user signup
    duplicate_response = client.post("/auth/signup", json=signup_data)
    assert duplicate_response.status_code == 400
    assert "Username is already registered" in duplicate_response.text
