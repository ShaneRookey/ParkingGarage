import Vehicles
import ParkingSpot
import ParkingGarage


# Main
def main():
    #test_vehicles()
    #test_parking_spot()
    #test_park_vehicle()
    #test_building_parking_garage()
    #test_parking_a_vehicle_in_garage()
    test_bus_storage()


    pass


# TESTING METHODS #########################################

# test vehicle creations create one of each vehicle and test methods within Vehicle
def test_vehicles():
    # create the vehicles
    motorcycle1 = Vehicles.Motorcycle()
    compact_car1 = Vehicles.Compact()
    bus1 = Vehicles.Bus()

    # print size of vehicles motorcycle = 1, car = 2, bus = 3
    print(motorcycle1.get_size_of_vehicle())
    print(compact_car1.get_size_of_vehicle())
    print(bus1.get_size_of_vehicle())


    #print statement for vehicles
    motorcycle1.print_vehicle()
    compact_car1.print_vehicle()
    bus1.print_vehicle()

    # check if vehicles are parked should be false right now
    print(motorcycle1.is_parked())
    print(compact_car1.is_parked())
    print(bus1.is_parked())

    pass


# testing some parking spot method  and creations
def test_parking_spot():
    # creating 3 different size spots to test
    parking_spot1 = ParkingSpot.ParkingSpot(1)
    parking_spot2 = ParkingSpot.ParkingSpot(2)
    parking_spot3 = ParkingSpot.ParkingSpot(3)

    # printing size of spot
    print(parking_spot1.get_size_of_spot())
    print(parking_spot2.get_size_of_spot())
    print(parking_spot3.get_size_of_spot())


    # printing size of spot
    parking_spot1.print_parking_spot()
    parking_spot2.print_parking_spot()
    parking_spot3.print_parking_spot()

    pass


# testing storing vehicle within parking spot class
def test_park_vehicle():
    # creating 3 different size spots to test
    parking_spot1 = ParkingSpot.ParkingSpot(1)
    parking_spot2 = ParkingSpot.ParkingSpot(2)
    parking_spot3 = ParkingSpot.ParkingSpot(3)

    # creating 3 different Vehicles spots to test
    motorcycle1 = Vehicles.Motorcycle()
    compact_car1 = Vehicles.Compact()

    motorcycle1.park_vehicle(parking_spot1)
    parking_spot1.print_parking_spot()   # should be occupied by a motorcycle

    compact_car1.park_vehicle(parking_spot1)  # should be occupied by motorcycle so cannot park and does not fit
    compact_car1.park_vehicle(parking_spot2)  # try parking in the second spot
    parking_spot2.print_parking_spot()  # should be occupied by a compact car

    compact_car1.park_vehicle(parking_spot2) # this vehicle should already be parked
    pass


    # test building and printing a parking garage
def test_building_parking_garage():
    number_of_levels = 2
    number_of_rows = 2
    number_of_spots_per_row = 10

    parking_garage1 = ParkingGarage.ParkingGarage(number_of_levels, number_of_rows, number_of_spots_per_row)
    parking_garage1.print_parking_garage()
    pass


def test_parking_a_vehicle_in_garage():
    number_of_levels = 2
    number_of_rows = 2
    number_of_spots_per_row = 10

    parking_garage1 = ParkingGarage.ParkingGarage(number_of_levels, number_of_rows, number_of_spots_per_row)
    motorcycle1 = Vehicles.Motorcycle()
    compact_car1 = Vehicles.Compact()

    motorcycle1.park_vehicle(parking_garage1.spot_array[0])
    compact_car1.park_vehicle(parking_garage1.spot_array[1])
    print()
    print()
    parking_garage1.print_parking_garage()  # should print garage with first spot taken

    pass


def test_bus_storage():
    number_of_levels = 5
    number_of_rows = 6
    number_of_spots_per_row = 15

    parking_garage1 = ParkingGarage.ParkingGarage(number_of_levels, number_of_rows, number_of_spots_per_row)
    bus1 = Vehicles.Bus()
    bus2 = Vehicles.Bus()
    bus3 = Vehicles.Bus()
    bus4 = Vehicles.Bus()
    bus5 = Vehicles.Bus()
    bus6 = Vehicles.Bus()
    motorcycle1 = Vehicles.Motorcycle()
    compact_car1 = Vehicles.Compact()
    parking_garage1.print_parking_garage()  # print before parking the bus

    # loop to see if bus fits anywhere in garage
    bus1.park_vehicle(parking_garage1)  # busses try to park anywhere
    bus2.park_vehicle(parking_garage1)
    bus3.park_vehicle(parking_garage1)  # busses try to park anywhere
    bus4.park_vehicle(parking_garage1)
    bus5.park_vehicle(parking_garage1)  # busses try to park anywhere
    bus6.park_vehicle(parking_garage1)
    motorcycle1.park_vehicle(parking_garage1.spot_array[8])
    compact_car1.park_vehicle(parking_garage1.spot_array[2])
    parking_garage1.print_parking_garage()  # if bus is sucessful to park we should see 5 X in a row

    pass



main()
