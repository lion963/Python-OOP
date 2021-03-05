from inheritance_exercise.restaurant.food.main_dish import MainDish

class Salmon(MainDish):
    __GRAMS = 22

    def __init__(self, name, price):
        super().__init__(name, price, Salmon.__GRAMS)

    @property
    def GRAMS(self):
        return self.__GRAMS

