from src.db.db_connection import db

class Pokemon:      
    def __str__(self):
        return f"Este é o pokemon {self.name}, do tipo {self.type_pokemon}"
  
    def __init__(self, id, name, type_pokemon):
        self.id = int(id)
    
        self.name = str(name)
    
        self.type_pokemon = str(type_pokemon)
    
    def index():
        query = "SELECT * FROM pokemon"

        pokemons = db.execute(query)

        return pokemons
    
    def show(id):
        query = f"SELECT * FROM pokemon WHERE id={id}"
        
        pokemon = db.execute(query)
        
        if pokemon == []: return None
        
        return pokemon[0]
    
    def new(pokemon):
        query = f"INSERT INTO pokemon (name, type) VALUES ('{pokemon.name}', '{pokemon.type_pokemon}')"
        
        pokemon = db.execute(query)
        
        id = db.cur.lastrowid
        
        db.save()
        
        return id

    def update(pokemon):
        query = f'''
        UPDATE pokemon
        SET name = '{pokemon.name}' , type = '{pokemon.type_pokemon}'
            WHERE id = {pokemon.id}
        '''
        
        pokemon = db.execute(query)
        
        id = db.cur.lastrowid
        
        db.save()
        
        return id

    def delete(id):
        query = f"DELETE FROM pokemon WHERE id={id}"
        
        pokemon = db.execute(query)
        
        db.save()
        
        if pokemon == []: return True
        
        return False
