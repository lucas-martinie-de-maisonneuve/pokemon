class Experience:
    def __init__(self, poke_player):
        self.poke_player = poke_player
        self.exp_poke = 0        
        self.numero_poke = poke_player["numero"]
        self.poke_evol = self.numero_poke["numero"+ 1]       
        
    def exp_par_combat(self, level):    
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
        return self.exp_poke
    
    def verif_exp(self, level):
        if level == self.exp_max():
            level =+ 1 
    
    def verif_for_evolve(self):
        if self.poke_player["level"] == 16:
            if self.poke_evol and self.poke_evol["evol"] == 2:
                self.poke_player = self.poke_evol
        if self.poke_player["level"] == 36:
            if self.poke_evol and self.poke_evol["evol"] == 3:
                self.poke_player = self.poke_evol             
    
    def exp_max(self, level):        
        if 1 <= level <= 2 :
            self.exp_poke = 15            
        if 3 < level < 4:
            self.exp_poke = 25
        if 5 < level < 10:
            self.exp_poke = 30(+5/level)
        if 11 < level < 20:
            self.exp_poke = 60(+5/level)
        if 21 < level < 35:
            self.exp_poke = 140(+8/level)
        if 36 < level < 50:
            self.exp_poke = 290(12/level)            
        return self.exp_poke