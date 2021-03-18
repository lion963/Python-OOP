from exam_preparation.retake_exam_22_08_2020.project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum([room.room_cost + room.expenses for room in self.rooms])
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []

        for room in self.rooms:
            if room.budget >= room.expenses:
                total_expenses = room.expenses + room.room_cost
                room.budget -= total_expenses
                result += [f'{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.']
            else:
                result += [f'{room.family_name} does not have enough budget and must leave the hotel.']
                self.rooms.remove(room)
        return '\n'.join(result)


    def status(self):
        total_people = sum([room.members_count for room in self.rooms])
        result = [f"Total population: {total_people}"]
        for room in self.rooms:
            result +=[f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$"]
            if room.children:
                result += [f"--- Child {i+1} monthly cost: {room.children[i].cost:.2f}$" for i in range(len(room.children))]
            appliances_cost = sum([app.get_monthly_expense() for app in room.appliances])
            result += [f"--- Appliances monthly cost: {appliances_cost:.2f}$"]
        return '\n'.join(result)
