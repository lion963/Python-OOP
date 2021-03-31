from exam_preparation.exam_19_12_2020.tests.project.factory.paint_factory import PaintFactory
from unittest import TestCase, main

class TestPaintFactory(TestCase):

    def setUp(self):
        self.paint_factory = PaintFactory('Slatina', 50)

    def test_initial_atributtes(self):
        result = [self.paint_factory.name, self.paint_factory.capacity, self.paint_factory.valid_ingredients, self.paint_factory.ingredients]
        expected = ['Slatina', 50, ["white", "yellow", "blue", "green", "red"], {}]

    def test_add_method_invalid_ingredient(self):
        with self.assertRaises(TypeError) as context:
            self.paint_factory.add_ingredient('orange', 20)
        self.assertEqual("Ingredient of type orange not allowed in PaintFactory", str(context.exception))

    def test_add_method_invalid_quantity(self):
        with self.assertRaises(ValueError) as context:
            self.paint_factory.add_ingredient('green', 55)
        self.assertEqual("Not enough space in factory", str(context.exception))

    def test_add_method_valid_ingredient_and_quantity(self):
        self.paint_factory.add_ingredient('green', 25)
        self.assertEqual({'green': 25}, self.paint_factory.ingredients)

    def test_remove_method_invalid_ingredient(self):
        with self.assertRaises(KeyError) as context:
            self.paint_factory.remove_ingredient('orange', 20)
        self.assertEqual("No such product in the factory", context.exception.args[0])

    def test_remove_method_invalid_quantity(self):
        self.paint_factory.add_ingredient('green', 25)
        with self.assertRaises(ValueError) as context:
            self.paint_factory.remove_ingredient('green', 30)
        self.assertEqual("Ingredient quantity cannot be less than zero", str(context.exception))

    def test_remove_method_valid_ingredient_and_quantity(self):
        self.paint_factory.add_ingredient('green', 25)
        self.paint_factory.remove_ingredient('green', 25)
        self.assertEqual({'green': 0}, self.paint_factory.ingredients)

    def test_products_property(self):
        self.paint_factory.add_ingredient('green', 25)
        self.paint_factory.add_ingredient('white', 25)
        self.assertEqual({'green': 25, 'white': 25}, self.paint_factory.ingredients)

    def test_can_add_method_from_base_class(self):
        self.paint_factory.add_ingredient('green', 20)
        self.paint_factory.add_ingredient('white', 20)
        self.assertTrue(self.paint_factory.can_add(10))


if __name__ == '__main__':
    main()