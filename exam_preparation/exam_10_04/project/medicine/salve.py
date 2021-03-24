from exam_preparation.exam_10_04.project.medicine.medicine import Medicine


class Salve(Medicine):
    def __init__(self):
        super().__init__(health_increase=50)
