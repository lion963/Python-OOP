from inheritance_exercise.restaurant.food.dessert import Dessert

class Cake(Dessert):
    __GRAMS = 250
    __CALORIES = 1000
    __PRICE = 5

    def __init__(self, name):
        super().__init__(name, Cake.__PRICE, Cake.__GRAMS, Cake.__CALORIES)

    @property
    def GRAMS(self):
        return self.__GRAMS

    @property
    def CALORIES(self):
        return self.__CALORIES

    @property
    def PRICE(self):
        return self.__PRICE

