
from flask import jsonify, request, render_template
from app import app
from src.controller.PokemonController import *


@app.route('/pokemons', methods=['GET'])
def pokemons_index():
    pokemons = PokemonController.index()

    return render_template('pokemon_index.html', pokemons=pokemons)

@app.route('/pokemons/<int:id>', methods=['GET'])
def pokemon_show(id):
    pokemon = PokemonController.show(id)
    
    return render_template('pokemon_show.html', pokemon=pokemon)
