import pytest
from models.vehicle import Car, Bus, Bike

def test_car_acceleration():
    car = Car("C1")
    car.accelerate(20)
    assert car.speed == 20

def test_car_braking():
    car = Car("C2", 30)
    car.brake(10)
    assert car.speed == 20
    car.brake(50)  # shouldn't go negative
    assert car.speed == 0

def test_vehicle_honks():
    car = Car("C1")
    bus = Bus("B1")
    bike = Bike("BK1")

    assert "Beep" in car.honk()
    assert "Honk" in bus.honk()
    assert "Ring" in bike.honk()
