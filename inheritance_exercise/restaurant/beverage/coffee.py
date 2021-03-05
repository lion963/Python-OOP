from inheritance_exercise.restaurant.beverage.hot_beverege import HotBeverage

class Coffee(HotBeverage):
    __MILLILITERS = 50
    __PRICE = 3.50

    def __init__(self, name, caffeine):
        super().__init__(name, Coffee.__PRICE, Coffee.__MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

    @property
    def MILLILITERS(self):
        return self.__MILLILITERS

    @property
    def PRICE(self):
        return self.__PRICE


