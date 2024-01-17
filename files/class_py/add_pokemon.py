import pygame
import json
from files.class_py.pokedex import Pokedex
from files.class_py.screen import Screen
from files.class_py.element import Element

pokedex = Pokedex()

class AddPokemon(Element, Screen):
    def __init__(self):
        Element.__init__(self)
        Screen.__init__(self)
        
    def ajout_pokemon(self):
            select_type = ["plante", "feu", "eau", "sol", "elec", "vol", "normal", "insecte", "plante", "feu", "eau", "sol", "elec", "vol", "normal", "insecte"]
            self.i = 0
            self.cate = 1
            enregistre = False
            confirm = False
            add_pokemon_name = ""
            add_pokemon_level = 1
            add_pokemon_type = select_type[self.i]
            add_pokemon_hp = ""
            add_pokemon_attaque = ""
            add_pokemon_def = ""
            active = True
            self.select_stat = 1
            while active:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            active = False
                        elif event.key == pygame.K_DOWN:
                            if self.cate < 5:
                                self.cate +=1
                        elif event.key == pygame.K_UP:
                            if self.cate > 1:
                                self.cate -= 1
                        elif event.key == pygame.K_RIGHT:
                            if self.cate == 2 and add_pokemon_level < 3:
                                 add_pokemon_level += 1
                            elif self.cate == 3:
                                if self.i == 8:
                                    self.i = 0
                                self.i +=1
                                add_pokemon_type = select_type[self.i]
                            elif self.cate ==4 and self.select_stat < 3:
                                self.select_stat += 1

                        elif event.key == pygame.K_LEFT:
                            if self.cate == 2 and add_pokemon_level > 1:
                                add_pokemon_level -= 1
                            elif self.cate == 3:
                                if self.i == 0:
                                    self.i = 8
                                self.i -=1
                                add_pokemon_type = select_type[self.i]
                            elif self.cate ==4 and self.select_stat > 1:
                                self.select_stat -= 1

                        elif event.key == pygame.K_RETURN and self.cate == 5:
                            confirm = True
                            # data_pokemon = pokedex.ouverture_pokemonjson()
                            # nouveau_pokemon = {
                            #     "numero": (pokedex.get_last_pokemon_number() +1),
                            #     "nom": add_pokemon_name,
                            #     "evol": add_pokemon_level,
                            #     "type": add_pokemon_type,
                            #     "attaque": add_pokemon_attaque,
                            #     "hp": add_pokemon_hp,
                            #     "def": add_pokemon_def,
                            #     "rencontre": 1,
                            # }
                            # data_pokemon.append(nouveau_pokemon)

                            # with open("pokemon.json", "w") as fichier:
                            #     json.dump(data_pokemon, fichier)
                            # enregistre = True

                        elif event.key == pygame.K_BACKSPACE:
                            if self.cate == 1 :
                                add_pokemon_name = add_pokemon_name[:-1]
                            if self.cate == 4 and self.select_stat == 1 :
                                add_pokemon_hp = add_pokemon_hp[:-1]
                            if self.cate == 4 and self.select_stat == 2 :
                                add_pokemon_attaque = add_pokemon_attaque[:-1]
                            if self.cate == 4 and self.select_stat == 3 :
                                add_pokemon_def = add_pokemon_def[:-1]

                        else:
                            if self.cate == 1:
                                add_pokemon_name += event.unicode
                            if self.cate == 4:
                                if self.select_stat == 1:
                                    add_pokemon_hp += event.unicode
                                if self.select_stat == 2:
                                    add_pokemon_attaque += event.unicode
                                if self.select_stat == 3:
                                    add_pokemon_def += event.unicode

                self.img(525, 350, 1050, 743, "add_pokemon/test_img")
                if confirm: 
                    self.texte(25, "Résumé des informations", self.white, 525, 50)
                else:
                    self.texte(25, "Saisir les informations du Pokemon :", self.white, 525, 50)

                self.texte(20, "Nom :", self.black,525, 100)
                self.button_rect(self.white, 525, 160, 450 ,70)
                self.simple_rect(self.black, 525, 160, 450, 70, 3)
                self.texte(30, add_pokemon_name, self.black, 525, 160)

                if add_pokemon_level == 1:
                    self.button_rect(self.lightyellow, 375, 300, 125 ,70)
                else:
                    self.button_rect(self.white, 375, 300, 125 ,70)
                if add_pokemon_level == 2:
                    self.button_rect(self.lightyellow, 525, 300, 125 ,70)
                else:
                    self.button_rect(self.white, 525, 300, 125 ,70)
                if add_pokemon_level == 3:
                    self.button_rect(self.lightyellow, 675, 300, 125 ,70)
                else:
                    self.button_rect(self.white, 675, 300, 125 ,70)
                self.texte(20, "Niveau Evol :", self.black,525, 240)
                self.simple_rect(self.black, 375, 300, 125, 70, 3)
                self.img(375, 300, 65,65, "add_pokemon/evol1")
                self.simple_rect(self.black, 525, 300, 125, 70, 3)
                self.img(525, 300, 65,65, "add_pokemon/evol2")
                self.simple_rect(self.black, 675, 300, 125, 70, 3)
                self.img(675, 300, 65,65, "add_pokemon/evol3")

                self.texte(20, "Type :", self.black,525, 380)
                self.img(400, 435, 70, 70, f"pokedex/{select_type[self.i -2]}")
                self.img(445, 440, 80, 80, f"pokedex/{select_type[self.i -1]}")
                self.img(525, 445, 90, 90, f"pokedex/{select_type[self.i]}")
                self.img(645, 435, 70, 70, f"pokedex/{select_type[self.i +2]}")
                self.img(605, 440, 80, 80, f"pokedex/{select_type[self.i +1]}")

                if self.cate == 1:
                    self.img(100, 160, 40, 40, "combat/arrow")
                elif self.cate == 2:
                    self.img(100, 300, 40, 40, "combat/arrow")
                elif self.cate == 3:
                    self.img(100, 445, 40, 40, "combat/arrow")
                elif self.cate == 4:
                    self.img(100, 590, 40, 40, "combat/arrow")
                elif self.cate == 5:
                    self.img(100, 660, 40, 40, "combat/arrow")

                if self.cate == 4 and self.select_stat == 1 or add_pokemon_hp != "":
                    self.button_rect(self.white, 375, 580, 125 ,70)
                    self.texte(30, add_pokemon_hp, self.black, 375, 580)
                    self.button_rect(self.yellow, 375, 525, 80 ,30)
                    self.texte(20, "HP", self.black,375, 525)
                    self.simple_rect(self.black, 375, 525, 80, 30, 3)

                elif add_pokemon_hp == "":
                    self.button_rect(self.yellow, 375, 580, 125 ,70)
                    self.texte(20, "HP", self.black,375, 580)

                if self.cate == 4 and self.select_stat == 2 or add_pokemon_attaque != "":
                    self.button_rect(self.white, 525, 580, 125 ,70)
                    self.texte(30, add_pokemon_attaque, self.black, 525, 580)
                    self.button_rect(self.red, 525, 525, 80 ,30)
                    self.texte(20, "Atq", self.black,525, 525)
                    self.simple_rect(self.black, 525, 525, 80, 30, 3)
                elif add_pokemon_attaque == "":
                    self.button_rect(self.red, 525, 580, 125 ,70)
                    self.texte(20, "Atq", self.black,525, 580)

                if self.cate == 4 and self.select_stat == 3 or add_pokemon_def != "":
                    self.button_rect(self.white, 675, 580, 125 ,70)
                    self.texte(30, add_pokemon_def,self.black, 675, 580)
                    self.button_rect(self.green, 675, 525, 80 ,30)
                    self.texte(20, "Def", self.black,675, 525)
                    self.simple_rect(self.black, 675, 525, 80, 30, 3)


                elif add_pokemon_def == "":
                    self.button_rect(self.green, 675, 580, 125 ,70)
                    self.texte(20, "Def", self.black,675, 580)

                if self.cate == 4:
                    if self.select_stat == 1:
                        self.simple_rect(self.white, 375, 525, 80, 30, 3)
                    if self.select_stat == 2:
                        self.simple_rect(self.white, 525, 525, 80, 30, 3)
                    if self.select_stat == 3:
                        self.simple_rect(self.white, 675, 525, 80, 30, 3)

                self.simple_rect(self.orange, 375, 580, 120, 65, 3)
                self.simple_rect(self.darkred, 525, 580, 120, 65, 3)
                self.simple_rect(self.darkgreen, 675, 580, 120, 65, 3)
                
                if self.cate == 5:
                    self.img(525, 660, 130, 55, "add_pokemon/confirmon")
                else: 
                    self.img(525, 660, 130, 55, "add_pokemon/confirmoff")

                if confirm: 
                    self.button_rect((122, 122, 122), 525, 350, 800, 535)
                    self.img(525, 350, 800, 535, "pokedex/background")
                    self.img(370,365, 255 ,265, f"pokedex/bg.{add_pokemon_type}")
                    self.img(525, 350, 600, 450, "pokedex/pokedex")
                    self.img(375, 370, 250, 250, "pokemon/default")
                    self.img(680, 300, 100, 100, f"pokedex/{add_pokemon_type}")
                    self.texte(16, f"Numero {pokedex.get_last_pokemon_number() +1}", self.black ,375, 255)
                    self.texte(16, f"{add_pokemon_name}", self.black ,680, 370)
                    self.texte(16, f"HP {add_pokemon_hp}", self.black ,680, 410)
                    self.texte(16, f"Atq {add_pokemon_attaque}", self.black ,680, 450)
                    self.texte(16, f"Def {add_pokemon_def}", self.black ,680, 490) 


                if enregistre:
                    self.texte(16, "Pokemon ajoute avec succes dans le fichier pokemon.json", (219, 19, 209), 525, 380)
                    enregistre = False
                    active = False
                    self.clock.tick(240)              
                self.update()