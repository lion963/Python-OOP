class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):

    def setUp(self):
        self.cat = Cat('Kitty')

    def test_size_increase_after_method_eat_call(self):
        self.cat.eat()
        result = self.cat.size
        expected_result = 1
        self.assertEqual(result, expected_result)

    def test_cat_is_fed_after_method_eat_call(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_eat_method_raise_error(self):
        self.cat.fed = True
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_sleep_method_raise_error(self):
        self.cat.fed = False
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_sleepy_after_method_eat_call(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()
