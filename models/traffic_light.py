class TrafficLight:
    def __init__(self, location: str):
        self.location = location
        self.state = "RED"  # RED, GREEN, YELLOW

    def change_state(self, new_state: str):
        if new_state in ["RED", "GREEN", "YELLOW"]:
            self.state = new_state
