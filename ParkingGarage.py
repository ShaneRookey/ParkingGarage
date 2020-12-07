import ParkingSpot
import random


# a parking garage class
class ParkingGarage:
    parking_garage = []  # initialize the parking garage
    rows_of_spots = []
    spot_array = []

    def __init__(self, levels, rows, spots_per_row):
        self.levels = levels
        self.rows = rows
        self.spots_per_row = spots_per_row

        # create rows
        for row in range(rows):
            self.spot_array.clear()
            self.create_spot_array(spots_per_row)
            self.rows_of_spots.append(self.spot_array)

        # create levels
        for level in range(levels):
            self.parking_garage.append(self.rows_of_spots)
        pass

    def print_parking_garage(self):
        level_counter = 1
        for levels in self.parking_garage:
            print("level " + str(level_counter))
            print(self.parking_garage[level_counter-1])
            level_counter += 1

    def create_spot_array(self, spots_per_row):
        # create spots
        for spots in range(spots_per_row):
            spot = ParkingSpot.ParkingSpot(random.randint(1, 3))
            self.spot_array.append(spot)  # generate random sized spots from 1-3 in rows

    def store_bus_in_spots(self, bus):
        large_spot_counter = 1
        for s in self.spot_array:
            if not self.spot_array[s].is_occupied() and (self.spot_array[s].get_size_of_spot() == 3):
                large_spot_counter += 1
                if large_spot_counter == 5:
                    bus.park_vehicle(self.spot_array[s])
                    self.spot_array[s] = bus.set_occupied(True)
                    self.spot_array[s+1] = bus.set_occupied(True)
                    self.spot_array[s+2] = bus.set_occupied(True)
                    self.spot_array[s+3] = bus.set_occupied(True)
                    self.spot_array[s+4] = bus.set_occupied(True)
                    self.spot_array[s].vehicle = bus.set_occupied(True)
                    self.spot_array[s + 1].vehicle = bus.set_occupied(True)
                    self.spot_array[s + 2].vehicle = bus.set_occupied(True)
                    self.spot_array[s + 3].vehicle = bus.set_occupied(True)
                    self.spot_array[s + 4].vehicle = bus.set_occupied(True)

        pass