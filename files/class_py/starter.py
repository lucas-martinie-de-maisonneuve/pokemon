import pygame
from files.class_py.pokedex import Pokedex
from files.class_py.element import Element
from files.class_py.screen import Screen

pygame.font.init()

class Starter(Element, Screen):
    def __init__(self):
        Screen.__init__(self)
        Element.__init__(self)
        self.pokedex = Pokedex()
        self.action = 1
        self.poke_player = ""
        self.choose_starter = False

    def starter(self):
        while self.choose_starter:
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
                    elif event.key == pygame.K_RETURN:
                        if self.action == 1:
                            self.poke_player = self.pokedex.starter()[0]
                            self.choose_starter = False
                            return self.poke_player
                        elif self.action == 2:
                            self.poke_player = self.pokedex.starter()[1]
                            self.choose_starter = False
                            return self.poke_player                        
                        elif self.action == 3:
                            self.poke_player = self.pokedex.starter()[2]
                            self.choose_starter = False
                            return self.poke_player
                        elif self.action == 4:
                            self.poke_player = self.pokedex.starter()[3]
                            self.choose_starter = False
                            return self.poke_player
                                                
            self.img_background(525, 350, 1050, 700, "starter/starterbg")
            self.texte(30, "Choisissez un Pokémon", self.white, 525, 220)
            self.img(160, 435, 180, 180, f"pokemon/{self.pokedex.starter()[0]['nom'].lower()}")
            self.img(400, 435, 180, 180, f"pokemon/{self.pokedex.starter()[1]['nom'].lower()}")
            self.img(620, 435, 180, 180, f"pokemon/{self.pokedex.starter()[2]['nom'].lower()}")
            self.img(900, 435, 180, 180, f"pokemon/{self.pokedex.starter()[3]['nom'].lower()}")

            if self.action == 1:
                self.img(160, 570, 130, 130, "starter/pokeball")
            else:
                self.img(160, 570, 110, 110, "starter/pokeball")

            if self.action == 2:
                self.img(400, 570, 130, 130, "starter/pokeball")
            else:
                self.img(400, 570, 110, 110, "starter/pokeball")

            if self.action == 3:
                self.img(620, 570, 130, 130, "starter/pokeball")
            else:
                self.img(620, 570, 110, 110, "starter/pokeball")

            if self.action == 4:
                self.img(880, 570, 130, 130, "starter/pokeball")
            else:
                self.img(880, 570, 110, 110, "starter/pokeball")
                
            self.update()
            