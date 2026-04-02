from app.core.redis import r

def push_to_queue(player_id: int):
    r.lpush("matchmaking_queue", player_id)
