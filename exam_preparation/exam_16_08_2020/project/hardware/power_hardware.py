from exam_preparation.exam_16_08_2020.project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    type = "Power"

    def __init__(self, name, capacity, memory):
        super().__init__(name, type=PowerHardware.type, capacity=capacity * 0.25, memory=memory * 1.75)
