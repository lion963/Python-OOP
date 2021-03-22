from exam_preparation.exam_16_08_2020.project.hardware.hardware import Hardware


class HeavyHardware(Hardware):

    def __init__(self, name, capacity, memory):
        super().__init__(name, "Heavy", capacity=int(capacity * 2), memory=int(memory * 0.75))
