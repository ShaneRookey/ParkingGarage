# Vehicle Classes

class Vehicle:
    size = 0
    can_park_in_spot = 0
    parking_spot = 0  # need to reference the spot this vehicle is in
    is_parked = 0  # 0 is not parked  1 is parked

    # Initiate Vehicle
    def __init__(self):
        pass

    # get size of Vehicle
    def get_size_of_vehicle(self):
        return self.size

    # set size of Vehicle
    def set_size_of_vehicle(self, size_of_car):
        self.size = size_of_car
        pass

    # print for debugging
    def print_vehicle(self):
        print(self)

    # park vehicle
    def park_vehicle(self, parking_spot):
        parking_spot.store_vehicle_in_spot(self)
        self.parking_spot = parking_spot
        self.is_parked = 1

    # get size of vehicle
    def get_parking_spot(self):
        return self.parking_spot

    # is the car parked? return true if yes
    def is_parked(self):
        if self.is_parked == 1:
            return True
        else:
            return False


# Motorcycle class - can park in any spot
class Motorcycle(Vehicle):
    size = 1  # size of motorcycle
    can_park_in_spot = 1  # size that it can fit in


# Motorcycle class - can park in any spot
class Compact(Vehicle):
    size = 2  # size of motorcycle
    can_park_in_spot = 2  # size that it can fit in


# bus class - can park in 5 consecutive LARGE spots - gonna be different
class Bus(Vehicle):
    size = 3

