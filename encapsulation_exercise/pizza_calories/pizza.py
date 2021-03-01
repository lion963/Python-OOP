class ValueError(Exception):
    pass


class Pizza:

    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_dough(self):
        return self.__dough

    def set_dough(self, dough):
        self.__dough = dough

    def get_toppings_capacity(self):
        return self.__toppings_capacity

    def set_toppings_capacity(self, toppings_capacity):
        self.__toppings_capacity = toppings_capacity

    def get_toppings(self):
        return self.__toppings

    def set_toppings(self, toppings):
        self.__toppings = toppings

    def add_topping(self, topping):
        if len(self.__toppings) < self.__toppings_capacity:
            if topping.topping_type not in self.__toppings:
                self.__toppings[topping.topping_type] = 0
            self.__toppings[topping.topping_type] += topping.weight
            return
        raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        return sum([value for value in self.__toppings.values()]) + self.__dough.weight

import unittest

from encapsulation_exercise.pizza_calories.dough import Dough
from encapsulation_exercise.pizza_calories.topping import Topping


class Tests(unittest.TestCase):
    def test_topping_init(self):
        t = Topping("Tomato", 20)
        self.assertEqual(t._Topping__topping_type, "Tomato")
        self.assertEqual(t._Topping__weight, 20)

    def test_dough_init(self):
        d = Dough("Sugar", "Mixing", 20)
        self.assertEqual(d._Dough__flour_type, "Sugar")
        self.assertEqual(d._Dough__baking_technique, "Mixing")
        self.assertEqual(d._Dough__weight, 20)

    def test_pizza_init(self):
        d = Dough("Sugar", "Mixing", 20)
        p = Pizza("Burger", d, 5)

        self.assertEqual(p._Pizza__name, "Burger")
        self.assertEqual(p._Pizza__dough, d)
        self.assertEqual(len(p._Pizza__toppings), 0)
        self.assertEqual(p._Pizza__toppings_capacity, 5)

    def test_pizza_add_topping_error(self):
        d = Dough("Sugar", "Mixing", 20)
        t = Topping("Tomato", 20)
        p = Pizza("Burger", d, 0)
        with self.assertRaises(ValueError) as ctx:
            p.add_topping(t)
        self.assertEqual("Not enough space for another topping", str(ctx.exception))

    def test_pizza_add_topping_new(self):
        d = Dough("Sugar", "Mixing", 20)
        t = Topping("Tomato", 20)
        p = Pizza("Burger", d, 200)
        p.add_topping(t)

        self.assertEqual(p.toppings["Tomato"], 20)
        self.assertEqual(len(p.toppings), 1)

    def test_pizza_add_topping_update(self):
        d = Dough("Sugar", "Mixing", 20)
        t = Topping("Tomato", 20)
        p = Pizza("Burger", d, 200)
        p.add_topping(t)
        p.add_topping(t)

        self.assertEqual(p.toppings["Tomato"], 40)

    def test_pizza_calculate_total_weight(self):
        d = Dough("Sugar", "Mixing", 20)
        t = Topping("Tomato", 20)
        p = Pizza("Burger", d, 200)
        p.add_topping(t)
        p.add_topping(t)

        self.assertEqual(p.calculate_total_weight(), 40)


if __name__ == '__main__':
    unittest.main()

