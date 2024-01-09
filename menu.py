import pygame
from screen import Screen

class Menu:
    def __init__(self):
        self.run = True

    def menu_open(self):
        while self.run :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            screen = Screen()
            screen.update()
            screen.img(80, 80, 'pokemon/pika', 500, 350)
