from exam_preparation.retake_exam_22_08_2020.project.rooms.room import Room
from exam_preparation.retake_exam_22_08_2020.project.people.child import Child
from exam_preparation.retake_exam_22_08_2020.project.appliances.fridge import Fridge
from exam_preparation.retake_exam_22_08_2020.project.appliances.laptop import Laptop
from exam_preparation.retake_exam_22_08_2020.project.appliances.stove import Stove
from exam_preparation.retake_exam_22_08_2020.project.appliances.tv import TV

import unittest


class RoomTests(unittest.TestCase):

    def test_attributes(self):
        params = ['Kamboshevi', 350.0, 2]
        room = Room(*params)
        result = [room.family_name, room.budget, room.members_count, room.children, room.expenses]
        expected_result = ['Kamboshevi', 350.0, 2, [], 0]
        self.assertListEqual(result, expected_result)

    def test_get_property(self):
        params = ['Kamboshevi', 350.0, 2]
        room = Room(*params)
        result = room.expenses
        expected_result = 0
        self.assertEqual(result, expected_result)

    def test_set_property_positive(self):
        params = ['Kamboshevi', 350.0, 2]
        room = Room(*params)
        room.expenses = 25.25
        result = room.expenses
        expected_result = 25.25
        self.assertEqual(result, expected_result)

    def test_set_property_negative(self):
        params = ['Kamboshevi', 350.0, 2]
        room = Room(*params)
        with self.assertRaises(ValueError):
            room.expenses = -1

    def test_calculate_expenses_method_positive(self):
        params = ['Kamboshevi', 350.0, 2]
        room = Room(*params)
        appliances = [TV(), Fridge(), Laptop(), Stove()]
        child1 = Child(3, 2, 3, 4)
        child2 = Child(2, 1, 3)
        children = [child1, child2]
        result = room.calculate_expenses(appliances, children)
        expected_result = 672
        self.assertEqual(result, expected_result)

    def test_calculate_expenses_method_negative(self):
        params = ['Kamboshevi', 350.0, 2]
        room = Room(*params)
        appliances = [TV(), Fridge(), Laptop(), Stove()]
        child1 = Child(-30, 2, 3, 4)
        child2 = Child(-20, 1, 3)
        children = [child1, child2]
        with self.assertRaises(ValueError):
            room.calculate_expenses(appliances, children)


if __name__ == '__main__':
    unittest.main()
