from src.model.pokemon import Pokemon

class PokemonController:
    def show(id):
        pokemon = Pokemon.show(id)

        if pokemon:
            return Pokemon(pokemon[1], pokemon[2])
        
        return None

    def index():
        pokemons = Pokemon.index()

        if pokemons:
            pokemon_list = []
            
            for pokemon in pokemons:
                pokemon_list.append(Pokemon(pokemon[1], pokemon[2]))
            
            return pokemon_list
        
        return None
