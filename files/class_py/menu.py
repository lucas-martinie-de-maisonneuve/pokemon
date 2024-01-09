import pygame
from files.class_py.screen import Screen
from files.class_py.element import Element

class Menu:
    def __init__(self):
        self.run = True

    def home(self):
        element = Element()
        screen = Screen()
        # pokemon_liste = ["salameche", "reptincelle", "dracaufeu", "bulbizarre", "herbizarre", "florizarre", "carapuce", "carabaffe", "tortank", "pikachu", "raichu", "chenipotte", "blindalys", "papinox", "canarticho", "racaillou", "gravalanch", "grolem", "evoli", "aquali", "voltali", "pyroli", "phyllali", "tauros", "kangourex", "elektek", "magmar", "scarabrute", "magicarpe", "leviator", "grainipiot", "pifeuil", "tengalice", "roucool", "roucoups", "roucarnage", "goupix", "fenard", "sabelette", "sablaireau", "osselait", "ossatueur", "insecateur", "magneti", "artikodin", "electhor", "sulfura", "kyogre", "groudon", "rayquaza"]
        # img_poke = random.choice(pokemon_liste)
        # screen.img    (50, 150, 150, 150, f'pokemon/{img_poke}')
        while self.run :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            element.img_background(525, 350, 1244, 700, f'background')
            i = 30
            if i < 35:
                element.texte(i, 'Appuyer sur une touche pour continuer',(255, 255, 255), screen.W//2, screen.H//2)
                i+=1
                pygame.time.delay(100)
                screen.update()