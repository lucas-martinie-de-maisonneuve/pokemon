import pygame
from files.class_py.screen import Screen
from files.class_py.element import Element
from files.class_py.pokedex import Pokedex
# from files.class_py.combat import Combat
import random

element = Element()
screen = Screen()
# combat = Combat()

class Maps:
    def __init__(self):
        self.run = True
        self.action = 1
    def home(self):
        element = Element()
        screen = Screen()
        pokedex = Pokedex()
        # combat = Combat()

        self.pokemon_liste = ["salameche", "reptincelle", "dracaufeu", "bulbizarre", "herbizarre", "florizarre", "carapuce", "carabaffe", "tortank", "pikachu", "raichu", "chenipotte", "blindalys", "papinox", "canarticho", "racaillou", "gravalanch", "grolem", "evoli", "aquali", "voltali", "pyroli", "phyllali", "tauros", "kangourex", "elektek", "magmar", "scarabrute", "magicarpe", "leviator", "grainipiot", "pifeuil", "tengalice", "roucool", "roucoups", "roucarnage", "goupix", "fenard", "sabelette", "sablaireau", "osselait", "ossatueur", "insecateur", "magneti", "artikodin", "electhor", "sulfura", "kyogre", "groudon", "rayquaza"]

        img_poke = random.choice(self.pokemon_liste)
        img_poke2 = random.choice(self.pokemon_liste)

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
                            pokedex.pokedex_run = True
                            pokedex.show_pokedex()
                            
            element.img(525, 200, 1244, 700,"combat/fight_background")
            element.img_mir(250, 325, 350, 350, f"pokemon/{img_poke}")                    
            element.img(725, 225, 175, 175, f"pokemon/{img_poke2}")
            # combat.afficher_capacite()
            element.button_rect(element.brown,525,650,screen.W,210)            
            element.img(300, 625, 470, 150, "combat/background_texte")           
            element.img(850, 625, 399, 150,"combat/zone_texte")
            element.texte(20, "What do you mean ?", element.black, 300, 625)
            # element.rect(screen.W -200,screen.H,1000,200," //")
            element.button_rect(element.darkred,765,600,145,45)
            element.simple_rect(element.red,765,600,135,35,2)

            element.button_rect(element.darkblue,945,600,145,45)
            element.simple_rect(element.blue, 945,600,135,35,2)

            element.button_rect(element.darkgreen,765,650,145,45)
            element.simple_rect(element.green, 765,650,135,35,2)

            element.button_rect(element.orange,945,650,145,45)
            element.simple_rect(element.yellow, 945,650,135,35,2)

            if self.action == 1 :
                self.button_attack = element.texte(19, "ATTACK", element.white, 765, 600)
                element.img(680, 600, 15, 15, f"combat/arrow")
            else:
                self.button_attack = element.texte(18, "ATTACK", element.black, 765, 600)
            if self.action == 2 :
                self.button_run = element.texte(19, "RUN", element.white, 945 , 600)
                element.img(860, 600, 15, 15, f"combat/arrow")
            else:
                self.button_run = element.texte(18, "RUN", element.black, 945 , 600)
            if self.action == 3 :
                self.button_bag = element.texte(19,"ITEMS", element.white, 765, 650)
                element.img(680, 650, 15, 15, f"combat/arrow")
            else:
                self.button_bag = element.texte(18,"ITEMS", element.black, 765, 650)
            if self.action ==4 :
                self.button_pokedex = element.texte(19,"POKEDEX", element.white, 945, 650)
                element.img(860, 650, 15, 15, f"combat/arrow")
            else:
                self.button_pokedex = element.texte(18,"POKEDEX", element.black, 945, 650)

            screen.update()
            
    def starter(self):
        
        self.pokemon_liste = ["salameche", "reptincelle", "dracaufeu", "bulbizarre", "herbizarre", "florizarre", "carapuce", "carabaffe", "tortank", "pikachu", "raichu", "chenipotte", "blindalys", "papinox", "canarticho", "racaillou", "gravalanch", "grolem", "evoli", "aquali", "voltali", "pyroli", "phyllali", "tauros", "kangourex", "elektek", "magmar", "scarabrute", "magicarpe", "leviator", "grainipiot", "pifeuil", "tengalice", "roucool", "roucoups", "roucarnage", "goupix", "fenard", "sabelette", "sablaireau", "osselait", "ossatueur", "insecateur", "magneti", "artikodin", "electhor", "sulfura", "kyogre", "groudon", "rayquaza"]
        
        img_salameche_starter = self.pokemon_liste[0]
        img_bulbi_starter = self.pokemon_liste[3]
        img_carapuce_starter = self.pokemon_liste[6]
        
        element.img(525, 350, 854, 550, "starter/sac_starter")
        element.texte(23, "Choisissez un Pokémon (1, 2 ou 3)", element.white, 525, 190)
        element.img(215, 310, 180, 180, f"pokemon/{img_salameche_starter}")
        element.img(515, 418, 180, 180, f"pokemon/{img_bulbi_starter}")
        element.img(805, 310, 180, 180, f"pokemon/{img_carapuce_starter}")
        screen.update()
        
