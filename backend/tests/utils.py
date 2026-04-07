def signup_user(client, username="TestUser", password="Password123"):
    signup_data = {
        "username": username,
        "password": password
    }
    return client.post("/auth/signup", json=signup_data)

def login_user(client, username="TestUser", password="Password123"):
    login_data = {
        "username": username,
        "password": password
    }
    return client.post("/auth/token", json=login_data)

def assert_validation_error(response):
    assert response.status_code == 400
    json_data = response.get_json()
    assert "validation_error" in json_data
