import pygame
from files.class_py.screen import Screen
from files.class_py.element import Element
from files.class_py.pokedex import Pokedex
from files.class_py.maps_combat import Maps
from files.class_py.combat import Combat
from files.class_py.starter import Starter

element = Element()
screen = Screen()
pokedex = Pokedex()
combat = Combat()
starter = Starter()

class Menu:
    def __init__(self):
        self.menu_run = True
        self.show_home = True

    def home(self):
        c = 1
        while self.menu_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if self.show_home:
                        self.show_home = False
                        break
                    if event.key == pygame.K_RIGHT:
                        if c < 4:
                            c += 1
                    elif event.key == pygame.K_LEFT:
                        if c > 1:
                            c -= 1
                    elif event.key == pygame.K_UP:
                        c = 5
                    elif event.key == pygame.K_DOWN:
                        c = 4
                    elif event.key == pygame.K_RETURN:
                        if c == 1:
                            if starter.poke_player == "":
                                starter.choose_starter = True
                                starter.starter()
                            else:
                                pokemon_random = pokedex.rand_pokemon()                           
                                
                                maps = Maps(starter.poke_player,pokemon_random)
                                maps.home()
                                maps.combat_run = True
                                pokedex.pokemon_rencontre(pokemon_random["nom"])
                                print (pokedex.pokemon_counter)
                        elif c == 2:
                            pokedex.pokedex_run = True
                            pokedex.show_pokedex()
                        elif c == 4:
                            pokedex.ajout_pokemon()
                            pass
            if self.show_home:
                element.img_background(525, 350, 1244, 700, 'background')
                element.img(1000, 650, 70, 70,'pokeball')
                element.img_mir(50, 50, 70,70,'pokeball')
                element.texte(30, 'Appuyer sur une touche pour continuer', (255, 255, 255), screen.W // 2, screen.H // 2)
                screen.update()

            if not self.show_home:      
                element.img(525, 350, 1244, 700, 'menu/backgroundmenu')
                if starter.poke_player != "":
                    element.img(525, 250, 400, 400, f'pokemon/{starter.poke_player["nom"].lower()}')

                if c == 1 : 
                    element.img(200, 550, 120, 120, 'menu/play')
                    element.texte(20,'Play',(255,255,255),200,630)
                else:
                    element.img(200, 550, 100, 100, 'menu/play')
                    element.texte(16,'Play',(0,0,0),200,620)
                if c == 2:
                    element.img(400, 550, 120, 120, 'menu/pokedex')
                    element.texte(20,'Pokedex',(255,255,255),400,630)
                else:
                    element.img(400, 550, 100, 100, 'menu/pokedex')
                    element.texte(16,'Pokedex',(0,0,0),400,620)
                if c == 3:
                    element.img(600, 550, 120, 120, 'menu/bag')
                    element.texte(20,'Bag',(255,255,255),600,630)
                else: 
                    element.img(600, 550, 100, 100, 'menu/bag')
                    element.texte(16,'Bag',(0,0,0),600,620)
                if c == 4:                 
                    element.img(800, 550, 120, 120, 'menu/add_poke')
                    element.texte(20,'Add Pokemon',(255,255,255),800,630)
                else:
                    element.img(800, 550, 100, 100, 'menu/add_poke')
                    element.texte(16,'Add Pokemon',(0,0,0),800,620)
                if c == 5:
                    element.img(990, 60, 100, 100, 'menu/settings')
                    element.texte(17,'Settings',(255,255,255),990,120)
                else:
                    element.img(990, 60, 80, 80, 'menu/settings')
                    element.texte(14,'Settings',(0,0,0),990,110)
                screen.update()
