class Cup():
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, liquid):
        if liquid <= self.status():
            self.quantity += liquid

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())
