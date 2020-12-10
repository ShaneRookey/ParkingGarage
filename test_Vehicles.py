import unittest
import Vehicles
import ParkingSpot


class test_Vehicles(unittest.TestCase):

    def test_get_size_of_vehicle(self):
        motorcycle = Vehicles.Motorcycle()
        car = Vehicles.Compact()
        bus = Vehicles.Bus()
        self.assertEqual(motorcycle.get_size_of_vehicle(), 1)
        self.assertEqual(car.get_size_of_vehicle(), 2)
        self.assertEqual(bus.get_size_of_vehicle(), 3)

    def test_print_vehicle(self):
        motorcycle = Vehicles.Motorcycle()
        car = Vehicles.Compact()
        bus = Vehicles.Bus()
        self.assertEqual(motorcycle.print_vehicle(), 'M')
        self.assertEqual(car.print_vehicle(), 'C')
        self.assertEqual(bus.print_vehicle(), 'B')

    def test_is_parked(self):
        motorcycle = Vehicles.Motorcycle()
        car = Vehicles.Compact()
        parking1 = ParkingSpot.ParkingSpot(1)
        motorcycle.park_vehicle(parking1)
        car.park_vehicle(parking1)  # shouldn't be able to park in same spot
        self.assertTrue(motorcycle.is_parked())
        self.assertFalse(car.is_parked())

    def test_park_vehicle(self):
        motorcycle = Vehicles.Motorcycle()
        car = Vehicles.Compact()
        parking1 = ParkingSpot.ParkingSpot(1)
        parking2 = ParkingSpot.ParkingSpot(1)
        parking3 = ParkingSpot.ParkingSpot(2)
        self.assertTrue(motorcycle.park_vehicle(parking1))
        self.assertFalse(car.park_vehicle(parking1))
        self.assertFalse(car.park_vehicle(parking2))
        self.assertTrue(car.park_vehicle(parking3))
        pass

    def test_get_parking_spot(self):
        motorcycle = Vehicles.Motorcycle()
        car = Vehicles.Compact()
        parking1 = ParkingSpot.ParkingSpot(1)
        parking2 = ParkingSpot.ParkingSpot(1)
        parking3 = ParkingSpot.ParkingSpot(2)
        motorcycle.park_vehicle(parking1)
        car.park_vehicle(parking1)
        car.park_vehicle(parking3)
        self.assertEqual(motorcycle.get_parking_spot(), parking1)
        self.assertEqual(car.get_parking_spot(), parking3)
        pass


