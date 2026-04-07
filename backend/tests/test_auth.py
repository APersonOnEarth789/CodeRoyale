from tests.utils import signup_user, login_user, assert_validation_error

# Test new user signup
def test_signup_success(client):
    signup_response = signup_user(client)
    assert signup_response.status_code == 200
    signup_json = signup_response.get_json()
    assert signup_json["username"] == "TestUser"
    assert "hashed_password" not in signup_json # Ensure password isn't exposed

# Test existing user signup
def test_signup_duplicate(client):
    signup_user(client)
    signup_response = signup_user(client)
    assert signup_response.status_code == 400
    assert "already registered" in signup_response.text

# Test signup with username too short
def test_signup_username_too_short(client):
    signup_response = signup_user(client, username="a")
    assert_validation_error(signup_response)
    assert "at least 2 characters" in signup_response.text

# Test signup with username too long
def test_signup_username_too_long(client):
    signup_response = signup_user(client, username="a"*129)
    assert_validation_error(signup_response)
    assert "at most 128 characters" in signup_response.text

# Test signup with password too short
def test_signup_password_too_short(client):
    signup_response = signup_user(client, password="a")
    assert_validation_error(signup_response)
    assert "at least 8 characters" in signup_response.text

# Test signup with password too long
def test_signup_password_too_long(client):
    signup_response = signup_user(client, password="a"*257)
    assert_validation_error(signup_response)
    assert "at most 256 characters" in signup_response.text

# Test correct credentials login
def test_login_success(client):
    signup_user(client)
    login_response = login_user(client)
    assert login_response.status_code == 200
    login_json = login_response.get_json()
    assert "access_token" in login_json # Ensure token is returned
    assert login_json["token_type"] == "bearer"

# Test wrong username login
def test_login_with_wrong_username(client):
    signup_user(client)
    login_response = login_user(client, username="Lemon")
    assert login_response.status_code == 401
    assert "Incorrect username or password" in login_response.text

# Test wrong password login
def test_login_with_wrong_password(client):
    signup_user(client)
    login_response = login_user(client, password="Lime12345")
    assert login_response.status_code == 401
    assert "Incorrect username or password" in login_response.text
