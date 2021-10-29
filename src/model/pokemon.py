from src.db.db_connection import db

class Pokemon:
    def __init__(self, name, type_pokemon):
        self.name = str(name)
        self.type_pokemon = str(type_pokemon)
    
    def __str__(self):
        return f"Este é o pokemon {self.name}, do tipo {self.type_pokemon}"

    
    def show(id):
        query = f"SELECT * FROM pokemon WHERE id={id}"
        
        pokemon = db.execute(query)
        
        if pokemon == []: return None
        
        return pokemon[0]
    
    def index():
        query = "SELECT * FROM pokemon"

        pokemons = db.execute(query)

        return pokemons