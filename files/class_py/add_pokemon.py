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
            self.cate = 1
            enregistre = False
            add_pokemon_name = ""
            add_pokemon_level = 1
            add_pokemon_type = 4
            add_pokemon_attaque = ""
            add_pokemon_hp = ""
            add_pokemon_def = ""
            active = True

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
                            if self.cate > 0:
                                self.cate -= 1
                        elif event.key == pygame.K_RETURN and self.cate == 5:
                            data_pokemon = pokedex.ouverture_pokemonjson()
                            nouveau_pokemon = {
                                "numero": (pokedex.get_last_pokemon_number() +1),
                                "nom": add_pokemon_name,
                                "evol": add_pokemon_level,
                                "type": add_pokemon_type,
                                "attaque": add_pokemon_attaque,
                                "hp": add_pokemon_hp,
                                "def": add_pokemon_def,
                                "rencontre": 1,
                            }
                            data_pokemon.append(nouveau_pokemon)

                            with open("pokemon.json", "w") as fichier:
                                json.dump(data_pokemon, fichier)
                            enregistre = True               
                        elif event.key == pygame.K_BACKSPACE:
                            add_pokemon_name = add_pokemon_name[:-1]
                        else:
                            if self.cate == 1:
                                add_pokemon_name += event.unicode
                            
                            
                self.img(525, 350, 1050, 743, "img_ajout_pokemon/test_img")
                self.texte(25, "Saisir les informations du Pokemon :", self.white, 525, 50)

                self.texte(20, "Nom :", self.black,525, 120)
                self.button_rect(self.white, 525, 180, 500 ,70)
                self.simple_rect(self.black, 525, 180, 500, 70, 3)
                self.texte(30, add_pokemon_name, self.black, 525, 180)

                self.texte(20, "Niveau Evol :", self.black,525, 260)
                self.button_rect(self.white, 525, 320, 500 ,70)
                self.simple_rect(self.black, 525, 320, 500, 70, 3)

                if self.cate == 1:
                    self.img(100, 180, 60, 60, "combat/arrow")
                elif self.cate == 2:
                    self.img(100, 320, 60, 60, "combat/arrow")
                elif self.cate == 3:
                    self.img(100, 550, 60, 60, "combat/arrow")
                    

                if enregistre:
                    self.texte(16, "Pokemon ajoute avec succes dans le fichier pokemon.json", (219, 19, 209), 525, 380)
                    enregistre = False
                    active = False
                    self.clock.tick(240)              
                self.update()