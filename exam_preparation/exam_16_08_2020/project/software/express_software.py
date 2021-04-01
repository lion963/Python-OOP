from exam_preparation.exam_16_08_2020.project.software.software import Software


class ExpressSoftware(Software):
    type = "Express"

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, "Express", int(capacity_consumption), int(memory_consumption * 2))
