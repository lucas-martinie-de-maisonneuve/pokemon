import pygame
from files.class_py.screen import Screen
from files.class_py.element import Element
from files.class_py.pokedex import Pokedex
# from files.class_py.combat import Combat
import random

class Maps:
    def __init__(self):
        self.run = True
        self.action = 1
    def home(self):
        element = Element()
        screen = Screen()
        pokedex = Pokedex()
        # combat = Combat()

        pokemon_liste = ["salameche", "reptincelle", "dracaufeu", "bulbizarre", "herbizarre", "florizarre", "carapuce", "carabaffe", "tortank", "pikachu", "raichu", "chenipotte", "blindalys", "papinox", "canarticho", "racaillou", "gravalanch", "grolem", "evoli", "aquali", "voltali", "pyroli", "phyllali", "tauros", "kangourex", "elektek", "magmar", "scarabrute", "magicarpe", "leviator", "grainipiot", "pifeuil", "tengalice", "roucool", "roucoups", "roucarnage", "goupix", "fenard", "sabelette", "sablaireau", "osselait", "ossatueur", "insecateur", "magneti", "artikodin", "electhor", "sulfura", "kyogre", "groudon", "rayquaza"]

        img_poke = random.choice(pokemon_liste)
        img_poke2 = random.choice(pokemon_liste)

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:                  
                    if event.key == pygame.K_RIGHT:
                        if self.action < 4:
                            self.action += 1
                    elif event.key == pygame.K_LEFT:
                        if self.action > 1:
                            self.action -= 1
                    elif event.key == pygame.K_UP and self.action > 2:
                        self.action -= 2
                    elif event.key == pygame.K_DOWN and self.action < 3:
                        self.action += 2
                    elif event.key == pygame.K_RETURN:
                        if self.action == 1:
                            pass
                        elif self.action == 2:
                            pass
                        elif self.action == 3:
                            pass
                        elif self.action == 4:
                            pokedex.show_pokedex()
                            pokedex.pokedex_run = True
                            
            element.img(525, 200, 1244, 700,'combat/fight_background')
            element.button_rect(element.brown,525,650,screen.W,215)            
            element.img_mir(300, 375, 150, 180, f'pokemon/{img_poke}')                    
            element.img(660, 225, 150, 180, f"pokemon/{img_poke2}")
            # combat.afficher_capacite()
            element.img(300, 625, 470, 150, 'combat/background_texte')           
            element.img(850, 625, 399, 150,'combat/zone_texte')
            element.texte(20, "What do you mean ?", element.black, 300, 625)
            # element.rect(screen.W -200,screen.H,1000,200," //")
            element.button_rect(element.red,760,600,145,45)
            element.simple_rect(element.black,760,600,125,35,1)

            element.button_rect(element.blue,940,600,145,45)
            element.simple_rect(element.black, 940,600,125,35,1)

            element.button_rect(element.purple,760,650,145,45)
            element.simple_rect(element.black, 760,650,125,35,1)

            element.button_rect(element.yellow,940,650,145,45)
            element.simple_rect(element.black, 940,650,125,35,1)

            if self.action == 1 :
                self.button_attack = element.texte(18, "Attack", element.white, 760, 600)
                element.img(675, 600, 15, 15, f"combat/arrow")
            else:
                self.button_attack = element.texte(18, "Attack", element.black, 760, 600)
            if self.action == 2 :
                self.button_run = element.texte(18, "Flee", element.white, 940 , 600)
                element.img(855, 600, 15, 15, f"combat/arrow")
            else:
                self.button_run = element.texte(18, "Flee", element.black, 940 , 600)
            if self.action == 3 :
                self.button_bag = element.texte(18,"Bag", element.white, 760, 650)
                element.img(675, 650, 15, 15, f"combat/arrow")
            else:
                self.button_bag = element.texte(18,"Bag", element.black, 760, 650)
            if self.action ==4 :
                self.button_pokedex = element.texte(18,"Pokedex", element.white, 940, 650)
                element.img(855, 650, 15, 15, f"combat/arrow")
            else:
                self.button_pokedex = element.texte(18,"Pokedex", element.black, 940, 650)

            screen.update()
