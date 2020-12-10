import ParkingGarage


# parking Spot class
class ParkingSpot:

    # A parking spot can be motorcycle -1, compact - 2, or large -3
    def __init__(self, size_of_spot):
        self.size_of_spot = size_of_spot
        self.occupied = 0
        self.vehicle = 0
        pass

    # print statement to debug easier
    def print_parking_spot(self):
        if self.occupied == 1:
            print(self.vehicle.print_vehicle(), end=' ')
            return self.vehicle.print_vehicle()
        else:
            print(str(self.size_of_spot), end=' ')
            return self.size_of_spot

    # I want to store a vehicle here in my parking spot
    def store_vehicle_in_spot(self, vehicle):
        if not self.is_occupied():
            if vehicle.get_size_of_vehicle() <= self.size_of_spot:
                self.set_occupied(True)
                self.set_vehicle(vehicle)
                return True
            else:
                return False
        else:
            return False

    # need to know if spot is occupied
    def is_occupied(self):
        if self.occupied == 1:
            return True
        elif self.occupied == 0:
            return False

    # set occupied flag
    def set_occupied(self, boolean):
        if boolean:
            self.occupied = 1
        else:
            self.occupied = 0

    # set occupied flag
    def set_vehicle(self, vehicle):
        self.vehicle = vehicle

    # get size of spot
    def get_size_of_spot(self):
        return self.size_of_spot

    # get vehicle in spot
    def get_vehicle_in_spot(self):
        return self.vehicle
