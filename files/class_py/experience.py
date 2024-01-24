from files.class_py.pokedex import Pokedex
# import json
pokedex = Pokedex()

class Experience:
    def __init__(self, poke_player):
        self.poke_player = poke_player
        # self.exp_max_poke = 0        
        # self.numero_poke = poke_player["numero"]
        # self.poke_evol = self.numero_poke["numero"]+ 1
        self.exp_poke = 0
        # self.liste_poke = pokedex.info_pokemon
        self.poke_sherch_name = pokedex.rand_pokemon()
        self.pokemons_name = self.poke_sherch_name['nom']
        # self.liste_rencontre_poke = pokedex.pkmn_rencontre   
        
    def exp_par_combat(self, level):
        if level is not None and 1 <= level <= 2:
            exp_poke = 15
                        
        elif level is not None and 3 <= level <= 4:
            exp_poke = 25
            
        elif level is not None and 5 <= level <= 10:
            exp_poke = 30
            
        elif level is not None and 11 <= level <= 20:
            exp_poke = 45
            
        elif level is not None and 21 <= level <= 35:
            exp_poke = 75
            
        elif level is not None and 36 <= level <= 50:
            exp_poke = 125
            
        else:            
            print("j'ai pas reussit a recup level pour faire fonctionner 'exp_par_combat'")
        print(exp_poke)
        print(self.poke_player)
        pokedex.update_exp(self.poke_player['nom'],exp_poke)    
    
    def verif_exp(self, level, exp_poke):
        if exp_poke >= self.exp_max(level):
            pokedex.update_lvl(self.poke_player['nom'],self.exp_max(level))           
    
    def verif_for_evolve(self):
        for info_poke_rencontre in pokedex.pkmn_rencontre:
            for position, poke_player in enumerate(pokedex.info_pokemon):
                if self.poke_player["nom"] == poke_player["nom"]:  
                    if info_poke_rencontre["level"] == 16:
                        next_poke = pokedex.info_pokemon[position + 1]
                        if next_poke["evol"] == 2:
                            self.poke_player = next_poke
                    if info_poke_rencontre["level"] == 36:
                        next_poke = pokedex.info_pokemon[position + 1]
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
        if level is not None:        
            if 1 <= level <= 2 :
                self.exp_max_poke = 15            
            if 3 <= level <= 4:
                self.exp_max_poke = 25
            if 5 <= level <= 10:
                self.exp_max_poke = 30
            if 11 <= level <= 20:
                self.exp_max_poke = 60
            if 21 <= level <= 35:
                self.exp_max_poke = 140
            if 36 <= level <= 50:
                self.exp_max_poke = 290            
            return self.exp_max_poke
        else:
            print("j'ai pas reussit a recup level pour faire fonctionner 'exp_max'")