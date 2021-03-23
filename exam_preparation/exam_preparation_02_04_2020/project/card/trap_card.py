from exam_preparation.exam_preparation_02_04_2020.project.card.card import Card

class TrapCard(Card):

    def __init__(self, name):
        super().__init__(name, damage_points=120, health_points=5)