from exam_preparation.exam_19_12_2020.project.medicine.medicine import Medicine
from exam_preparation.exam_19_12_2020.project.supply.food_supply import FoodSupply
from exam_preparation.exam_19_12_2020.project.supply.supply import Supply
from exam_preparation.exam_19_12_2020.project.supply.water_supply import WaterSupply
from exam_preparation.exam_19_12_2020.project.medicine.painkiller import Painkiller
from exam_preparation.exam_19_12_2020.project.medicine.salve import Salve
from exam_preparation.exam_19_12_2020.project.survivor import Survivor


class Bunker:

    def __init__(self):
        self.survivors: list = []
        self.supplies: list = []
        self.medicine: list = []

    @property
    def food(self):
        result = [supply for supply in self.supplies if supply.__class__.__name__ == 'FoodSupply']
        if not result:
            raise IndexError("There are no food supplies left!")
        return result

    @property
    def water(self):
        result = [supply for supply in self.supplies if supply.__class__.__name__ == 'WaterSupply']
        if not result:
            raise IndexError("There are no water supplies left!")
        return result

    @property
    def painkillers(self):
        result = [supply for supply in self.supplies if supply.__class__.__name__ == 'Painkiller']
        if not result:
            raise IndexError("There are no painkillers left!")
        return result

    @property
    def salves(self):
        result = [supply for supply in self.supplies if supply.__class__.__name__ == 'Salve']
        if not result:
            raise IndexError("There are no salves left!")
        return result

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            for med in self.medicine[::-1]:
                if med.__class__.__name__ == medicine_type:
                    med.apply(survivor)
                    self.medicine.remove(med)
                    return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            for supp in self.supplies:
                if supp.__class__.__name__ == sustenance_type:
                    supp.apply(survivor)
                    self.supplies.remove(supp)
                    return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            FoodSupply().apply(survivor)
            WaterSupply().apply(survivor)

