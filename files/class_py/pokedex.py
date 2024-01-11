import json
import random
from files.class_py.element import Element
from files.class_py.screen import Screen
from files.class_py.combat import Combat

class Pokedex(Element):
    def __init__(self):
        self.info_pokemon = self.ouverture_pokemonjson()

    def ouverture_pokemonjson(self):
        with open('pokemon.json', 'r') as fichier:
            self.donnees_pokemon = json.load(fichier)
            return self.donnees_pokemon
#### Liste de tout les pokemon ####
    def information_pokemon(self, data):
        self.pokemon_liste = []
        for info_pokemon in self.info_pokemon:
            self.pokemon_liste(info_pokemon[data])  
            print (info_pokemon[data])
### Choix pokemon pour combat #####
    def rand_pokemon(self):
        self.pokeliste = []
        for pokemon in self.info_pokemon:
            self.pokeliste.append(pokemon)
        self.poke_random = random.choice(self.pokeliste)
        return self.poke_random
        
    def info_rand_pokemon(self, data):
        for pokemon in self.info_pokemon:
            if pokemon['nom'] == self.poke_random['nom']:
                print(pokemon[data])

    def show_pokedex(self):
        element.img(525,350,1050,743,'pokedex/background')
        page = 1
        # for pokemon in enumerate(self.info_pokemon[0:10]):
        for pokemon in self.info_pokemon:
            pokemon_name = pokemon['nom'].lower()
            element.texte(10, str(pokemon['numero']), (0,0,0), 30, 50+ pokemon['numero'] * 60)
            element.texte(10, str(pokemon['nom']), (0,0,0), 80, 50+ pokemon['numero'] * 60)
            element.img(180, 50 + pokemon['numero'] * 60, 50, 50, f'pokemon/{pokemon_name}')
            element.texte(10, f"Type : {str(pokemon['type'])}", (0,0,0), 230, 50+ pokemon['numero'] * 60)
            print(pokemon['numero'], pokemon['nom'], pokemon['type'], pokemon['attaque'], pokemon['hp'])
            print (pokemon_name)
        screen.update()
        
    def ajout_pokemon(self, nom, numero_actuelle):        
        try:  
            pokemon_existants = combat.ouverture_pokemonjson()
        except FileNotFoundError:
            pokemon_existants = []

        nouveau_pokemon = {
            "numero": numero_actuelle + 1,
            "nom": nom,
            "evol": 1,
            "type": "feu",
            "debut": 1,
            "fin": None,
            "attaque": None,
            "hp": None,
            "def": None,
            "vitesse": None
        }
        
        pokemon_existants.append(nouveau_pokemon)
        
        with open('pokemon.json', 'w') as fichier:
            json.dump(pokemon_existants, fichier)

        return nouveau_pokemon
    
# pokedex.rand_pokemon()
# pokedex.info_rand_pokemon('type')
# pokedex.info_rand_pokemon('debut')
pokedex = Pokedex()
element = Element()
screen = Screen()
combat = Combat()
# pokedex.show_pokedex()