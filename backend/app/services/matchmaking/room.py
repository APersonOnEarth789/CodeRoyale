from app.core.redis import r
from .store import cleanup_player_metadata
import uuid, json

def create_room(player1_metadata, player2_metadata):
    room_id = str(uuid.uuid4())
    room_data = {
        "room_id": room_id,
        "players": [player1_metadata, player2_metadata],
        "status": "active"
    }
    room_key = f"matchmaking:room:{room_id}"

    with r.pipeline() as pipe:
        pipe.set(room_key, json.dumps(room_data), ex=1800)
        cleanup_player_metadata([player1_metadata["player_id"], player2_metadata["player_id"]], pipe=pipe)
        pipe.execute()
