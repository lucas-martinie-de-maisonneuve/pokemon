import json
import random
import pygame
from files.class_py.element import Element
from files.class_py.screen import Screen

class Pokedex(Element):
    def __init__(self):
        self.info_pokemon = self.ouverture_pokemonjson()
        self.pokedex_run = False
        self.detailed_pokemon = False
        self.pokemon_counter = {}
        Element.__init__(self)

    def ouverture_pokemonjson(self):
        with open('pokemon.json', 'r') as fichier:
            self.donnees_pokemon = json.load(fichier)
            return self.donnees_pokemon

    def get_last_pokemon_number(self):
        last_pokemon = self.info_pokemon[-1]
        return last_pokemon['numero']

    def starter(self):
        self.starter1 = self.info_pokemon[0]
        self.starter2 = self.info_pokemon[3]
        self.starter3 = self.info_pokemon[6]
        self.starter4 = self.info_pokemon[9]
        return self.starter1, self.starter2, self.starter3, self.starter4 
#### Liste de tout les pokemon ####
    def information_pokemon(self, data):
        self.pokemon_liste = []
        for info_pokemon in self.info_pokemon:
            self.pokemon_liste(info_pokemon[data])  

    def pokemon_rencontre(self, meet):
        for pokemon in self.info_pokemon:
            if meet == pokemon["nom"]:
                if meet in self.pokemon_counter:
                    self.pokemon_counter[meet] += 1
                else:
                    self.pokemon_counter[meet] = 1

                return {
                    "nom": pokemon,
                    "counter": self.pokemon_counter[meet]
                }

    def rand_pokemon(self):
        random_pokemon = random.choice(self.info_pokemon)
        return {
            'numero': random_pokemon['numero'],
            'nom': random_pokemon['nom'],
            'fin': random_pokemon['evol'],
            'type': random_pokemon['type'],
            'attaque': random_pokemon['attaque'],
            'hp': random_pokemon['hp'],
            'def': random_pokemon['def']
        }

    def show_pokedex(self):
        poke_choose = 1
        while self.pokedex_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if poke_choose < self.get_last_pokemon_number() +1:
                            poke_choose += 1
                        if poke_choose == self.get_last_pokemon_number() +1:
                            poke_choose = 1
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        if poke_choose > 0:
                            poke_choose -= 1
                        if poke_choose == 0:
                            poke_choose = self.get_last_pokemon_number()
                    elif event.key == pygame.K_UP or event.key == pygame.K_z and not self.detailed_pokemon:
                        if poke_choose > 9:
                            poke_choose -= 9
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s and not self.detailed_pokemon:
                        if poke_choose < 45:
                            poke_choose += 9
                    elif event.key == pygame.K_RETURN:
                        self.detailed_pokemon = True
                    elif event.key == pygame.K_ESCAPE:
                        if self.detailed_pokemon:
                            self.detailed_pokemon = False
                        else:
                            self.pokedex_run = False

            element.img(525, 350, 1050, 743, 'pokedex/background')
            if self.detailed_pokemon == False:
                for i, pokemon in enumerate(self.info_pokemon):
                    column = i % 9
                    row = i // 9
                    self.pokemon_name = pokemon['nom'].lower()
                    if pokemon['nom'] in self.pokemon_counter:
                        if pokemon['numero'] == poke_choose:
                            element.img(75 + column * 110, 90 + row * 110, 110, 110, f'pokemon/{self.pokemon_name}')
                            element.simple_rect((255,255,255),75 + column * 110, 90 + row * 110, 120, 120,3)
                            element.texte(18, f"{pokemon['numero']} / {self.get_last_pokemon_number()}",(255,255,255),1000, 680)


                        else:
                            element.img(75 + column * 110, 90 + row * 110, 85, 85, f'pokemon/{self.pokemon_name}')
                    else:
                        if pokemon['numero'] == poke_choose:
                            element.simple_rect((255,255,255),75 + column * 110, 90 + row * 110, 120, 120,3)
                            element.img(75 + column * 110, 90 + row * 110, 85, 85, f'pokemon/unknown')
                            element.texte(30, "?", (255, 255, 255), 75 + column * 110, 90 + row * 110)
                            element.texte(18, f"{pokemon['numero']} / {self.get_last_pokemon_number()}",(255,255,255),1000, 680)

                        else:
                            element.img(75 + column * 110, 90 + row * 110, 85, 85, f'pokemon/unknown')
                            element.texte(30, "?", (255, 255, 255), 75 + column * 110, 90 + row * 110)
                screen.update()

            if self.detailed_pokemon:
                element.img(525, 350, 1050, 743, 'pokedex/background')
                for pokemon in self.info_pokemon:
                    if pokemon['nom'] in self.pokemon_counter:
                        if poke_choose == pokemon['numero']:
                            element.img(320,365, 340 ,360, f"pokedex/bg.{pokemon['type']}")
                            element.img(525, 350, 800, 600, 'pokedex/pokedex')
                            element.img(320, 360, 300, 300, f"pokemon/{pokemon['nom']}")
                            element.img(750, 280, 150, 150, f"pokedex/{pokemon['type']}")
                            element.texte(18, f"Num {pokemon['numero']} - {pokemon['nom']}", (0,0,0), 750, 380)
                            element.texte(18, f"HP : {pokemon['hp']}", (0,0,0), 750, 430)
                            element.texte(18, f"Atq : {pokemon['attaque']}", (0,0,0), 750, 480)
                            element.texte(18, f"Def : {pokemon['def']}", (0,0,0), 750, 530)
                            element.texte(18, f"{pokemon['numero']} / {self.get_last_pokemon_number()}",(255,255,255),1000, 680)
                    elif pokemon['nom'] not in self.pokemon_counter:
                        if poke_choose == pokemon['numero']:
                            element.img(525, 350, 800, 600, 'pokedex/pokedex')
                            element.img(320, 360, 300, 300, f"pokemon/unknown")
                            element.texte(100, "?", (255,255,255), 325, 360)
                            element.img(750, 280, 150, 150, f"pokedex/unknowntype")
                            element.texte(50, "?", (255,255,255), 750, 290)
                            element.texte(18, "Num ??? - ???", (0,0,0), 750, 380)
                            element.texte(18, "HP : ???", (0,0,0), 750, 430)
                            element.texte(18, "Atq : ???", (0,0,0), 750, 480)
                            element.texte(18, "Def : ???", (0,0,0), 750, 530)
                            element.texte(18, f"{pokemon['numero']} / {self.get_last_pokemon_number()}",(255,255,255),1000, 680)

                screen.update()

pokedex = Pokedex()
element = Element()
screen = Screen()
