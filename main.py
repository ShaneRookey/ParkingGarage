import Vehicles
import ParkingSpot
import ParkingGarage


# Main
def main():
    #test_vehicle_creations()
    #test_create_parking_spot()
    #test_store_vehicle()
    #test_park_vehicle()
    #test_building_parking_garage()
    #test_parking_a_vehicle_in_garage()
    #test_bus_storage()


    pass


# TESTING METHODS #########################################

# test vehicle creations
def test_vehicle_creations():
    motorcycle1 = Vehicles.Motorcycle()  # build motorcycle
    motorcycle1.print_vehicle()


# test creating a parking spot
def test_create_parking_spot():
    parking_spot1 = ParkingSpot.ParkingSpot(1)
    parking_spot2 = ParkingSpot.ParkingSpot(2)
    parking_spot3 = ParkingSpot.ParkingSpot(3)
    parking_spot1.print_parking_spot()
    parking_spot2.print_parking_spot()
    parking_spot3.print_parking_spot()


# testing storing vehicle within parking spot class
def test_store_vehicle():
    motorcycle1 = Vehicles.Motorcycle()
    parking1 = ParkingSpot.ParkingSpot(1)
    parking1.store_vehicle_in_spot(motorcycle1)
    parking1.print_parking_spot()


# testing parking the vehicle - specifically motorcycles in the vehicle class
def test_park_vehicle():
    # motorcycle and motorcycle spot creation
    motorcycle1 = Vehicles.Motorcycle()
    parking1 = ParkingSpot.ParkingSpot(1)
    motorcycle1.park_vehicle(parking1)  # park motorcycle 1 in parking spot 1

    #  car creation
    car1 = Vehicles.Compact()
    parking2 = ParkingSpot.ParkingSpot(2)
    car1.park_vehicle(parking2)  # park car in parking spot 2
    car1.park_vehicle(parking1)  # shoudl not be able to park here because its occupied

    parking1.print_parking_spot()
    parking2.print_parking_spot()


def test_building_parking_garage():
    number_of_levels = 2
    number_of_rows = 1
    number_of_spots = 5
    parking_garage1 = ParkingGarage.ParkingGarage(number_of_levels, number_of_rows, number_of_spots)
    parking_garage1.print_parking_garage()
    pass


def test_parking_a_vehicle_in_garage():
    number_of_levels = 2
    number_of_rows = 2
    number_of_spots = 5
    parking_garage1 = ParkingGarage.ParkingGarage(number_of_levels, number_of_rows, number_of_spots)
    motorcycle1 = Vehicles.Motorcycle()
    spot = parking_garage1.parking_garage[0][0][0]
    motorcycle1.park_vehicle(spot)
    print("// printing parking garage")
    parking_garage1.print_parking_garage()

    print("// printing vehicle at parking spot ")
    spot.print_parking_spot()

    print("// printing motorcycle parking spot")
    print(motorcycle1.get_parking_spot())


def test_bus_storage():
    number_of_levels = 5
    number_of_rows = 5
    number_of_spots = 10
    parking_garage1 = ParkingGarage.ParkingGarage(number_of_levels, number_of_rows, number_of_spots)

    spot = parking_garage1.parking_garage[0][0][0]
    bus1 = Vehicles.Bus()
    bus1.park_vehicle(spot)
    parking_garage1.print_parking_garage()
    print("// printing vehicle at parking spot ")
    spot.print_parking_spot()
    pass



main()
