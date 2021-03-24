from exam_preparation.exam_10_04.project.medicine.medicine import Medicine


class Painkiller(Medicine):
    def __init__(self):
        super().__init__(health_increase=20)
