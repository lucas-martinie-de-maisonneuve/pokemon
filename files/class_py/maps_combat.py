import pygame
from files.class_py.screen import Screen
from files.class_py.element import Element
from files.class_py.combat import Combat
import random

class Maps:
    def __init__(self):
        self.run = True
        self.red = (247, 7, 7)
        self.blue = (0, 8, 255)
        self.green = (35, 247, 7)
        self.yellow = (244, 244, 9)
        self.purple = (207, 7, 247)
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
<<<<<<<<< Temporary merge branch 1
            element.img(525, 200, 1244, 700,'fight_background')
            element.img_mir(330, 400, 180, 180, f'pokemon/{img_poke2}')                    
            element.img(665, 225, 180, 180, f"pokemon/{img_poke}")
=========
            element.img(525, 200, 1244, 700,'combat/fight_background')
            element.img_mir(300, 550, 150, 180, f'pokemon/{img_poke2}')                    
            element.img(700, 400, 150, 180, f"pokemon/{img_poke}")
>>>>>>>>> Temporary merge branch 2
            # combat.afficher_capacite()
            element.rect(screen.W -200,screen.H,1000,200," //")
            self.button_attack = element.texte(12, "Attack", self.red, 900, 600)
            self.button_run = element.texte(12, "Flee", self.green, 950 , 600)
            self.button_bag = element.texte(12,"Bag", self.blue, 900, 650)
            self.button_pokedex = element.texte(12,"Pokedex", self.yellow, 950, 650) 

            screen.update()