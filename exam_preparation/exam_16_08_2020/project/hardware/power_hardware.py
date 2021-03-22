from exam_preparation.exam_16_08_2020.project.hardware.hardware import Hardware


class PowerHardware(Hardware):

    def __init__(self, name, capacity, memory):
        super().__init__(name, "Power", int(capacity * 0.25), int(memory * 1.75))
