class ValueError(Exception):
    pass


class Pizza:

    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_dough(self):
        return self.__dough

    def set_dough(self, dough):
        self.__dough = dough

    def get_toppings_capacity(self):
        return self.__toppings_capacity

    def set_toppings_capacity(self, toppings_capacity):
        self.__toppings_capacity = toppings_capacity

    def get_toppings(self):
        return self.__toppings
    @property
    def toppings(self):
        return self.__toppings

    def set_toppings(self, toppings):
        self.__toppings = toppings

    def add_topping(self, topping):
        if len(self.__toppings) < self.__toppings_capacity:
            if topping.get_topping_type() not in self.__toppings:
                self.__toppings[topping.get_topping_type()] = 0
            self.__toppings[topping.get_topping_type()] += topping.get_weight()
            return
        raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        return sum([value for value in self.get_toppings().values()])
# + self.__dough.get_weight()
