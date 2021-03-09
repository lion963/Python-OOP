from polymorphism_and_magic_methods_exercise.animals.cat import Cat


class Kitten(Cat):
    gender = "Female"

    def __init__(self, name, age):
        super().__init__(name, age, Kitten.gender)

    def make_sound(self):
        return f"Meow"