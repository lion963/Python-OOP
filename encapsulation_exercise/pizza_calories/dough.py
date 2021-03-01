class Dough:

    def __init__(self, flour_type, baking_technique, weight):
        self.__flour_type = flour_type
        self.__baking_technique = baking_technique
        self.__weight = weight

    def get_flour_type(self):
        return self.__flour_type

    def set_flour_type(self, flour_type):
        self.__flour_type = flour_type

    def get_baking_technique(self):
        return self.__baking_technique

    def set_baking_technique(self, baking_technique):
        self.__baking_technique = baking_technique

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight
