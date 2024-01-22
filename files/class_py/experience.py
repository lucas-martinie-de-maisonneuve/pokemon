class Experience:
    def __init__(self, poke_player):
        self.poke_player = poke_player
        self.exp_winner = 0
        self.barre_expMax = 0
        self.levels = 1 
        
    def exp_par_combat(self, evolve):
    
        if evolve == 1:        
            self.exp_winner =+ 15
            return self.exp_winner
        elif evolve == 2:
            self.exp_winner =+ 30
            return self.exp_winner
        elif evolve == 3:
            self.exp_winner =+ 45
            return self.exp_winner
        
    
    def exp_needed(self):        
        if 1 < self.levels < 2 :
            self.barre_expMax = 15
            
        if 3 < self.levels < 4:
            self.barre_expMax = 25

        if 5 < self.levels < 10:
            self.barre_expMax = 30(+5/self.levels)

        if 11 < self.levels < 20:
            self.barre_expMax = 60(+5/self.levels)

        if 21 < self.levels < 35:
            self.barre_expMax = 140(+8/self.levels)

        if 36 < self.levels < 50:
            self.barre_expMax = 290(12/self.levels)
            
        return self.barre_expMax
        
experience = Experience()

         
            
            
    # def evolve(self, exp, exp_max, evolve_poke):
    #     if exp == exp_max:
    #         if evolve_poke == 1:
    #             evolve_poke == 2
    #         elif evolve_poke == 2:
    #             evolve_poke = 3
    #     return evolve_poke
                
    # def levels(self):
    #     nb_lvl = ["1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,5,46,47,48,49,50"]
    #     return nb_lvl
        
        
    
                      
      
        
        