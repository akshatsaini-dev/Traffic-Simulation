from models.sensor import Sensor
from models.traffic_light import TrafficLight

def test_sensor_returns_density():
    sensor = Sensor("S1")
    density = sensor.detect_traffic_density()
    assert isinstance(density, int)
    assert 0 <= density <= 20

def test_traffic_light_changes():
    light = TrafficLight("L1")
    light.change_state("GREEN")
    assert light.state == "GREEN"

    light.change_state("YELLOW")
    assert light.state == "YELLOW"

    light.change_state("INVALID")  # shouldn't change
    assert light.state == "YELLOW"
