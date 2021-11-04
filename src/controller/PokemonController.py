from src.model.pokemon import Pokemon 

class PokemonController:

    def index():
        pokemons = Pokemon.index()

        if pokemons:
            pokemon_list = []
            
            for pokemon in pokemons:
                pokemon_list.append(Pokemon(pokemon[0], pokemon[1], pokemon[2]))
            
            return pokemon_list
        return None

    def show(id):
        pokemon = Pokemon.show(id)

        if pokemon:
            return Pokemon(pokemon[0], pokemon[1], pokemon[2])
        
        return None
    
    def new(pokemon):
        
        id = Pokemon.new(Pokemon(0, pokemon['name'], pokemon['type']))

        if id: return True 
        return False
    
    def update(pokemon):
        id = Pokemon.update(Pokemon(pokemon['id'], pokemon['name'], pokemon['type']))
        
        if id==0: return True 
        else: return False

    def delete(id):
        return Pokemon.delete(id)
