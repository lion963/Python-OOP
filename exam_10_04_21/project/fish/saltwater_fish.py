from exam_10_04_21.project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    size_salt = 5
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.size_salt, price)

    def eat(self):
        self.size += 2

