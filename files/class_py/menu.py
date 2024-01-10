import pygame
from files.class_py.screen import Screen
from files.class_py.element import Element

element = Element()
screen = Screen()

class Menu:
    def __init__(self):
        self.run = True
        self.show_menu = False
        self.show_home = True

    def home(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    self.show_menu = True
                    self.show_home = False
            if self.show_home:
                element.img_background(525, 350, 1244, 700, 'background')
                element.img(1000, 650, 70, 70,'pokeball')
                element.img_mir(50, 50, 70,70,'pokeball')
                element.texte(30, 'Appuyer sur une touche pour continuer', (255, 255, 255), screen.W // 2, screen.H // 2)
                screen.update()

            if self.show_menu:      
                element.img(525, 350, 1244, 700, 'menu/backgroundmenu')
                element.img(200, 550, 100, 100, 'menu/play')
                element.img(400, 550, 100, 100, 'menu/pokedex')
                element.img(600, 550, 100, 100, 'menu/bag')
                element.img(800, 550, 100, 100, 'menu/add_poke')
                screen.update()
                print(self.show_menu)
