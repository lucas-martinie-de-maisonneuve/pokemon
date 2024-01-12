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

    def rand_pokemon(self,data):
        self.pokeliste = []
        for pokemon in self.info_pokemon:
            self.pokeliste.append(pokemon)
        self.poke_random = random.choice(self.pokeliste)

        for pokemon in self.info_pokemon:
            if pokemon['nom'] == self.poke_random['nom']:
                print (pokemon[data])
                return pokemon[data]

     
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
                        if poke_choose == self.get_last_pokemon_number():
                            poke_choose = 1
                    elif event.key == pygame.K_LEFT:
                        if poke_choose > 1:
                            poke_choose -= 1
                        if poke_choose == 1:
                            poke_choose = self.get_last_pokemon_number()
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
                        element.img(320,365, 340 ,360, f'pokedex/bg.{pokemon['type']}')
                        element.img(525, 350, 800, 600, 'pokedex/pokedex')
                        element.img(320, 360, 300, 300, f"pokemon/{pokemon['nom']}")
                        element.img(750, 280, 150, 150, f'pokedex/{pokemon['type']}')
                        element.texte(18, f"Num {pokemon['numero']} - {pokemon['nom']}", (0,0,0), 750, 380)
                        element.texte(18, f"HP : {pokemon['hp']}", (0,0,0), 720, 430)
                        element.texte(18, f"Atq : {pokemon['attaque']}", (0,0,0), 720, 480)
                        element.texte(18, f"Def : {pokemon['def']}", (0,0,0), 720, 530)
                        screen.update()
        

# pokedex.info_rand_pokemon('type')
# pokedex.info_rand_pokemon('debut')
pokedex = Pokedex()
element = Element()
screen = Screen()
# pokedex.show_pokedex()