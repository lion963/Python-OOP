from exam_preparation.exam_preparation_02_04_2020.project.player.player import Player

class Advanced(Player):

    def __init__(self, username):
        super().__init__(username, health=250)