from exam_preparation.exam_preparation_02_04_2020.project.card.card import Card

class MagicCard(Card):

    def __init__(self, name):
        super().__init__(name, damage_points=5, health_points=80)