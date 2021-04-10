from exam_10_04_21.project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    size_fresh = 3
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.size_fresh, price)

    def eat(self):
        self.size += 3

