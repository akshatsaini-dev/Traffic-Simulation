from models.vehicle import Car, Bus, Bike
from controllers.traffic_controller import TrafficController
from utils.logger import Logger

if __name__ == "__main__":
    controller = TrafficController("Intersection-1")

    # Create some vehicles
    car = Car("C1")
    bus = Bus("B1")
    bike = Bike("BK1")

    Logger.log(car.honk())
    Logger.log(bus.honk())
    Logger.log(bike.honk())

    # Simulate traffic control
    for _ in range(5):
        state = controller.manage_traffic()
        Logger.log(f"Traffic Light at {controller.intersection} is {state}")
