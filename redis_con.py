import redis
import json

class RedisData:
    def __init__(self):
        self.r = redis.Redis(host="localhost", port=6379, decode_responses=True)

    def set_data(self, key, data): 
        self.r.set(key, json.dumps(data)) 

    def setex_set_data(self, key, data):
        self.r.setex(key, 43200, json.dumps(data))
 
    def get_data(self, key):
        data = self.r.get(key)
        if data:
            return json.loads(data)
        return []

