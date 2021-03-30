class Survivor:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.health: int = 100
        self.needs: int = 100

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name not valid!")
        self.__name = value

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age not valid!")

    @property
    def health(self):
        return self.health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Health not valid!")
        if self.health + value > 100:
            self.health = 100
        else:
            self.health = value

    @property
    def needs(self):
        return self.needs

    @needs.setter
    def needs(self, value):
        if value < 0:
            raise ValueError("Needs not valid!")
        if self.needs + value > 100:
            self.needs = 100
        else:
            self.needs = value

    @property
    def needs_sustenance(self):
        return self.needs < 100

    @property
    def needs_healing(self):
        return self.health < 100
