import json
import random
from files.class_py.element import Element
from files.class_py.screen import Screen
import pygame

element = Element()
screen = Screen()

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
        cadre_capacite = element.rect(screen.H/3,screen.W,1000,200," ")
        self.button_attack = element.texte(12, "Attack", self.red, cadre_capacite/4, cadre_capacite/2)
        self.button_run = element.texte(12, "Run", self.green, cadre_capacite/2 - self.button_attack, cadre_capacite /2 - self.button_attack)
        self.button_bag = element.texte(12,"Bag", self.blue, cadre_capacite/4 - self.button_run, cadre_capacite/2 - self.button_attack)
        self.button_pokedex = element.texte(12,"Pokedex", self.yellow, cadre_capacite/4 - self.button_bag, cadre_capacite/2 - self.button_run)        
    
    def capacites(self):
        click_on_attack = self.button_attack
        click_on_run = self.button_run
        click_on_bag = self.button_bag
        click_on_pokedex = self.button_pokedex        
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        running = False 
                elif event.type == pygame.KEYDOWN:                                                                
                    if event.button == 1:
                        if click_on_attack:
                            self.fonction_attack()
                            pass
                        elif click_on_run:
                            self.fonction_run() 
                            pass
                        elif click_on_bag:
                            self.fonction_bag()
                            pass
                        elif click_on_pokedex:
                            self.ouvrir_pokedex()
                            pass    

    def fonction_attack(self,sort1):        
        self.damage_sort1 = sort1        
        # type_attack = self.recuperer_typeAdvers()
        pass
            
    def fonction_defense(self):
        pass
    
    def fonction_run(self):
        pass
    
    def fonction_bag(self):
        pass
    
    def ouvrir_pokedex(self):
        pass                            
    
    def calcule_combatPrincipal(self):
        pass
    
    def jouer_combat(self):
        pass
    
    def recup_pokemonGagnant(self):
        # mon_pokemon = self.apparition_pokemon()
        # pokemon = self.apparition_pokemon()
        pass
    
combat = Combat()



        
    
