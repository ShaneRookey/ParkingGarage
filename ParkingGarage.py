import ParkingSpot
import random


# a parking garage class
class ParkingGarage:
    spot_array = []
    total_spots = 0

    def __init__(self, levels, rows, spots_per_row):
        self.levels = levels
        self.rows = rows
        self.spots_per_row = spots_per_row
        self.total_spots = spots_per_row*rows*levels

        self.create_spot_array(self.spots_per_row)

        pass

    # print each spot
    # new line for each row
    # two new lines for levels
    def print_parking_garage(self):
        for spots in range(self.total_spots):
            if (spots % self.spots_per_row == 0) and (spots != 0):
                print()
                if spots == self.spots_per_row*self.rows:
                    print()
                    print(self.spot_array[spots].get_size_of_spot(), end=' ')
                else:
                    print(self.spot_array[spots].get_size_of_spot(), end=' ')
            else:
                print(self.spot_array[spots].get_size_of_spot(), end=' ')
        pass

    def create_spot_array(self, spots_per_row):
        random_spot_gen = [1, 2, 3]
        random_array = random.choices(random_spot_gen, weights=[1, 5, 10], k=self.total_spots)
        # create spots
        for spots in range(self.total_spots):
            spot = ParkingSpot.ParkingSpot(random_array[spots])  # generate random sized spots from 1-3 in rows
            self.spot_array.append(spot)

    def store_bus_in_spots(self, bus):
        large_spots = 0
        for spot in range(self.total_spots):
            if not self.spot_array[spot].is_occupied() and (self.spot_array[spot].get_size_of_spot() == 3):  #check that spot is not occupied or too small
                large_spots += 1
                if large_spots == 5:
                    self.spot_array[spot].occupied = 1  # occupy spot
                    self.spot_array[spot - 1].occupied = 1
                    self.spot_array[spot - 2].occupied = 1
                    self.spot_array[spot - 3].occupied = 1
                    self.spot_array[spot - 4].occupied = 1
                    self.spot_array[spot].vehicle = bus
                    self.spot_array[spot - 1].vehicle = bus  # set the vehicle that is parked in the spot
                    self.spot_array[spot - 2].vehicle = bus
                    self.spot_array[spot - 3].vehicle = bus  # set the vehicle that is parked in the spot
                    self.spot_array[spot - 4].vehicle = bus
                    print("\n\nbus is parked")
                    return True
            else:
                print("\n\nNot enough room for the bus")
                return False
