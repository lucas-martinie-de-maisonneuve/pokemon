import json
from files.class_py.element import Element
from files.class_py.screen import Screen
from files.class_py.type import Type
from files.class_py.pokedex import Pokedex
# import pygame

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
        self.game_over = False
        self.win = ""       
        
    def ouverture_pokemonjson(self):
        with open('pokemon.json', 'r') as fichier:
            self.donnees_pokemon = json.load(fichier)
            return self.donnees_pokemon               
    
    def attack(self, vie, pokemon_attack, type_pokemon_starter, type_pokemon_advers, poke_def):
        
        if type_pokemon_starter == "feu":
            poke_dmg = type.feu(type_pokemon_advers, pokemon_attack)
            self.dmg_poke = poke_dmg * (1 - poke_def / 200) 
            vie_restante = vie - self.dmg_poke
            print (f"Le pokemon inflige {self.dmg_poke} dégats, l'autre avait {vie}HP, il lui reste {vie_restante}HP mais il avait {poke_def}de def")
            return vie_restante
        
        if type_pokemon_starter == "eau":
            poke_dmg = type.eau(type_pokemon_advers, pokemon_attack)
            self.dmg_poke = poke_dmg * (1 - poke_def / 200) 
            vie_restante = vie - self.dmg_poke
            print (f"Le pokemon inflige {self.dmg_poke}, l'autre avait {vie}, il lui reste {vie_restante} mais il avait {poke_def}")
            return vie_restante
        
        if type_pokemon_starter == "plante":
            poke_dmg = type.plante(type_pokemon_advers, pokemon_attack) 
            self.dmg_poke = poke_dmg * (1 - poke_def / 200) 
            vie_restante = vie - self.dmg_poke
            print (f"Le pokemon inflige {self.dmg_poke}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
        
        if type_pokemon_starter == "insecte":
            poke_dmg = type.insecte(type_pokemon_advers, pokemon_attack) 
            self.dmg_poke = poke_dmg * (1 - poke_def / 200) 
            vie_restante = vie - self.dmg_poke
            print (f"Le pokemon inflige {self.dmg_poke}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
        
        if type_pokemon_starter == "sol":
            poke_dmg = type.sol(type_pokemon_advers, pokemon_attack)
            self.dmg_poke = poke_dmg * (1 - poke_def / 200) 
            vie_restante = vie - self.dmg_poke 
            print (f"Le pokemon inflige {self.dmg_poke}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
        
        if type_pokemon_starter == "vol":
            poke_dmg = type.vol(type_pokemon_advers, pokemon_attack)
            self.dmg_poke = poke_dmg * (1 - poke_def / 200) 
            vie_restante = vie - self.dmg_poke
            print (f"Le pokemon inflige {self.dmg_poke}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
        
        if type_pokemon_starter == "elec":
            poke_dmg = type.elec(type_pokemon_advers, pokemon_attack) 
            self.dmg_poke = poke_dmg * (1 - poke_def / 200) 
            vie_restante = vie - self.dmg_poke 
            print (f"Le pokemon inflige {self.dmg_poke}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante
        
        if type_pokemon_starter == "normal":
            poke_dmg = type.normal(type_pokemon_advers, pokemon_attack) 
            self.dmg_poke = poke_dmg * (1 - poke_def / 200) 
            vie_restante = vie - self.dmg_poke 
            print (f"Le pokemon inflige {self.dmg_poke}, l'autre avait {vie}, il lui reste {vie_restante}")
            return vie_restante   
    
    def recup_poke_winner(self, poke_player, poke_advers, poke_player_hp, poke_rand_hp):
        print("player",poke_player_hp)
        print(poke_rand_hp)       
        if poke_player_hp <= 0:
            self.game_over = True
            print(f"{poke_advers} à gagner le combat")            
            self.win = poke_advers            
        elif poke_rand_hp <= 0:
            self.game_over = True
            print(f"{poke_player} à gagner le combat")
            print(poke_rand_hp)
            print(f"player{poke_player_hp}")
            self.win = poke_player
            
        return self.win