class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


import unittest


class TestCar(unittest.TestCase):
    def __get_exception_from_init(self, make, model, fuel_consumption, fuel_capacity):
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)
        return context.exception

    def test_carInit_whenValidValues_shouldInitializeIt(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        car = Car(make, model, fuel_consumption, fuel_capacity)

        expected = [make, model, fuel_consumption, fuel_capacity, 0]
        actual = [car.make, car.model, car.fuel_consumption, car.fuel_capacity, car.fuel_amount]

        self.assertListEqual(expected, actual)

    def test_carInit_whenNoneMake_shouldRaise(self):
        make = None
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenEmptyStringMake_shouldRaise(self):
        make = ''
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenNoneModel_shouldRaise(self):
        make = 'test make'
        model = None
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenEmptyStringModel_shouldRaise(self):
        make = 'test make'
        model = ''
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenNegativeFuelConsumption_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = -6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenZeroFuelConsumption_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 0
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenNegativeFuelCapacity_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = -60

        params = [make, model, fuel_consumption, fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenZeroFuelCapacity_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 0

        params = [make, model, fuel_consumption, fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenNegativeFuelAmount_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)

        with self.assertRaises(Exception) as context:
            car.fuel_amount = -1

        self.assertIsNotNone(context.exception)

    def testCarRefuel_whenNegativeFuel_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)

        with self.assertRaises(Exception) as context:
            car.refuel(-1)

        self.assertIsNotNone(context.exception)

    def testCarRefuel_whenZeroFuel_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)

        with self.assertRaises(Exception) as context:
            car.refuel(0)

        self.assertIsNotNone(context.exception)

    def testCarRefuel_whenPositiveFuelAndEnoughInCapacity_shouldIcreaseAmount(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)

        car.refuel(5)
        self.assertEqual(5, car.fuel_amount)

    def testCarRefuel_whenPositiveFuelAndMoreThenCapacity_shouldSetAmountToCapacity(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)

        car.refuel(car.fuel_capacity * 2)
        self.assertEqual(fuel_capacity, car.fuel_amount)

    def test_carDrive_whenEnoughFuel_shouldDecreaseFuel(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)

        car.refuel(car.fuel_capacity)

        distance = 100
        car.drive(distance)
        expected = car.fuel_capacity - (distance / 100 * car.fuel_consumption)
        actual = car.fuel_amount

        self.assertEqual(expected, actual)

    def test_carDrive_whenNotEnoughFuel_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)

        with self.assertRaises(Exception) as context:
            car.drive(100)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()