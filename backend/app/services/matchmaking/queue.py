from app.core.redis import r
from redis.exceptions import WatchError
import time

def push_to_queue(player_id: int):
    queue_key = "matchmaking:queue"

    with r.pipeline() as pipe:
        for _ in range(5): # Try enqueue up to 5 times
            try:             
                pipe.watch(queue_key)

                # Queue size before adding new player
                queue_size = pipe.zcard(queue_key) 

                # Start transaction
                pipe.multi()
                if queue_size >= 1: # Form match if someone already waiting
                    pipe.zrange(queue_key, 0, 0)
                    pipe.zremrangebyrank(queue_key, 0, 0)
                else:
                    pipe.zadd(queue_key, {player_id: int(time.time_ns())}) # Sort by join time
                results = pipe.execute() # Execute all queued commands

                # If match made results will include ZRANGE response
                if queue_size >= 1:
                    waiting_player_id = int(results[0][0])
                    return {
                        "status": "matched",
                        "player1_id": waiting_player_id,
                        "player2_id": player_id
                    }
                else:
                    return {"status": "queued"}
            except WatchError:
                # Queue was modified, retry
                continue
        
        return {"status": "error"} # All 5 tries failed
