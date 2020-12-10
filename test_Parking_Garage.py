import unittest
import ParkingGarage


class test_parking_garage(unittest.TestCase):

    def test_create_spot_array(self):
        number_of_levels = 5
        number_of_rows = 5
        number_of_spots_per_row = 5
        total_spots = number_of_levels*number_of_rows*number_of_levels
        parking_garage1 = ParkingGarage.ParkingGarage(number_of_levels, number_of_rows, number_of_spots_per_row)
        parking_garage2 = ParkingGarage.ParkingGarage(number_of_levels, number_of_rows, number_of_spots_per_row)

        self.assertEqual(len(parking_garage1.spot_array), total_spots)
        self.assertNotEqual(parking_garage2, parking_garage1)

    def test_store_bus_in_spots(self):

        pass

