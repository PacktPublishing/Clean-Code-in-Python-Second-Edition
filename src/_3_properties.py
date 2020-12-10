import redis


class PlayerStatus:

    def __init__(self):
        self.redis_connection = redis.StrictRedis()
        self.key = "score_1"

    def accumulate_points(self, new_points):
        current_score = int(self.redis_connection.get(self.key) or 0)
        score = current_score + new_points
        self.redis_connection.set(self.key, score)

    @property
    def points(self):
        return int(self.redis_connection.get(self.key) or 0)

    @points.setter
    def points(self, new_points):
        self.redis_connection.set(self.key, new_points)

"""
player_status = PlayerStatus()
player_status.accumulate_points(20)
player_status.points += 20
player_status.points = 20
print(player_status.points)
"""
