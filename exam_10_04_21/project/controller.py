from exam_10_04_21.project.aquarium.freshwater_aquarium import FreshwaterAquarium
from exam_10_04_21.project.aquarium.saltwater_aquarium import SaltwaterAquarium
from exam_10_04_21.project.decoration.decoration_repository import DecorationRepository
from exam_10_04_21.project.decoration.ornament import Ornament
from exam_10_04_21.project.decoration.plant import Plant
from exam_10_04_21.project.fish.freshwater_fish import FreshwaterFish
from exam_10_04_21.project.fish.saltwater_fish import SaltwaterFish


class Controller:

    def __init__(self):
        self.decorations_repository: DecorationRepository = DecorationRepository()
        self.aquariums: list = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        aquarium_types = ["FreshwaterAquarium", "SaltwaterAquarium"]
        if aquarium_type not in aquarium_types:
            return f"Invalid aquarium type."
        if aquarium_type == "FreshwaterAquarium":
            aquarium = FreshwaterAquarium(aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."
        elif aquarium_type == "SaltwaterAquarium":
            aquarium = SaltwaterAquarium(aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        decoration_types = ["Ornament", "Plant"]
        if decoration_type not in decoration_types:
            return f"Invalid decoration type."
        if decoration_type == "Ornament":
            decoration = Ornament()
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."
        elif decoration_type == "Plant":
            decoration = Plant()
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        aquarium = [aqur for aqur in self.aquariums if aqur.name == aquarium_name]
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."
        if aquarium:
            aquarium[0].decorations.append(decoration)
            self.decorations_repository.decorations.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        fish_types = ["FreshwaterFish", "SaltwaterFish"]
        aquarium = [aqur for aqur in self.aquariums if aqur.name == aquarium_name]
        if fish_type not in fish_types:
            return f"There isn't a fish of type {fish_type}."
        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
            res=aquarium[0].add_fish(fish)
            if res:
                return res
            if fish not in aquarium[0].fish:
                return f"Water not suitable."
        elif fish_type == "SaltwaterFish":
            fish = SaltwaterFish(fish_name, fish_species, price)
            res = aquarium[0].add_fish(fish)
            if res:
                return res
            if fish not in aquarium[0].fish:
                return f"Water not suitable."

    def feed_fish(self, aquarium_name: str):
        aquarium = [aqur for aqur in self.aquariums if aqur.name == aquarium_name]
        if aquarium:
            aquarium[0].feed()
            return f"Fish fed: {len(aquarium[0].fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = [aqur for aqur in self.aquariums if aqur.name == aquarium_name]
        if aquarium:
            decoration_sum = sum([decor.price for decor in aquarium[0].decorations])
            fish_sum = sum([fis.price for fis in aquarium[0].fish])
            value = decoration_sum + fish_sum
            return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += f"{aquarium.__str__()}\n"
        return result



