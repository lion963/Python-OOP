from defining_classes_exercise.pokemon_battle.pokemon import Pokemon

class Trainer():

    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f'Caught {pokemon.name} with health {pokemon.health}'
        return f'This pokemon is already caught'

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemon:
            if pokemon_name == pokemon.name:
                self.pokemon.remove(pokemon)
                return f'You have released {pokemon_name}'
        return f'Pokemon is not caught'

    def trainer_data(self):
        return f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n- {'- '.join([pokemon_obj.pokemon_details() for pokemon_obj in self.pokemon])}"
