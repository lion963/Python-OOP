class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        new_obj=Person(self.name, other.surname)
        return new_obj

    def __repr__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name, people):
        self.people = people
        self.name = name

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        name_list = []
        for p in self.people:
            name_list.append(str(p))
        return f"Group {self.name} with members {', '.join(name_list)}"

    def __add__(self, other):
        list1=self.people+other.people
        name_list=[f"Person {i}: {str(list1[i])}" for i in range(len(list1))]
        new_obj=Group(f"{self.name}&{other.name}", name_list)
        return new_obj

    def __getitem__(self, index):
        return self.people[index]



p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
