from flask import Blueprint
from flask_jwt_extended import jwt_required
from flask_pydantic import validate
from app.services.auth.dependencies import get_current_user
from .service import add_to_queue, store_player_metadata

matchmaking_bp = Blueprint("matchmaking", __name__, url_prefix="/matchmaking")

@matchmaking_bp.route("/join_queue", methods=["POST"])
@jwt_required()
@validate()
def join_queue():
    user = get_current_user()
    store_player_metadata(user)
    result = add_to_queue(user.id)
    if result["status"] in {"already_queued", "retry_failed"}:
        return (result, 409)
    return (result, 200)
