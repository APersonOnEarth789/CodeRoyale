from tests.utils import signup_user, login_user, queue_user
from redis.exceptions import WatchError

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

    # Check queue is cleared (users removed)
    from app.core.redis import r
    assert r.zcard("matchmaking:queue") == 0

# Test valid user joins queue twice
def test_queue_twice(client):
    signup_user(client)
    token1 = login_user(client)[1]["access_token"]
    queue_user(client, token1)
    join_response, join_json = queue_user(client, token1)
    assert join_response.status_code == 409
    assert join_json["status"] == "already_queued"

# Test return value from failed retries
def test_retries_fail(monkeypatch):
    from app.services.matchmaking.queue import push_to_queue

    def always_fail(*args, **kwargs):
        raise WatchError()
    monkeypatch.setattr("redis.client.Pipeline.execute", always_fail)

    result = push_to_queue(1)
    assert result["status"] == "retry_failed"

# Test sequence of three queue joins
def test_queue_flow(client):
    signup_user(client)
    token1 = login_user(client)[1]["access_token"]
    join_json1 = queue_user(client, token1)[1]
    assert join_json1["status"] == "queued"

    signup_user(client, username="TestUser2")
    token2 = login_user(client, username="TestUser2")[1]["access_token"]
    join_json2 = queue_user(client, token2)[1]
    assert join_json2["status"] == "matched"

    signup_user(client, username="TestUser3")
    token3 = login_user(client, username="TestUser3")[1]["access_token"]
    join_json3 = queue_user(client, token3)[1]
    assert join_json3["status"] == "queued"

# Test authorisation layer works
def test_route_requires_auth(client):
    res = client.post("/matchmaking/join_queue")
    assert res.status_code == 401

def test_queue_invalid_token(client):
    headers = {"Authorization": "Bearer invalidtoken"}
    res = client.post("/matchmaking/join_queue", headers=headers)
    assert res.status_code in {401, 422}
