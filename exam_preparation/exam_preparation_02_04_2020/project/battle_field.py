from exam_preparation.exam_preparation_02_04_2020.project.player.player import Player
from exam_preparation.exam_preparation_02_04_2020.project.player.beginner import Beginner


class Battlefield:

    @staticmethod
    def is_dead_player(player1, player2):
        if player1.is_dead or player2.is_dead:
            return True
        return False

    @staticmethod
    def check_if_beginner(player):
        return isinstance(player, Beginner)

    def fight(self, attacker: Player, enemy: Player):
        players = [attacker, enemy]
        if self.is_dead_player(attacker, enemy):
            raise ValueError("Player is dead!")
        for pl in players:
            pl.health += sum([card.health_points for card in pl.card_repository.cards])
            if self.check_if_beginner(pl):
                pl.health += 40
                for card in pl.card_repository.cards:
                    card.damage_points += 30

        for card in attacker.card_repository.cards:
            if enemy.is_dead:
                return
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            if attacker.is_dead:
                return
            attacker.take_damage(card.damage_points)
