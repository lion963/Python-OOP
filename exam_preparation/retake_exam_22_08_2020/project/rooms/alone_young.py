from exam_preparation.retake_exam_22_08_2020.project.rooms.room import Room
from exam_preparation.retake_exam_22_08_2020.project.appliances.tv import TV


class AloneYoung(Room):

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, budget=salary, members_count=1)
        self.room_cost = 10
        self.appliances = [TV()]
        self.expenses = self.calculate_expenses(self.appliances)
