import unittest
import ParkingSpot
import Vehicles
import ParkingGarage


class test_Parking_Spots(unittest.TestCase):

    def test_print_parking_spot(self):
        parking1 = ParkingSpot.ParkingSpot(1)
        parking2 = ParkingSpot.ParkingSpot(3)
        motorcycle = Vehicles.Motorcycle()
        motorcycle.park_vehicle(parking1)

        self.assertEqual('M', parking1.print_parking_spot())
        self.assertEqual(3, parking2.print_parking_spot())

    def test_store_vehicle_in_spot(self):
        parking1 = ParkingSpot.ParkingSpot(1)
        parking2 = ParkingSpot.ParkingSpot(1)
        parking3 = ParkingSpot.ParkingSpot(3)
        parking4 = ParkingSpot.ParkingSpot(3)
        parking5 = ParkingSpot.ParkingSpot(2)
        motorcycle = Vehicles.Motorcycle()
        car1 = Vehicles.Compact()
        car2 = Vehicles.Compact()
        bus1 = Vehicles.Bus()
        bus2 = Vehicles.Bus()

        self.assertTrue(parking1.store_vehicle_in_spot(motorcycle))
        self.assertFalse(parking2.store_vehicle_in_spot(car1))
        self.assertTrue(parking3.store_vehicle_in_spot(car1))
        self.assertFalse(parking3.store_vehicle_in_spot(car2))
        self.assertTrue(parking4.store_vehicle_in_spot(bus1))
        self.assertFalse(parking5.store_vehicle_in_spot(bus1))
        self.assertFalse(parking4.store_vehicle_in_spot(bus2))

    def test_is_occupied(self):
        parking1 = ParkingSpot.ParkingSpot(1)
        parking2 = ParkingSpot.ParkingSpot(2)
        motorcycle = Vehicles.Motorcycle()
        parking1.store_vehicle_in_spot(motorcycle)
        self.assertTrue(parking1.is_occupied())
        self.assertFalse(parking2.is_occupied())

    def test_set_occupied(self):
        parking1 = ParkingSpot.ParkingSpot(1)
        parking1.set_occupied(True)
        self.assertTrue(parking1.is_occupied())
        parking1.set_occupied(False)
        self.assertFalse(parking1.is_occupied())

    def test_get_vehicle_in_spot(self):
        parking1 = ParkingSpot.ParkingSpot(1)
        parking2 = ParkingSpot.ParkingSpot(1)
        motorcycle = Vehicles.Motorcycle()
        car1 = Vehicles.Compact()
        parking1.store_vehicle_in_spot(motorcycle)
        parking2.store_vehicle_in_spot(car1)
        self.assertEqual(parking1.get_vehicle_in_spot(), motorcycle)
        self.assertFalse(parking2.get_vehicle_in_spot())

    def test_set_vehicle(self):
        parking1 = ParkingSpot.ParkingSpot(1)
        motorcycle = Vehicles.Motorcycle()
        parking1.set_vehicle(motorcycle)
        self.assertEqual(motorcycle, parking1.get_vehicle_in_spot())

    def test_get_size_of_spot(self):
        parking1 = ParkingSpot.ParkingSpot(1)
        parking2 = ParkingSpot.ParkingSpot(2)
        parking3 = ParkingSpot.ParkingSpot(3)
        self.assertEqual(parking1.get_size_of_spot(), 1)
        self.assertEqual(parking2.get_size_of_spot(), 2)
        self.assertEqual(parking3.get_size_of_spot(), 3)
        self.assertNotEqual(parking1.get_size_of_spot(), parking2.get_size_of_spot())
