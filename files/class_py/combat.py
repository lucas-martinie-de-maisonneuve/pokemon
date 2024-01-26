from files.class_py.type import Type
# from files.class_py.experience import Experience
from files.class_py.element import Element
# from config import confirmation_sound, current_volume, volume_levels
import random

type = Type()

class Combat:
    def __init__(self):
        self.element = Element()
        self.combat = True       
        self.game_over = False
        self.win = ""
        # Experience.__init__(self)       
        
    def attack(self, vie, pokemon_attack, type_pokemon_starter, type_pokemon_advers, poke_def):
        
        if self.miss_attack(15):
            return vie
        if type_pokemon_starter == "feu":
            poke_dmg = type.feu(type_pokemon_advers, pokemon_attack)
            self.dmg_poke = round(poke_dmg * (1 - poke_def / 200)) 
            vie_restante = vie - self.dmg_poke
            return vie_restante
        
        if type_pokemon_starter == "eau":
            poke_dmg = type.eau(type_pokemon_advers, pokemon_attack)
            self.dmg_poke = round(poke_dmg * (1 - poke_def / 200)) 
            vie_restante = vie - self.dmg_poke
            return vie_restante
        
        if type_pokemon_starter == "plante":
            poke_dmg = type.plante(type_pokemon_advers, pokemon_attack) 
            self.dmg_poke = round(poke_dmg * (1 - poke_def / 200)) 
            vie_restante = vie - self.dmg_poke
            return vie_restante
        
        if type_pokemon_starter == "insecte":
            poke_dmg = type.insecte(type_pokemon_advers, pokemon_attack) 
            self.dmg_poke = round(poke_dmg * (1 - poke_def / 200)) 
            vie_restante = vie - self.dmg_poke
            return vie_restante
        
        if type_pokemon_starter == "sol":
            poke_dmg = type.sol(type_pokemon_advers, pokemon_attack)
            self.dmg_poke = round(poke_dmg * (1 - poke_def / 200)) 
            vie_restante = vie - self.dmg_poke 
            return vie_restante
        
        if type_pokemon_starter == "vol":
            poke_dmg = type.vol(type_pokemon_advers, pokemon_attack)
            self.dmg_poke = round(poke_dmg * (1 - poke_def / 200)) 
            vie_restante = vie - self.dmg_poke
            return vie_restante
        
        if type_pokemon_starter == "elec":
            poke_dmg = type.elec(type_pokemon_advers, pokemon_attack) 
            self.dmg_poke = round(poke_dmg * (1 - poke_def / 200)) 
            vie_restante = vie - self.dmg_poke 
            return vie_restante
        
        if type_pokemon_starter == "normal":
            poke_dmg = type.normal(type_pokemon_advers, pokemon_attack) 
            self.dmg_poke = round(poke_dmg * (1 - poke_def / 200)) 
            vie_restante = vie - self.dmg_poke 
            return vie_restante
        
        if type_pokemon_starter == "eau.vol":
            poke_dmg = type.eauvol(type_pokemon_advers, pokemon_attack) 
            self.dmg_poke = poke_dmg * (1 - poke_def / 200) 
            vie_restante = vie - self.dmg_poke 
            return vie_restante
        
        if type_pokemon_starter == "feu.vol":
            poke_dmg = type.feuvol(type_pokemon_advers, pokemon_attack) 
            self.dmg_poke = poke_dmg * (1 - poke_def / 200) 
            vie_restante = vie - self.dmg_poke 
            return vie_restante
        
        if type_pokemon_starter == "elec.vol":
            poke_dmg = type.elecvol(type_pokemon_advers, pokemon_attack) 
            self.dmg_poke = poke_dmg * (1 - poke_def / 200) 
            vie_restante = vie - self.dmg_poke 
            return vie_restante

    def recup_poke_winner(self, poke_player, poke_advers, poke_player_hp, poke_rand_hp):     
        if poke_player_hp <= 0:
            self.game_over = True
            self.win = poke_advers   
            self.element.win_song_play = True
        elif poke_rand_hp <= 0:
            self.game_over = True
            self.win = poke_player 
            self.element.win_song_play = True           
        return self.win
    
    def miss_attack(self, chance_to_miss):
# Vérifie si l'attaque rate en fonction d'un pourcentage donné.
# Parameters:
#  chance_to_miss (float): Pourcentage de chance de rater l'attaque.
# Returns:
#  bool: True si l'attaque rate, False sinon.
        return random.random() < chance_to_miss / 100.0