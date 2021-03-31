from exam_preparation.exam_19_12_2020.tests.project.factory.factory import Factory


# class PaintFactory(Factory):
#     def __init__(self, name: str, capacity: int):
#         super().__init__(name, capacity)
#         self.valid_ingredients = ["white", "yellow", "blue", "green", "red"]
#
#     def add_ingredient(self, ingredient_type: str, quantity: int):
#
#         if ingredient_type not in self.valid_ingredients:
#             raise TypeError(f"Ingredient of type {ingredient_type} not allowed in PaintFactory")
#         elif self.capacity < quantity:
#             raise ValueError("Not enough space in factory")
#         elif ingredient_type not in self.ingredients.keys():
#             self.ingredients[ingredient_type] = 0
#
#         self.ingredients[ingredient_type] += quantity
#
#     def remove_ingredient(self, ingredient_type: str, quantity: int):
#         if ingredient_type not in self.ingredients.keys():
#             raise KeyError("No such product in the factory")
#         elif quantity > self.ingredients[ingredient_type]:
#             raise ValueError("Ingredient quantity cannot be less than zero")
#
#         self.ingredients[ingredient_type] -= quantity
#
#     @property
#     def products(self):
#         return self.ingredients

class PaintFactory(Factory):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def add_ingredient(self, product_type, product_quantity):
        if product_type in ["white", "yellow", "blue", "green", "red"]:
            if self.can_add(product_quantity):
                if product_type not in self.ingredients:
                    self.ingredients[product_type] = 0
                self.ingredients[product_type] += product_quantity
            else:
                raise ValueError("Not enough space in factory")
        else:
            raise TypeError(f"Ingredient of type {product_type} not allowed in {self.__class__.__name__}")

    def remove_ingredient(self, product_type, product_quantity):
        if product_type in self.ingredients:
            if self.ingredients[product_type] - product_quantity >= 0:
                self.ingredients[product_type] -= product_quantity
            else:
                raise ValueError("Ingredients quantity cannot be less than zero")
        else:
            raise KeyError("No such ingredient in the factory")

    @property
    def products(self):
        return self.ingredients
