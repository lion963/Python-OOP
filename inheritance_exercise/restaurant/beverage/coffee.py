from inheritance_exercise.restaurant.beverage.hot_beverege import HotBeverage

class Coffee(HotBeverage):
    __MILLILITERS = 50
    __PRICE = 3.50

    def __init__(self, name, price, milliliters, caffeine: float):
        super().__init__(name, price, milliliters)
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