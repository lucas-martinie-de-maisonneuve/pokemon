import pygame
from files.class_py.screen import Screen
from files.class_py.element import Element
from files.class_py.pokedex import Pokedex
import random

class Maps:
    def __init__(self):
        self.run = True

    def home(self):
        element = Element()
        screen = Screen()
        pokedex = Pokedex()

        pokemon_liste = ["salameche", "reptincelle", "dracaufeu", "bulbizarre", "herbizarre", "florizarre", "carapuce", "carabaffe", "tortank", "pikachu", "raichu", "chenipotte", "blindalys", "papinox", "canarticho", "racaillou", "gravalanch", "grolem", "evoli", "aquali", "voltali", "pyroli", "phyllali", "tauros", "kangourex", "elektek", "magmar", "scarabrute", "magicarpe", "leviator", "grainipiot", "pifeuil", "tengalice", "roucool", "roucoups", "roucarnage", "goupix", "fenard", "sabelette", "sablaireau", "osselait", "ossatueur", "insecateur", "magneti", "artikodin", "electhor", "sulfura", "kyogre", "groudon", "rayquaza"]
        # rand_poke = str(pokedex.info_rand_pokemon(["nom"])).lower()
        # poke_random = pokedex.info_rand_pokemon(rand_poke)
        
        img_poke = random.choice(pokemon_liste)
        img_poke2 = random.choice(pokemon_liste)
        # screen.img(50, 150, 150, 150, f'pokemon/{img_poke}')
        while self.run :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            element.img(525, 350, 1244, 700,'fight_background')
            element.img_mir(300, 550, 150, 150, f'pokemon/{img_poke2}')                    
            element.img(700, 400, 150, 150, f"pokemon/{img_poke}")
            screen.update()
                