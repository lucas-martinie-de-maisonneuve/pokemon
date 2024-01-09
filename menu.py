import pygame
from screen import Screen

class Menu:
    def __init__(self):
        self.run = True

    def menu_open(self):
        screen = Screen()
        while self.run :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            screen.update()
            screen.img(180, 180, 'pokemon/pika', 500, 350)
