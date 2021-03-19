from exam_preparation.retake_exam_22_08_2020.project.appliances.appliance import Appliance
from exam_preparation.retake_exam_22_08_2020.project.people.child import Child

class Room:

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name: str = name
        self.budget: float = budget
        self.members_count: int = members_count
        self.children: list = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError('Expenses cannot be negative')
        self.__expenses = value

    def calculate_expenses(self, *args):
        total_expenses = 0
        for list_obj in args:
            for obj in list_obj:
                if isinstance(obj, Appliance):
                    total_expenses += obj.get_monthly_expense()
                elif isinstance(obj, Child):
                    total_expenses += obj.cost*30
        self.expenses = total_expenses
        return self.expenses
