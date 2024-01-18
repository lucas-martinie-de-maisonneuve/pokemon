from files.class_py.pokedex import Pokedex
pokedex = Pokedex()

class Type:
    def __init__(self) -> None:
        pass
    
    def normal(self,type,damage):        
        if type:
            print(type)
            print(damage)
            return damage                        
                
    def feu(self,type,damage):
        if type == "feu" or type == "eau":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "plante" or type == "insecte":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "elec" or type == "sol" or type == "vol":
            damage = damage
            print(damage)
            print(type)
            return damage
        
    def eau(self,type,damage):        
        if type == "feu" or type == "sol":
            damage = damage * 2
            print(type)
            print(damage)
            return damage
            
        elif type == "eau" or type == "plante":
            damage = damage // 2
            print(type)
            print(damage)
            return damage
            
        elif type == "normal" or type == "elec" or type == "insecte" or type == "vol":
            damage = damage
            print(type)
            print(damage)
            return damage
        
    def plante(self,type,damage):
        if type == "feu" or type == "plante" or type == "vol" or type == "insecte":
            damage = damage // 2
            print(type)
            print(damage)
            return damage
            
        elif type == "eau" or type == "sol":
            damage = damage * 2
            print(type)
            print(damage)
            return damage
            
        elif type == "normal" or type == "elec":
            damage = damage
            print(type)
            print(damage)
            return damage
        
    def elec(self,type,damage):
        if type == "plante" or type == "elec":
            damage = damage // 2
            print(type)
            print(damage)
            return damage
            
        elif type == "eau" or type == "vol":
            damage = damage * 2
            print(type)
            print(damage)
            return damage
            
        elif type == "normal" or type == "feu" or type == "sol" or type == "insecte":
            damage = damage
            print(type)
            print(damage)
            return damage
        
    def sol(self,type,damage):
        if type == "plante" or type ==  "insecte":
            damage = damage // 2
            print(type)
            print(damage)
            return damage
        
        elif type == "feu" or type == "elec":
            damage = damage * 2
            print(type)
            print(damage)
            return damage
            
        elif type == "normal" or type == "eau" or type == "sol" or type == "vol":
            damage = damage
            print(type)
            print(damage)
            return damage
        
    def vol(self,type,damage):
        if type == "elec":
            damage = damage // 2
            print(type)
            print(damage)
            return damage
        
        elif type == "plante" or type == "insecte":
            damage = damage * 2
            print(type)
            print(damage)
            return damage
        
        elif type == "normal" or type == "feu" or type == "eau" or type == "sol" or type == "vol":
            damage = damage
            print(type)
            print(damage)
            return damage
        
    def insecte(self,type,damage):
        if type == "feu" or type ==  "vol":
            damage = damage // 2
            print(type)
            print(damage)
            return damage
            
        elif type == "plante":
            damage = damage * 2
            print(type)
            print(damage)
            return damage
            
        elif type == "normal" or type == type == "eau" or type == "elec" or type == "sol" or type == "insecte":
            damage = damage
            print(type)
            print(damage)
            return damage
        
    #     #Defend
    #     for type in self.type_pokemon:
    #         if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
    #             damage == self.data_defend/2
                
    #         elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
    #             damage == self.data_defend*2
                
    #         elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
    #             damage == self.data_defend                                       
    
    # def eau(self,type,damage,player):
    #     #Attack        
    #     self.type_pokemon = pokedex.rand_pokemon("type")
    #     for type in self.type_pokemon:
    #         if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
    #             damage == self.data_damage/2
                
    #         elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
    #             damage == self.data_damage*2
                
    #         elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
    #             damage == self.data_damage
    #     #Defend
    #     for type in self.type_pokemon:
    #         if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
    #             damage == self.data_defend/2
                
    #         elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
    #             damage == self.data_defend*2
                
    #         elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
    #             damage == self.data_defend
    
    # def plante(self,type,damage,player):
    #     #Attack        
    #     self.type_pokemon = pokedex.rand_pokemon("type")
    #     for type in self.type_pokemon:
    #         if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
    #             damage == self.data_damage/2
                
    #         elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
    #             damage == self.data_damage*2
                
    #         elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
    #             damage == self.data_damage
    #     #Defend
    #     for type in self.type_pokemon:
    #         if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
    #             damage == self.data_defend/2
                
    #         elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
    #             damage == self.data_defend*2
                
    #         elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
    #             damage == self.data_defend
    
    # def elec(self,type,damage,player):
    #     #Attack        
    #     self.type_pokemon = pokedex.info_pokemon
    #     for type in self.type_pokemon:
    #         if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
    #             damage == self.data_damage/2
                
    #         elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
    #             damage == self.data_damage*2
                
    #         elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
    #             damage == self.data_damage
    #     #Defend
    #     for type in self.type_pokemon:
    #         if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
    #             damage == self.data_defend/2
                
    #         elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
    #             damage == self.data_defend*2
                
    #         elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
    #             damage == self.data_defend
    
    # def normal(self,type,damage,player):
    #     #Attack        
    #     self.type_pokemon = pokedex.rand_pokemon("type")
    #     for type in self.type_pokemon:
    #         if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
    #             damage == self.data_damage/2
                
    #         elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
    #             damage == self.data_damage*2
                
    #         elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
    #             damage == self.data_damage
    #     #Defend
    #     for type in self.type_pokemon:
    #         if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
    #             damage == self.data_defend/2
                
    #         elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
    #             damage == self.data_defend*2
                
    #         elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
    #             damage == self.data_defend
    
    # def insecte(self,type,damage,player):
    #     #Attack        
    #     self.type_pokemon = pokedex.rand_pokemon("type")
    #     for type in self.type_pokemon:
    #         if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
    #             damage == self.data_damage/2
                
    #         elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
    #             damage == self.data_damage*2
                
    #         elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
    #             damage == self.data_damage
    #     #Defend
    #     for type in self.type_pokemon:
    #         if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
    #             damage == self.data_defend/2
                
    #         elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
    #             damage == self.data_defend*2
                
    #         elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
    #             damage == self.data_defend
    
    # def sol(self,type,damage,player):
    #     #Attack        
    #     self.type_pokemon = pokedex.rand_pokemon("type")
    #     for type in self.type_pokemon:
    #         if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
    #             damage == self.data_damage/2
                
    #         elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
    #             damage == self.data_damage*2
                
    #         elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
    #             damage == self.data_damage
    #     #Defend
    #     for type in self.type_pokemon:
    #         if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
    #             damage == self.data_defend/2
                
    #         elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
    #             damage == self.data_defend*2
                
    #         elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
    #             damage == self.data_defend
    
    # def vol(self,type,damage,player):
    #     #Attack        
    #     self.type_pokemon = pokedex.rand_pokemon("type")
    #     for type in self.type_pokemon:
    #         if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
    #             damage == self.data_damage/2
                
    #         elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
    #             damage == self.data_damage*2
                
    #         elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
    #             damage == self.data_damage
    #     #Defend
    #     for type in self.type_pokemon:
    #         if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
    #             damage == self.data_defend/2
                
    #         elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
    #             damage == self.data_defend*2
                
    #         elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
    #             damage == self.data_defend
    
    