class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < 10:
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < 15:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = [customer for customer in self.customers if customer.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        if customer.age >= dvd.age_restriction:
            if not dvd in customer.rented_dvds:
                if not dvd.is_rented:
                    dvd.is_rented = True
                    customer.rented_dvds.append(dvd)
                    return f"{customer.name} has successfully rented {dvd.name}"
                return f"DVD is already rented"
            return f"{customer.name} has already rented {dvd.name}"
        return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

    def return_dvd(self, customer_id, dvd_id):
        customer = [customer for customer in self.customers if customer.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += f"{customer.__repr__()}\n"
        for dvd in self.dvds:
            result += f"{dvd.__repr__()}\n"
        return result
