import ParkingGarage


# parking Spot class
class ParkingSpot:
    occupied = 0  # 0 is empty - 1 is full
    vehicle = 0  # want to store a vehicle

    # A parking spot can be motorcycle -1, compact - 2, or large -3
    def __init__(self, size_of_spot):
        self.size_of_spot = size_of_spot
        pass

    # get size of spot
    def get_size_of_spot(self):
        return self.size_of_spot

    # get size of spot
    def set_size_of_spot(self, size):
        self.size_of_spot = size
    pass

    # print statement to debug easier
    def print_parking_spot(self):
        if self.occupied == 1:
            print("occupied by ")
            print(self.vehicle)
        else:
            print("size of spot is " + str(self.size_of_spot))

    # I want to store a vehicle here in my parking spot
    def store_vehicle_in_spot(self, vehicle):
        if not self.is_occupied():
            if vehicle.get_size_of_vehicle == 3:  # if bus use different method within parking garage
                ParkingGarage.store_bus_in_spots(vehicle)
            else:  # if not a bus- vehicle can park normally
                if vehicle.get_size_of_vehicle() <= self.size_of_spot:
                    self.occupied = 1  # occupy spot
                    self.vehicle = vehicle
                else:
                    print("does not fit!")
        else:
            print("occupied!")

    # need to know if spot is occupied
    def is_occupied(self):
        if self.occupied == 1:
            return True
        elif self.occupied == 0:
            return False

    def set_occupied(self, boolean):
        if boolean:
            self.occupied = 1
        else:
            self.occupied = 0