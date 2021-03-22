from exam_preparation.exam_16_08_2020.project.hardware.hardware import Hardware


class HeavyHardware(Hardware):

    def __init__(self, name, capacity, memory):
        super().__init__(name, "Heavy", capacity=capacity * 2, memory=memory * 0.75)
