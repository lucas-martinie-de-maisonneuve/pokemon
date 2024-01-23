from files.class_py.pokedex import Pokedex
import json
pokedex = Pokedex()

class Experience:
    def __init__(self, poke_player):
        self.poke_player = poke_player
        # self.exp_max_poke = 0        
        # self.numero_poke = poke_player["numero"]
        # self.poke_evol = self.numero_poke["numero"]+ 1
        self.liste_poke = pokedex.info_pokemon
        self.liste_rencontre_poke = pokedex.pkmn_rencontre
    
    def recup_level(self):
        for info_poke_rencontre in self.liste_rencontre_poke:
            for pokemon in self.liste_poke: 
                if info_poke_rencontre["nom"] == pokemon["nom"]:
                    poke_lvl = info_poke_rencontre["level"]
                    return poke_lvl                   
        
    def exp_par_combat(self, level):
        # self.exp_poke = 0    
        if 1 <= level <= 2 :
            self.exp_poke =+ 15            
        if 3 < level < 4:
            self.exp_poke =+ 25
        if 5 < level < 10:
            self.exp_poke =+ 30
        if 11 < level < 20:
            self.exp_poke =+ 45
        if 21 < level < 35:
            self.exp_poke =+ 75
        if 36 < level < 50:
            self.exp_poke =+ 125
            
        self.liste_rencontre_poke.append({"level": self.exp_poke})          
        
        with open('rencontre.json', 'w') as file:
            json.dump(self.liste_rencontre_poke, file, indent=2)
    
    def verif_exp(self, level):
        if level == self.exp_max(level):
            level =+ 1 
    
    def verif_for_evolve(self):
        for info_poke_rencontre in self.liste_rencontre_poke:
            for position, poke_player in enumerate(self.liste_poke):
                if self.poke_player["nom"] == poke_player["nom"]:  
                    if info_poke_rencontre["level"] == 16:
                        next_poke = self.liste_poke[position + 1]
                        if next_poke["evol"] == 2:
                            self.poke_player = next_poke
                    if info_poke_rencontre["level"] == 36:
                        next_poke = self.liste_poke[position + 1]
                        if next_poke["evol"] == 3:
                            self.poke_player = next_poke
     
                     
        # if self.poke_player["level"] == 16:
        #     if self.poke_evol and self.poke_evol["evol"] == 2:
        #         self.poke_player = self.poke_evol
        #         print(self.poke_evol)
        # if self.poke_player["level"] == 36:
        #     if self.poke_evol and self.poke_evol["evol"] == 3:
        #         self.poke_player = self.poke_evol
        #         print(self.poke_evol)             
    
    def exp_max(self, level):        
        if 1 <= level <= 2 :
            self.exp_max_poke = 15            
        if 3 < level < 4:
            self.exp_max_poke = 25
        if 5 < level < 10:
            self.exp_max_poke = 30
        if 11 < level < 20:
            self.exp_max_poke = 60
        if 21 < level < 35:
            self.exp_max_poke = 140
        if 36 < level < 50:
            self.exp_max_poke = 290            
        return self.exp_max_poke