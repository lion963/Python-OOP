class Child:
    MONTH=30

    def __init__(self, food_cost: int, *toys_cost):
        self.cost: float = (food_cost + sum(toys_cost))*Child.MONTH
