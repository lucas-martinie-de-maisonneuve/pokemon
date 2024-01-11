import json
import random
import pygame
from files.class_py.element import Element
from files.class_py.screen import Screen

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
        print (self.poke_random)

    def info_rand_pokemon(self, data):
        for pokemon in self.info_pokemon:
            if pokemon['nom'] == self.poke_random['nom']:
                print(pokemon[data])

    # def show_pokedex(self):
    #     page = 0
    #     while self.pokedex_run:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 quit()
    #             if event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_RIGHT:
    #                     if page +10 < self.get_last_pokemon_number():
    #                         page += 10

    #                 elif event.key == pygame.K_LEFT:
    #                     if page >= 0:
    #                         page -= 10

    #         element.img(525, 350, 1050, 743, 'pokedex/background')
    #         start_poke = page
    #         end_poke = page + 10

    #         for pokemon in self.info_pokemon[start_poke:end_poke]:

    #             pokemon_name = pokemon['nom'].lower()
    #             element.texte(15, str(pokemon['numero']), (0, 0, 0), 30, 50 + pokemon['numero'] * 60)
    #             element.texte(15, str(pokemon['nom']), (0, 0, 0), 120, 50 + pokemon['numero'] * 60)
    #             element.img(220, 50 + pokemon['numero'] * 60, 60, 60, f'pokemon/{pokemon_name}')
    #             element.texte(15, f'Type : {str(pokemon['type'])}', (0, 0, 0), 330, 50 + pokemon['numero'] * 60)

    #         screen.update()

    def show_pokedex(self):
        page_size = 9 

        element.img(525, 350, 1050, 743, 'pokedex/background')

        for i, pokemon in enumerate(self.info_pokemon):
            column = i % page_size
            row = i // page_size

            pokemon_name = pokemon['nom'].lower()
            element.img(75 + column * 110, 90 + row * 110, 85, 85, f'pokemon/{pokemon_name}')

        screen.update()

    
# pokedex.rand_pokemon()
# pokedex.info_rand_pokemon('type')
# pokedex.info_rand_pokemon('debut')
pokedex = Pokedex()
element = Element()
screen = Screen()
# pokedex.show_pokedex()