from exam_preparation.exam_16_08_2020.project.software.software import Software


class ExpressSoftware(Software):
    type = "Express"

    def __init__(self, name, capacity_consumption, memory):
        super().__init__(name, type=ExpressSoftware.type, capacity_consumption=capacity_consumption, memory_consumption=memory * 2)
