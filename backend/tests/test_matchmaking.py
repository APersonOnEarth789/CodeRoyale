from tests.utils import signup_user, login_user, queue_user

# Test valid user joins queue successfully
def test_join_queue_first_player(client):
    signup_user(client)
    token = login_user(client)[1]["access_token"]
    join_response, join_json = queue_user(client, token)
    assert join_response.status_code == 200
    assert join_json["status"] == "queued"

# Test two valid users matched successfully
def test_players_matched(client):
    id1 = signup_user(client)[1]["id"]
    token1 = login_user(client)[1]["access_token"]
    queue_user(client, token1)

    id2 = signup_user(client, username="TestUser2")[1]["id"]
    token2 = login_user(client, username="TestUser2")[1]["access_token"]
    join_response, join_json = queue_user(client, token2)

    assert join_response.status_code == 200
    assert join_json["status"] == "matched"
    assert join_json["player1_id"] == id1
    assert join_json["player2_id"] == id2
