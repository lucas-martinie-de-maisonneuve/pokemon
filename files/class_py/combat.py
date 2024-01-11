import json
import random
from files.class_py.element import Element
from files.class_py.screen import Screen
from files.class_py.type import Type
from files.class_py.menu import Menu
from files.class_py.maps_combat import Maps
from files.class_py.pokedex import Pokedex
import pygame

element = Element()
screen = Screen()
type = Type()
menu = Menu()
maps = Maps()
pokedex = Pokedex()

class Combat:
    def __init__(self) -> None:
        pass
        
    def ouverture_pokemonjson(self):
        with open('pokemon.json', 'r') as fichier:
            self.donnees_pokemon = json.load(fichier)
            return self.donnees_pokemon    
              
    def rand_pokemon(self):
        self.info_pokemon = self.ouverture_pokemonjson()
        self.pokeliste = []
        for pokemon in self.info_pokemon:
            self.pokeliste.append(pokemon)
        self.poke_random = random.choice(self.pokeliste)
        print (self.poke_random)
        
    def info_rand_pokemon(self, data):
        self.info_pokemon = self.ouverture_pokemonjson()
        for pokemon in self.info_pokemon:
            if pokemon['nom'] == self.poke_random['nom']:
                print(pokemon[data])
    
    def afficher_capacite(self):
        self.red = (247, 7, 7)
        self.blue = (0, 8, 255)
        self.green = (35, 247, 7)
        self.yellow = (244, 244, 9)
        self.purple = (207, 7, 247)
        while menu.run :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            cadre_capacite = element.rect(screen.H/3,screen.W,1000,200," ")
            self.button_attack = element.texte(12, "Attack", self.red, cadre_capacite/4, cadre_capacite/2)
            self.button_run = element.texte(12, "Flee", self.green, cadre_capacite/2 - self.button_attack, cadre_capacite /2 - self.button_attack)
            self.button_bag = element.texte(12,"Bag", self.blue, cadre_capacite/4 - self.button_run, cadre_capacite/2 - self.button_attack)
            self.button_pokedex = element.texte(12,"Pokedex", self.yellow, cadre_capacite/4 - self.button_bag, cadre_capacite/2 - self.button_run)        
    
    def fonction_capacites(self):
        click_on_attackDefense = self.button_attack
        click_on_flee = self.button_run
        click_on_bag = self.button_bag
        click_on_pokedex = self.button_pokedex       
        c = 1
        while menu.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    menu.run = False
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_ESCAPE or pygame.K_DELETE:
                        self.show_menu = True
                        self.show_home = False
                        
                    if event.key == pygame.K_RIGHT:
                        if c < 4:
                            c += 1
                    elif event.key == pygame.K_LEFT:
                        if c > 1:
                            c -= 1
                    elif event.key == pygame.K_UP:
                        c = 5
                    elif event.key == pygame.K_DOWN and c == 5:
                        c = 4
                    elif event.key == pygame.K_RETURN:
                        if c == 1:
                            if click_on_attackDefense:
                                maps.home()
                                self.fonction_AttackDefense()
                        elif c == 2:
                            if click_on_flee:
                                maps.home()
                                self.fonction_flee()
                        elif c == 3:
                            if click_on_bag:
                                maps.home()
                                self.fonction_bag()
                        elif c == 4:
                            if click_on_pokedex:
                                pokedex.show_pokedex()
                            
    def fonction_AttackDefense():
        type.feu()
        type.eau()
        type.plante()
        type.elec()
        type.normal()
        type.insecte()
        type.sol()
        type.vol()
        
    def fonction_flee(self):
        while menu.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    menu.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return menu.show_menu            
    
    def fonction_bag(self):
        pass                             
    
    def calcule_combatPrincipal(self):
        pass
    
    def jouer_combat(self):
        pass
    
    def recup_pokemonGagnant(self):
        # mon_pokemon = self.apparition_pokemon()
        # pokemon = self.apparition_pokemon()
        pass
                                                                                      
                   
                               

    




        
    
