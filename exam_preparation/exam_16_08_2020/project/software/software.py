class Software:

    def __init__(self, name, type, capacity_consumption, memory_consumption):
        self.name = name
        self.type = type
        self.capacity_consumption = capacity_consumption
        self.memory_consumption = memory_consumption


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if not (value == "Express" or  value=="Light"):
            raise Exception('Type must be "Express" or "Light"')
        self.__type = value
