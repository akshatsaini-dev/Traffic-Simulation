from models.traffic_light import TrafficLight
from models.sensor import Sensor

class TrafficController:
    def __init__(self, intersection: str):
        self.intersection = intersection
        self.light = TrafficLight(intersection)
        self.sensor = Sensor(intersection)

    def manage_traffic(self):
        density = self.sensor.detect_traffic_density()
        if density > 10:
            self.light.change_state("GREEN")
        elif 5 < density <= 10:
            self.light.change_state("YELLOW")
        else:
            self.light.change_state("RED")
        return self.light.state
