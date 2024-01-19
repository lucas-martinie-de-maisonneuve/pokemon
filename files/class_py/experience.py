class Experience:
    def __init__(self, poke_player):
        self.poke_player = poke_player
        self.exp_winner = 0
        self.exp_max_evol1 = 15
        self.exp_max_evol2 = 60
        self.exp_max_evol3 = 135
        
    def gain_exp(self, level_adv):
        if 1 < level_adv < 5:        
            self.exp_winner =+ 15
            return self.exp_winner
        elif 5 < level_adv == 15:
            self.exp_winner = 25 * level_adv
            return self.exp_winner
        elif 15 < level_adv < 35:
            self.exp_winner =+ 35 * level_adv
            return self.exp_winner
            
    def evolve(self, exp, exp_max, evolve_poke):
        if exp == exp_max:
            if evolve_poke == 1:
                evolve_poke == 2
            elif evolve_poke == 2:
                evolve_poke = 3
        return evolve_poke
                
    def niveau(self):
       pass
    
                      
      
        
        