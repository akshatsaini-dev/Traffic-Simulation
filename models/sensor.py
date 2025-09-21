import random

class Sensor:
    def __init__(self, location: str):
        self.location = location

    def detect_traffic_density(self):
        # Random value simulating cars per minute
        return random.randint(0, 20)
