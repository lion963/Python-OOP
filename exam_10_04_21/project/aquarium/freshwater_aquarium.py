from exam_10_04_21.project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    def __init__(self, name: str):
        super().__init__(name, capacity=50)



