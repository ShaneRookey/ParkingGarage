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
        if self.occupied == 1:
            return 'X'
        else:
            return self.size_of_spot

    # print statement to debug easier
    def print_parking_spot(self):
        if self.occupied == 1:
            print("occupied by ")
            print(self.vehicle)
        else:
            print(str(self.size_of_spot))

    # I want to store a vehicle here in my parking spot
    def store_vehicle_in_spot(self, vehicle):
        if not self.is_occupied():  # if the spot is open
            if vehicle.get_size_of_vehicle() <= self.size_of_spot:  # if the vehicle is smaller or equal to size of spot, it can park
                self.occupied = 1  # occupy spot
                self.vehicle = vehicle  # set the vehicle that is parked in the spot
                return True
            else:
                print("does not fit!")  # vehicle does not fit
                return False
        else:
            print("occupied!")  #  If spot is taken
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
