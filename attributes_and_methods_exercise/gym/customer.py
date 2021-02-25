class Customer:
    __id = 0

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        type(self).__id += 1
        self.id = Customer.__id

    @staticmethod
    def get_next_id(self):
        return self.id + 1

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
