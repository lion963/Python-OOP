from defining_classes_exercise.guild_system.guild import Guild


class Player:

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f'Skill {skill_name} added to the collection of the player {self.name}'
        else:
            return f'Skill already added'

    def player_info(self):
        skill_list = ['===' + key + ' – ' + str(value) for key, value in self.skills.items()]
        return f'Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n' + '\n'.join(
            skill_list)


player = Player("George", 50, 100)
player2 = Player("Asen", 50, 100)
print(player.add_skill("Shield Break", 20))
# print(player.add_skill("Jumping", 30))
print(player.player_info())
guild = Guild("UGT")
# guild1 = Guild("Proba")
print(guild.assign_player(player))
# print(guild1.assign_player(player))
# print(guild.kick_player('adfadf'))
print(guild.guild_info())
