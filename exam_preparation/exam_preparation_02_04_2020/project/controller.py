from exam_preparation.exam_preparation_02_04_2020.project.player.player_repository import PlayerRepository
from exam_preparation.exam_preparation_02_04_2020.project.player.beginner import Beginner
from exam_preparation.exam_preparation_02_04_2020.project.player.advanced import Advanced
from exam_preparation.exam_preparation_02_04_2020.project.card.card_repository import CardRepository
from exam_preparation.exam_preparation_02_04_2020.project.card.magic_card import MagicCard
from exam_preparation.exam_preparation_02_04_2020.project.card.trap_card import TrapCard
from exam_preparation.exam_preparation_02_04_2020.project.battle_field import Battlefield


class Controller:

    def __init__(self):
        self.player_repository: PlayerRepository = PlayerRepository()
        self.card_redpository: CardRepository = CardRepository()

    def add_player(self, type: str, username: str):
        if type == 'Beginner':
            player = Beginner(username)
            self.player_repository.add(player)
            return f"Successfully added player of type {type} with username: {username}"
        if type == 'Advanced':
            player = Advanced(username)
            self.player_repository.add(player)
            return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type: str, name: str):
        if type == 'Magic':
            card = MagicCard(name)
            self.card_redpository.add(card)
            return f"Successfully added card of type {type}Card with name: {name}"
        if type == 'Trap':
            card = TrapCard(name)
            self.card_redpository.add(card)
            return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        card = self.card_redpository.find(card_name)
        player = self.player_repository.find(username)
        player.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        battlefield = Battlefield()
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        battlefield.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = ""
        for player in self.player_repository.players:
            result += f"Username: {player.username} - Health: {player.health} - Cards {len(player.card_repository.cards)}\n"
            for card in player.card_repository.cards:
                result += f"### Card: {card.name} - Damage: {card.damage_points}\n"
        return result
