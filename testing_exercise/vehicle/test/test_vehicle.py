from testing_exercise.vehicle.project.vehicle import Vehicle
import unittest


class VehicleTests(unittest.TestCase):

    def setUp(self):
        self.vehicle = Vehicle(65.25, 125.58)

    def test_fuel(self):
        result = self.vehicle.fuel
        expected_result = 65.25
        self.assertEqual(result, expected_result)

    def test_fuel_type(self):
        result = type(self.vehicle.fuel)
        expected_result = float
        self.assertEqual(result, expected_result)

    def test_capacity(self):
        result = self.vehicle.capacity
        expected_result = 65.25
        self.assertEqual(result, expected_result)

    def test_capacity_type(self):
        result = type(self.vehicle.capacity)
        expected_result = float
        self.assertEqual(result, expected_result)

    def test_horse_power(self):
        result = self.vehicle.horse_power
        expected_result = 125.58
        self.assertEqual(result, expected_result)

    def test_horse_power_type(self):
        result = type(self.vehicle.horse_power)
        expected_result = float
        self.assertEqual(result, expected_result)

    def test_fuel_consamption(self):
        result = self.vehicle.fuel_consumption
        expected_result = 1.25
        self.assertEqual(result, expected_result)

    def test_fuel_consamption_type(self):
        result = type(self.vehicle.fuel_consumption)
        expected_result = float
        self.assertEqual(result, expected_result)

    def test_DEFAULT_FUEL_CONSUMPTION(self):
        result = Vehicle.DEFAULT_FUEL_CONSUMPTION
        expected_result = 1.25
        self.assertEqual(result, expected_result)

    def test_DEFAULT_FUEL_CONSUMPTION_type(self):
        result = type(Vehicle.DEFAULT_FUEL_CONSUMPTION)
        expected_result = float
        self.assertEqual(result, expected_result)

    def test_drive_method_raise(self):
        with self.assertRaises(Exception):
            self.vehicle.drive(100)

    def test_drive_method(self):
        self.vehicle.drive(50)
        result = self.vehicle.fuel
        expected_result = 2.75
        self.assertEqual(result, expected_result)

    def test_refuel_method_raise(self):
        with self.assertRaises(Exception):
            self.vehicle.refuel(10.0)

    def test_refuel_method(self):
        self.vehicle.drive(50)
        self.vehicle.refuel(50.0)
        result = self.vehicle.fuel
        expected_result = 52.75
        self.assertEqual(result, expected_result)

    def test__str__method(self):
        result = str(self.vehicle)
        expected_result = 'The vehicle has 125.58 horse power with 65.25 fuel left and 1.25 fuel consumption'
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
