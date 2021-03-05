from inheritance_exercise.restaurant.food.main_dish import MainDish

class Salmon(MainDish):
    __GRAMS = 22

    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)

    @property
    def GRAMS(self):
        return self.__GRAMS