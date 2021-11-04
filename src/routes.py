
from flask import jsonify, request, render_template, redirect 
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

@app.route('/pokemons', methods=['POST'])
def pokemons_new():
    form_data = request.form.to_dict()

    if PokemonController.new(form_data):
        return redirect("http://localhost:3001/pokemons", code=302)
    
    else:
        return render_template('error.html')

@app.route('/pokemons/form', methods=['GET'])
def pokemons_form():
    return render_template('pokemon_form.html')

@app.route('/pokemons/update', methods=['POST'])
def pokemons_update():
    form_data = request.form
    if PokemonController.update(form_data.to_dict()):
        return redirect("http://localhost:3001/pokemons", code=302)
    else:
        return render_template('error.html')

@app.route('/pokemons/update/<int:id>', methods=['GET'])
def pokemons_update_form(id):
    return render_template('pokemon_update.html', pokemon=PokemonController.show(id))

@app.route('/pokemons/delete/<int:id>', methods=['GET'])
def pokemon_delete(id):
    pokemon = PokemonController.delete(id)
    if pokemon:
        return redirect("http://localhost:3001/pokemons", code=302)