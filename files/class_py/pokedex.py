import json
import random
import pygame
from files.class_py.element import Element
from files.class_py.screen import Screen
from files.class_py.combat import Combat

class Pokedex(Element):
    def __init__(self):
        self.info_pokemon = self.ouverture_pokemonjson()
        self.pokedex_run = True

    def ouverture_pokemonjson(self):
        with open('pokemon.json', 'r') as fichier:
            self.donnees_pokemon = json.load(fichier)
            return self.donnees_pokemon
        
    def get_last_pokemon_number(self):
        last_pokemon = self.info_pokemon[-1]
        return last_pokemon['numero']
    
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
        print (self.poke_random)

    def info_rand_pokemon(self, data):
        for pokemon in self.info_pokemon:
            if pokemon['nom'] == self.poke_random['nom']:
                print(pokemon[data])

    def show_pokedex(self):
        poke_choose = 1
        detailed_pokemon = False
        while self.pokedex_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if poke_choose < self.get_last_pokemon_number():
                            poke_choose += 1
                    elif event.key == pygame.K_LEFT:
                        if poke_choose > 1:
                            poke_choose -= 1
                    elif event.key == pygame.K_UP:
                        if poke_choose > 9:
                            poke_choose -= 9
                    elif event.key == pygame.K_DOWN:
                        if poke_choose < 45:
                            poke_choose += 9
                    elif event.key == pygame.K_RETURN:
                        detailed_pokemon = True

            element.img(525, 350, 1050, 743, 'pokedex/background')
            if detailed_pokemon == False:
                for i, pokemon in enumerate(self.info_pokemon):
                    column = i % 9
                    row = i // 9
                    self.pokemon_name = pokemon['nom'].lower()
                    if pokemon['numero'] == poke_choose:
                        element.img(75 + column * 110, 90 + row * 110, 110, 110, f'pokemon/{self.pokemon_name}')
                        element.simple_rect((255,255,255),75 + column * 110, 90 + row * 110, 120, 120,3)

                    else:
                        element.img(75 + column * 110, 90 + row * 110, 85, 85, f'pokemon/{self.pokemon_name}')
                screen.update()

            if detailed_pokemon:
                element.img(525, 350, 1050, 743, 'pokedex/background')
                for pokemon in self.info_pokemon:
                    if poke_choose == pokemon['numero']:
                        element.img(525, 350, 800, 600, 'pokedex/pokedex')
                        element.img(320, 360, 300, 300, f'pokemon/{pokemon['nom']}')
                        # element.img(750, 300, 300, 300, f'pokemon/{pokemon['type']}')
                        element.texte(20, f'Num {pokemon['numero']} - {pokemon['nom']}', (0,0,0), 750, 350)
                        element.texte(20, f'HP : {pokemon['hp']}', (0,0,0), 720, 400)
                        element.texte(20, f'Atq : {pokemon['attaque']}', (0,0,0), 720, 450)
                        element.texte(20, f'Def : {pokemon['def']}', (0,0,0), 720, 500)
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