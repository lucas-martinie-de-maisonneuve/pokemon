import json
from files.class_py.element import Element
from files.class_py.screen import Screen
from files.class_py.type import Type
from files.class_py.pokedex import Pokedex
import pygame

element = Element()
screen = Screen()
type = Type()
pokedex = Pokedex()

class Combat:
    def __init__(self):
        self.combat = True
        self.info_pokemon = self.ouverture_pokemonjson()
        
    def ouverture_pokemonjson(self):
        with open('pokemon.json', 'r') as fichier:
            self.donnees_pokemon = json.load(fichier)
            return self.donnees_pokemon    
              
    def fonction_AttackDefense():
        type.feu()
        type.eau()
        type.plante()
        type.elec()
        type.normal()
        type.insecte()
        type.sol()
        type.vol()

    def attack(self, vie, pokemon_attack, type_pokemon_starter, type_pokemon_advers):
        
        if type_pokemon_starter == "feu":
            poke_dmg = type.feu(type_pokemon_advers, pokemon_attack)
            vie_restante = vie - poke_dmg
            print (f"Le pokemon inflige {poke_dmg}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
        
        if type_pokemon_starter == "eau":
            damage = type.eau(type_pokemon_advers, pokemon_attack)
            vie_restante = vie - damage
            print (f"Le pokemon inflige {damage}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
        
        if type_pokemon_starter == "plante":
            damage = type.plante(type_pokemon_advers, pokemon_attack)
            vie_restante = vie - damage
            print (f"Le pokemon inflige {damage}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
        
        if type_pokemon_starter == "insecte":
            damage = type.insecte(type_pokemon_advers, pokemon_attack)
            vie_restante = vie - damage
            print (f"Le pokemon inflige {damage}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
        
        if type_pokemon_starter == "sol":
            damage = type.sol(type_pokemon_advers, pokemon_attack)
            vie_restante = vie - damage
            print (f"Le pokemon inflige {damage}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
        
        if type_pokemon_starter == "vol":
            damage = type.vol(type_pokemon_advers, pokemon_attack)
            vie_restante = vie - damage
            print (f"Le pokemon inflige {damage}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
        
        if type_pokemon_starter == "elec":
            damage = type.elec(type_pokemon_advers, pokemon_attack)
            vie_restante = vie - damage
            print (f"Le pokemon inflige {damage}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
        
        if type_pokemon_starter == "normal":
            damage = type.normal(type_pokemon_advers, pokemon_attack)
            vie_restante = vie - damage
            print (f"Le pokemon inflige {damage}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
                

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
    

# pokedex.rand_pokemon()
    
    
    # def fonction_capacites(self):
    #     click_on_attackDefense = self.button_attack
    #     click_on_flee = self.button_run
    #     click_on_bag = self.button_bag
    #     click_on_pokedex = self.button_pokedex       
    #     c = 1
    #     while self.combat:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 self.combat = False
    #             if event.type == pygame.KEYDOWN: 
    #                 if event.key == pygame.K_ESCAPE or pygame.K_DELETE:
    #                     self.show_menu = True                        
    #                 if event.key == pygame.K_RIGHT:
    #                     if c < 4:
    #                         c += 1
    #                 elif event.key == pygame.K_LEFT:
    #                     if c > 1:
    #                         c -= 1
    #                 elif event.key == pygame.K_UP:
    #                     c = 5
    #                 elif event.key == pygame.K_DOWN and c == 5:
    #                     c = 4
    #                 elif event.key == pygame.K_RETURN:
    #                     if c == 1:
    #                         if click_on_attackDefense:
    #                             # maps.home()
    #                             self.fonction_AttackDefense()
    #                     elif c == 2:
    #                         if click_on_flee:
    #                             # maps.home()
    #                             self.fonction_flee()
    #                     elif c == 3:
    #                         if click_on_bag:
    #                             # maps.home()
    #                             self.fonction_bag()
    #                     elif c == 4:
    #                         if click_on_pokedex:
    #                             pokedex.show_pokedex()
                               

    




        
    
