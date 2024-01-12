import pygame
from files.class_py.screen import Screen
from files.class_py.element import Element
from files.class_py.combat import Combat
import random

class Maps:
    def __init__(self):
        self.run = True
    def home(self):
        element = Element()
        screen = Screen()
        combat = Combat()


        pokemon_liste = ["salameche", "reptincelle", "dracaufeu", "bulbizarre", "herbizarre", "florizarre", "carapuce", "carabaffe", "tortank", "pikachu", "raichu", "chenipotte", "blindalys", "papinox", "canarticho", "racaillou", "gravalanch", "grolem", "evoli", "aquali", "voltali", "pyroli", "phyllali", "tauros", "kangourex", "elektek", "magmar", "scarabrute", "magicarpe", "leviator", "grainipiot", "pifeuil", "tengalice", "roucool", "roucoups", "roucarnage", "goupix", "fenard", "sabelette", "sablaireau", "osselait", "ossatueur", "insecateur", "magneti", "artikodin", "electhor", "sulfura", "kyogre", "groudon", "rayquaza"]

        img_poke = random.choice(pokemon_liste)
        img_poke2 = random.choice(pokemon_liste)

        while self.run :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            element.img(525, 200, 1244, 700,'combat/fight_background')
            element.img_mir(300, 550, 150, 180, f'pokemon/{img_poke2}')                    
            element.img(700, 400, 150, 180, f"pokemon/{img_poke}")
            # combat.afficher_capacite()
            element.img(850, 625, 399, 150,'combat/zone_texte')
            self.button_attack = element.texte(18, "Attack", element.red, 750, 600)
            self.button_run = element.texte(18, "Flee", element.green, 950 , 600)
            self.button_bag = element.texte(18,"Bag", element.blue, 750, 650)
            self.button_pokedex = element.texte(18,"Pokedex", element.yellow, 950, 650) 
            screen.update()
