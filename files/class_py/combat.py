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
        self.poke = pokedex.rand_pokemon()
        self.poke_player = self.poke['nom']
        
    def ouverture_pokemonjson(self):
        with open('pokemon.json', 'r') as fichier:
            self.donnees_pokemon = json.load(fichier)
            return self.donnees_pokemon    
              
    # def fonction_AttackDefense():
    #     type.feu()
    #     type.eau()
    #     type.plante()
    #     type.elec()
    #     type.normal()
    #     type.insecte()
    #     type.sol()
    #     type.vol()

    # def fct_capacite1(self):
    #     self.attack()
    #     self.defense()
        
    # def defense(self, poke_def):
    #     poke_def = (1 - poke_def // 200)
    #     return poke_def
        
    def attack(self, vie, pokemon_attack, type_pokemon_starter, type_pokemon_advers, poke_def):
        
        if type_pokemon_starter == "feu":
            poke_dmg = type.feu(type_pokemon_advers, pokemon_attack)
            dmg_poke = poke_dmg * (1 - poke_def // 200) 
            vie_restante = vie - dmg_poke
            print (f"Le pokemon inflige {dmg_poke} dégats, l'autre avait {vie}HP, il lui reste {vie_restante}HP mais il avait {poke_def}de def")
            return vie_restante
        
        if type_pokemon_starter == "eau":
            poke_dmg = type.eau(type_pokemon_advers, pokemon_attack)
            dmg_poke = poke_dmg * (1 - poke_def // 200) 
            vie_restante = vie - dmg_poke
            print (f"Le pokemon inflige {dmg_poke}, l'autre avait {vie}, il lui reste {vie_restante} mais il avait {poke_def}")
            return vie_restante
        
        if type_pokemon_starter == "plante":
            poke_dmg = type.plante(type_pokemon_advers, pokemon_attack) 
            dmg_poke = poke_dmg * (1 - poke_def // 200) 
            vie_restante = vie - dmg_poke
            print (f"Le pokemon inflige {dmg_poke}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
        
        if type_pokemon_starter == "insecte":
            poke_dmg = type.insecte(type_pokemon_advers, pokemon_attack) 
            dmg_poke = poke_dmg * (1 - poke_def // 200) 
            vie_restante = vie - dmg_poke
            print (f"Le pokemon inflige {dmg_poke}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
        
        if type_pokemon_starter == "sol":
            poke_dmg = type.sol(type_pokemon_advers, pokemon_attack)
            dmg_poke = poke_dmg * (1 - poke_def // 200) 
            vie_restante = vie - dmg_poke 
            print (f"Le pokemon inflige {dmg_poke}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
        
        if type_pokemon_starter == "vol":
            poke_dmg = type.vol(type_pokemon_advers, pokemon_attack)
            dmg_poke = poke_dmg * (1 - poke_def // 200) 
            vie_restante = vie - dmg_poke
            print (f"Le pokemon inflige {dmg_poke}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
        
        if type_pokemon_starter == "elec":
            poke_dmg = type.elec(type_pokemon_advers, pokemon_attack) 
            dmg_poke = poke_dmg * (1 - poke_def // 200) 
            vie_restante = vie - dmg_poke 
            print (f"Le pokemon inflige {dmg_poke}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
        
        if type_pokemon_starter == "normal":
            poke_dmg = type.normal(type_pokemon_advers, pokemon_attack) 
            dmg_poke = poke_dmg * (1 - poke_def // 200) 
            vie_restante = vie - dmg_poke 
            print (f"Le pokemon inflige {dmg_poke}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
        
    def verify_poke_player_HP(self, poke_hp_player):
        return poke_hp_player
    
    def verify_poke_advers_HP(self, poke_hp_advers):
        return poke_hp_advers
    
    def recup_poke_winner(self, poke_player, poke_advers):        
        if self.verify_poke_player_HP < 0:
            print(f"{poke_player} à gagner le combat")
            return poke_player
        elif self.verify_poke_advers_HP < 0:
            print(f"{poke_advers} à gagner le combat")
            return poke_advers
                                                                     
    

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
                               

    




        
    
