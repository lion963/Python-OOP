from exam_preparation.retake_exam_22_08_2020.project.rooms.room import Room
from exam_preparation.retake_exam_22_08_2020.project.appliances.tv import TV
from exam_preparation.retake_exam_22_08_2020.project.appliances.fridge import Fridge
from exam_preparation.retake_exam_22_08_2020.project.appliances.laptop import Laptop


class YoungCouple(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, budget=salary_one + salary_two, members_count=2)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.expenses = self.calculate_expenses(self.appliances)
