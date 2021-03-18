from exam_preparation.retake_exam_22_08_2020.project.appliances.appliance import Appliance


class Stove(Appliance):
    COST = 0.7

    def __init__(self):
        super().__init__(cost=Stove.COST)
