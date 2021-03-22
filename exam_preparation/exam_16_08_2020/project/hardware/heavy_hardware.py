from exam_preparation.exam_16_08_2020.project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    type = "Heavy"


    def __init__(self, name, capacity, memory):
        super().__init__(name, type=HeavyHardware.type, capacity=capacity * 2, memory=memory * 0.75)
