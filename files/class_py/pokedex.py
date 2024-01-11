import json
import random

class Pokedex:
    def __init__(self):
        pass

    def ouverture_pokemonjson(self):
        with open('pokemon.json', 'r') as fichier:
            self.donnees_pokemon = json.load(fichier)
            return self.donnees_pokemon
    
    # A utilise pour le pokedex      
    def information_pokemon(self, data):
        self.info_pokemon = self.ouverture_pokemonjson()
        self.pokemon_liste = []
        for info_pokemon in self.info_pokemon:
            self.pokemon_liste(info_pokemon[data])  
            print (info_pokemon[data])    
    
    # Pour le class combat, type            
    def rand_pokemon(self):
        self.info_pokemon = self.ouverture_pokemonjson()
        self.pokeliste = []
        for pokemon in self.info_pokemon:
            self.pokeliste.append(pokemon)
        self.poke_random = random.choice(self.pokeliste)
        return self.poke_random
        
    def info_rand_pokemon(self, data):
        self.info_pokemon = self.ouverture_pokemonjson()
        for pokemon in self.info_pokemon:
            if pokemon['nom'] == self.poke_random['nom']:
                print(pokemon["nom"])
    
pokedex = Pokedex()
pokedex.rand_pokemon()
pokedex.info_rand_pokemon('type')
pokedex.info_rand_pokemon('debut')