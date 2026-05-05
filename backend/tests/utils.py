def signup_user(client, username="TestUser", password="Password123"):
    signup_data = {
        "username": username,
        "password": password
    }
    response = client.post("/auth/signup", json=signup_data)
    return response, response.get_json()

def login_user(client, username="TestUser", password="Password123"):
    login_data = {
        "username": username,
        "password": password
    }
    response = client.post("/auth/token", json=login_data)
    return response, response.get_json()

def assert_validation_error(response):
    assert response.status_code == 400
    json_data = response.get_json()
    assert "validation_error" in json_data

def queue_user(client, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/matchmaking/join_queue", headers=headers)
    return response, response.get_json()
