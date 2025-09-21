class Vehicle:
    def __init__(self, vehicle_id: str, speed: int = 0):
        self.vehicle_id = vehicle_id
        self.speed = speed

    def accelerate(self, amount: int):
        self.speed += amount

    def brake(self, amount: int):
        self.speed = max(0, self.speed - amount)


class Car(Vehicle):
    def honk(self):
        return f"Car {self.vehicle_id} says Beep Beep!"


class Bus(Vehicle):
    def honk(self):
        return f"Bus {self.vehicle_id} says Honk Honk!"


class Bike(Vehicle):
    def honk(self):
        return f"Bike {self.vehicle_id} says Ring Ring!"
