from exam_preparation.exam_16_08_2020.project.software.software import Software


class UnsuccessfulInstallException(Exception):
    pass


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        if self.capacity < sum(
                [s.capacity_consumption for s in self.software_components]) + software.capacity_consumption \
                or self.memory < sum([s.memory_consumption for s in self.software_components]) + software.memory_consumption:
            raise UnsuccessfulInstallException('Software cannot be installed')

        self.software_components.append(software)

    def uninstall(self, software: Software):
        # if software in self.software_components:
        self.software_components.remove(software)

