
# Vehicle Classes
class Vehicle:

    # Initiate Vehicle
    def __init__(self):
        self.parking_spot = 0
        self.parked_flag = 0
        pass

    # print for debugging
    def print_vehicle(self):
        size_switcher = {
            1: "M",
            2: "C",       # dictionary as switch statement for sizes
            3: "B"
        }
        return size_switcher.get(self.size)

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
                return True
            else:
                return False
        else:
            print("this vehicle is parked already")
            return False

    # get size of vehicle
    def get_parking_spot(self):
        return self.parking_spot

    # get size of Vehicle
    def get_size_of_vehicle(self):
        return self.size


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
                return True
            else:
                return False
        else:
            print("this vehicle is parked already")
            return False

    # get size of vehicle
    def get_parking_spot(self):
        return self.parking_spot
