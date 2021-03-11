class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return (f"{self.name} has saved {self.money} money.")


import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Asen', 3000, 100)

    def test_name(self):
        result = self.worker.name
        expected_result = 'Asen'
        self.assertEqual(result, expected_result)

    def test_salary(self):
        result = self.worker.salary
        expected_result = 3000
        self.assertEqual(result, expected_result)

    def test_energy(self):
        result = self.worker.energy
        expected_result = 100
        self.assertEqual(result, expected_result)

    def test_energy_after_rest_method_call(self):
        self.worker.rest()
        result = self.worker.energy
        expected_result = 100 + 1
        self.assertEqual(result, expected_result)

    def test_work_method_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_work_method_negative_energy(self):
        self.worker.energy = -1
        with self.assertRaises(Exception):
            self.worker.work()

    def test_money_after_work_method_call(self):
        self.worker.work()
        result = self.worker.money
        expected_result = 3000
        self.assertEqual(result, expected_result)

    def test_energy_after_work_method_call(self):
        self.worker.work()
        result = self.worker.energy
        expected_result = 100 - 1
        self.assertEqual(result, expected_result)

    def test_get_info_method(self):
        result = self.worker.get_info()
        expected_result = "Asen has saved 0 money."
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
