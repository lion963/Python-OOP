from encapsulation_exercise.wild_cat_zoo.caretaker import Caretaker
from encapsulation_exercise.wild_cat_zoo.cheetah import Cheetah
from encapsulation_exercise.wild_cat_zoo.keeper import Keeper
from encapsulation_exercise.wild_cat_zoo.lion import Lion
from encapsulation_exercise.wild_cat_zoo.tiger import Tiger
from encapsulation_exercise.wild_cat_zoo.vet import Vet


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price:
            if len(self.animals) < self.__animal_capacity:
                self.animals.append(animal)
                self.__budget-=price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return f"Not enough space for animal"
        return f"Not enough budget"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        amount = 0
        for worker in self.workers:
            amount += worker.salary
        if self.__budget >= amount:
            self.__budget -= amount
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        amount=0
        for animal in self.animals:
            amount += animal.get_needs()
        if self.__budget >= amount:
            self.__budget -= amount
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = ''
        result += f"You have {len(self.animals)} animals\n"
        lions = [animal for animal in self.animals if animal.__class__.__name__ == "Lion"]
        result += f"----- {len(lions)} Lions:\n"
        if lions:
            for lion in lions:
                result += f"Name: {lion.name}, Age: {lion.age}, Gender: {lion.gender}\n"
        tigers = [animal for animal in self.animals if animal.__class__.__name__ == 'Tiger']
        result += f"----- {len(tigers)} Tigers:\n"
        if tigers:
            for tiger in tigers:
                result += f"Name: {tiger.name}, Age: {tiger.age}, Gender: {tiger.gender}\n"
        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == 'Cheetah']
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        if cheetahs:
            for cheetah in cheetahs[:-1]:
                result += f"Name: {cheetah.name}, Age: {cheetah.age}, Gender: {cheetah.gender}\n"
            for cheetah in cheetahs[-1:]:
                result += f"Name: {cheetah.name}, Age: {cheetah.age}, Gender: {cheetah.gender}"
        return result

    def workers_status(self):
        result = ''
        result += f"You have {len(self.workers)} workers\n"
        keepers = [worker for worker in self.workers if worker.__class__.__name__ == 'Keeper']
        result += f"----- {len(keepers)} Keepers:\n"
        if keepers:
            for keeper in keepers:
                result += f"Name: {keeper.name}, Age: {keeper.age}, Salary: {keeper.salary}\n"
        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == 'Caretaker']
        result += f"----- {len(caretakers)} Caretakers:\n"
        if caretakers:
            for caretaker in caretakers:
                result += f"Name: {caretaker.name}, Age: {caretaker.age}, Salary: {caretaker.salary}\n"
        vets = [worker for worker in self.workers if worker.__class__.__name__ == 'Vet']
        result += f"----- {len(vets)} Vets:\n"
        if vets:
            for vet in vets[:-1]:
                result += f"Name: {vet.name}, Age: {vet.age}, Salary: {vet.salary}\n"
            for vet in vets[-1:]:
                result += f"Name: {vet.name}, Age: {vet.age}, Salary: {vet.salary}"
        return result


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
           Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
           Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
           Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
