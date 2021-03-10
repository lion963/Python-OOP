class Animal:
    def __init__(self, species):
        self.__species = species

    @property
    def species(self):
        return self.__species

    def make_sound(self):
        return animals_call[self.species]

def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())

animals_call={'dog': 'woof-woof', 'cat': 'meow', 'chicken': 'chick', 'lion': 'rrrrrrrr...'}
animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
animal_sound(animals)

