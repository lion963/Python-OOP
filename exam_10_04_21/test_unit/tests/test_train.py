from unittest import TestCase, main

from exam_10_04_21.test_unit.project.train.train import Train


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train('Express', 2)

    def test_attributes(self):
        self.assertEqual("Express", self.train.name)
        self.assertEqual(2, self.train.capacity)
        self.assertListEqual([], self.train.passengers)

    def test_add_method_not_enough_capacity(self):
        self.train.add("Asen")
        self.train.add("Katerina")
        with self.assertRaises(ValueError) as contex:
            self.train.add("Him")
        self.assertIsNotNone(contex)
        self.assertEqual("Train is full", str(contex.exception))

    def test_add_method_if_passenger_exists(self):
        self.train.add("Asen")
        with self.assertRaises(ValueError) as contex:
            self.train.add("Asen")
        self.assertIsNotNone(contex)
        self.assertEqual("Passenger Asen Exists", str(contex.exception))

    def test_add_method_passenger_added(self):
        actual = self.train.add("Asen")
        expected = "Added passenger Asen"
        self.assertEqual(expected, actual)

    def test_remove_method_passenger_not_in_passengers(self):
        self.train.add("Asen")
        with self.assertRaises(ValueError) as contex:
            self.train.remove("Him")
        self.assertIsNotNone(contex)
        self.assertEqual("Passenger Not Found", str(contex.exception))

    def test_remove_method_passenger_removed(self):
        self.train.add("Asen")
        actual = self.train.remove("Asen")
        expected = "Removed Asen"
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
