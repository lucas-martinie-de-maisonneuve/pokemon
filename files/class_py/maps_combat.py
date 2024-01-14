import pygame
from files.class_py.screen import Screen
from files.class_py.element import Element
from files.class_py.pokedex import Pokedex
from files.class_py.combat import Combat
import random

pokedex = Pokedex()
class Maps(Element, Screen):

    def __init__(self):
        self.run = True
        self.action = 1
        Element.__init__(self)
        Screen.__init__(self)
        combat = Combat()
    def home(self):

        self.pokemon_liste = ["salameche", "reptincelle", "dracaufeu", "bulbizarre", "herbizarre", "florizarre", "carapuce", "carabaffe", "tortank", "pikachu", "raichu", "chenipotte", "blindalys", "papinox", "canarticho", "racaillou", "gravalanch", "grolem", "evoli", "aquali", "voltali", "pyroli", "phyllali", "tauros", "kangourex", "elektek", "magmar", "scarabrute", "magicarpe", "leviator", "grainipiot", "pifeuil", "tengalice", "roucool", "roucoups", "roucarnage", "goupix", "fenard", "sabelette", "sablaireau", "osselait", "ossatueur", "insecateur", "magneti", "artikodin", "electhor", "sulfura", "kyogre", "groudon", "rayquaza"]
        pokemon_random = pokedex.rand_pokemon("nom").lower()
        print(pokemon_random)
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
                            
            self.img(525, 200, 1244, 700,"combat/fight_background")
            self.img_mir(250, 325, 350, 350, f"pokemon/{img_poke}")                    
            self.img(725, 225, 175, 175, f"pokemon/{pokemon_random}")
            # combat.afficher_capacite()
            self.button_rect(self.brown,525,650,self.W,210)            
            self.img(300, 625, 470, 150, "combat/background_texte")           
            self.img(850, 625, 399, 150,"combat/zone_texte")
            self.texte(20, "What do you mean ?", self.black, 300, 625)
            # self.rect(self.W -200,self.H,1000,200," //")
            self.button_rect(self.darkred,765,600,145,45)
            self.simple_rect(self.red,765,600,135,35,2)

            self.button_rect(self.darkblue,945,600,145,45)
            self.simple_rect(self.blue, 945,600,135,35,2)

            self.button_rect(self.darkgreen,765,650,145,45)
            self.simple_rect(self.green, 765,650,135,35,2)

            self.button_rect(self.orange,945,650,145,45)
            self.simple_rect(self.yellow, 945,650,135,35,2)

            if self.action == 1 :
                self.button_attack = self.texte(19, "ATTACK", self.white, 765, 600)
                self.img(680, 600, 15, 15, f"combat/arrow")
            else:
                self.button_attack = self.texte(18, "ATTACK", self.black, 765, 600)
            if self.action == 2 :
                self.button_run = self.texte(19, "RUN", self.white, 945 , 600)
                self.img(860, 600, 15, 15, f"combat/arrow")
            else:
                self.button_run = self.texte(18, "RUN", self.black, 945 , 600)
            if self.action == 3 :
                self.button_bag = self.texte(19,"ITEMS", self.white, 765, 650)
                self.img(680, 650, 15, 15, f"combat/arrow")
            else:
                self.button_bag = self.texte(18,"ITEMS", self.black, 765, 650)
            if self.action ==4 :
                self.button_pokedex = self.texte(19,"POKEDEX", self.white, 945, 650)
                self.img(860, 650, 15, 15, f"combat/arrow")
            else:
                self.button_pokedex = self.texte(18,"POKEDEX", self.black, 945, 650)

            self.update()
            
    def starter(self):
        
        self.pokemon_liste = ["salameche", "reptincelle", "dracaufeu", "bulbizarre", "herbizarre", "florizarre", "carapuce", "carabaffe", "tortank", "pikachu", "raichu", "chenipotte", "blindalys", "papinox", "canarticho", "racaillou", "gravalanch", "grolem", "evoli", "aquali", "voltali", "pyroli", "phyllali", "tauros", "kangourex", "elektek", "magmar", "scarabrute", "magicarpe", "leviator", "grainipiot", "pifeuil", "tengalice", "roucool", "roucoups", "roucarnage", "goupix", "fenard", "sabelette", "sablaireau", "osselait", "ossatueur", "insecateur", "magneti", "artikodin", "electhor", "sulfura", "kyogre", "groudon", "rayquaza"]
        
        img_salameche_starter = self.pokemon_liste[0]
        img_bulbi_starter = self.pokemon_liste[3]
        img_carapuce_starter = self.pokemon_liste[6]
        
        self.img(525, 350, 854, 550, "starter/sac_starter")
        self.texte(23, "Choisissez un Pokémon", self.white, 525, 190)
        self.img(215, 310, 180, 180, f"pokemon/{img_salameche_starter}")
        self.img(515, 418, 180, 180, f"pokemon/{img_bulbi_starter}")
        self.img(805, 310, 180, 180, f"pokemon/{img_carapuce_starter}")
        self.update()
        
