from exam_preparation.retake_exam_22_08_2020.project.appliances.appliance import Appliance


class Laptop(Appliance):
    COST = 1

    def __init__(self):
        super().__init__(cost=Laptop.COST)
