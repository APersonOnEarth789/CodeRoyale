from .queue import push_to_queue
from .store import set_player_metadata, get_player_metadata
from .room import create_room
from app.services.users.models import User

def add_to_queue(player_id: int):
    response = push_to_queue(player_id)
    if response["status"] == "matched":
        player1_metadata = get_player_metadata(response["player1_id"])
        player2_metadata = get_player_metadata(response["player2_id"])
        create_room(player1_metadata, player2_metadata)
    return response # Forward result

def store_player_metadata(player: User):
    set_player_metadata(player)
