from inheritance_exercise.restaurant.beverage.hot_beverege import HotBeverage

class Tea(HotBeverage):

    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)