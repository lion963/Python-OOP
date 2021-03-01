class Toppings:

    def __init__(self, topping_type, weight):
        self.__topping_type = topping_type
        self.__weight = weight

    def get_topping_type(self):
        return self.__topping_type

    def get_weight(self):
        return self.__weight

    def set_topping_type(self, topping_type):
        self.__topping_type = topping_type

    def set_weight(self, weight):
        self.__weight = weight
