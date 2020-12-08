import ParkingSpot
# Vehicle Classes

class Vehicle:
    size = 0
    parking_spot = 0  # need to reference the spot this vehicle is in
    parked_flag = 0  # 0 is not parked  1 is parked

    # Initiate Vehicle
    def __init__(self):
        pass

    # get size of Vehicle
    def get_size_of_vehicle(self):
        return self.size

    # print for debugging
    def print_vehicle(self):
        switcher = {
            1: "Motorcycle",
            2: "Compact Car",       # dictionary as switch statement for sizes
            3: "Bus"
        }
        print(switcher.get(self.size))

    # is the car parked? return true if yes
    def is_parked(self):
        if self.parked_flag == 1:
            return True
        else:
            return False

    # park vehicle
    def park_vehicle(self, parking_spot):
        if self.parked_flag == 0:
            if parking_spot.store_vehicle_in_spot(self):
                self.parking_spot = parking_spot
                self.parked_flag = 1
        else:
            print("this vehicle is parked already")

    # get size of vehicle
    def get_parking_spot(self):
        return self.parking_spot


# Motorcycle class - can park in any spot
class Motorcycle(Vehicle):
    size = 1  # size of motorcycle


# Motorcycle class - can park in any spot
class Compact(Vehicle):
    size = 2  # size of motorcycle


# bus class - can park in 5 consecutive LARGE spots - gonna be different
class Bus(Vehicle):
    size = 3

    # park vehicle
    def park_vehicle(self, parking_garage):
        if self.parked_flag == 0:
            if parking_garage.store_bus_in_spots(self):
                self.parking_spot = parking_garage
                self.parked_flag = 1
        else:
            print("this vehicle is parked already")


