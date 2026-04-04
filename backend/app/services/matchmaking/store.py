from app.core.redis import r
from app.services.users.models import User
import time

def set_player_metadata(player: User):
    key = f"matchmaking:player:{player.id}"
    player_metadata = {
        "player_id": player.id,
        "display_name": player.username,
        "joined_at": int(time.time_ns())
        # "skill_rating": player.rating,
        # "region": player.region
    }
    r.hset(key, mapping=player_metadata)
    r.expire(key, 300) # 5 minutes

def get_player_metadata(player_id: int):
    key = f"matchmaking:player:{player_id}"
    return r.hgetall(key)

def cleanup_player_metadata(player_ids: list[int], pipe):
    keys = [f"matchmaking:player:{player_id}" for player_id in player_ids]
    pipe.delete(*keys)
