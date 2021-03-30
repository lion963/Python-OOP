from exam_preparation.exam_19_12_2020.project.supply.supply import Supply


class WaterSupply(Supply):
    def __init__(self):
        super().__init__(needs_increase=40)
