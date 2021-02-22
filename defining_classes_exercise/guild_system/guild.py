class Guild():

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if not player.guild == self.name and not player.guild == 'Unaffiliated':
            return f'Player {player.name} is in another guild.'
        else:
            if player not in self.players:
                self.players.append(player)
                player.guild = self.name
                return f'Welcome player {player.name} to the guild {self.name}'
            return f'Player {player.name} is already in the guild.'

    def kick_player(self, player_name):
        for player in self.players:
            if player_name == player.name:
                self.players.remove(player)
                return f'Player {player_name} has been removed from the guild'
        return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        return ''.join([player.player_info() for player in self.players])
