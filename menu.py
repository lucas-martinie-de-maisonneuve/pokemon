import pygame
from screen import Screen
import random

class Menu:
    def __init__(self):
        self.run = True

    def menu_open(self):
        screen = Screen()
        pokemon_liste = ["salameche", "reptincelle", "dracaufeu", "bulbizarre", "herbizarre", "florizarre", "carapuce", "carabaffe", "tortank", "pikachu", "raichu", "chenipotte", "blindalys", "papinox", "canarticho", "racaillou", "gravalanch", "grolem", "evoli", "aquali", "voltali", "pyroli", "phyllali", "tauros", "kangourex", "elektek", "magmar", "scarabrute", "magicarpe", "leviator", "grainipiot", "pifeuil", "tengalice", "roucool", "roucoups", "roucarnage", "goupix", "fenard", "sabelette", "sablaireau", "osselait", "ossatueur", "insecateur", "magneti", "artikodin", "electhor", "sulfura", "kyogre", "groudon", "rayquaza"]
        img_poke = random.choice(pokemon_liste)
        img_poke2 = random.choice(pokemon_liste)
        while self.run :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            screen.update()
            screen.img_mir(250, 500, 180, 180, f'pokemon/{img_poke2}')
            screen.img(800, 200, 180, 180, f'pokemon/{img_poke}')