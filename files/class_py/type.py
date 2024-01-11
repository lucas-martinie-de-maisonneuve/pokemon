from files.class_py.pokedex import Pokedex
pokedex = Pokedex()

class Type:
    def __init__(self,degats,reduction_degats,coup_critique) -> None:
        self.degats = degats
        self.reduction = reduction_degats
        self.coup_critique = coup_critique #En pourcentage
        self.data_damage = pokedex.information_pokemon("attaque")
        self.data_defend = pokedex.information_pokemon("defense")                 
        
    def feu(self,type,damage,player):
        #Attack
        self.type_pokemon = pokedex.information_pokemon("type")
        for type in self.type_pokemon:
            if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
                damage == self.data_damage/2
                
            elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
                damage == self.data_damage*2
                
            elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
                damage == self.data_damage
        #Defend
        for type in self.type_pokemon:
            if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
                damage == self.data_defend/2
                
            elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
                damage == self.data_defend*2
                
            elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
                damage == self.data_defend                                       
    
    def eau(self,type,damage,player):
        #Attack        
        self.type_pokemon = pokedex.information_pokemon("type")
        for type in self.type_pokemon:
            if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
                damage == self.data_damage/2
                
            elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
                damage == self.data_damage*2
                
            elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
                damage == self.data_damage
        #Defend
        for type in self.type_pokemon:
            if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
                damage == self.data_defend/2
                
            elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
                damage == self.data_defend*2
                
            elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
                damage == self.data_defend
    
    def plante(self,type,damage,player):
        #Attack        
        self.type_pokemon = pokedex.information_pokemon("type")
        for type in self.type_pokemon:
            if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
                damage == self.data_damage/2
                
            elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
                damage == self.data_damage*2
                
            elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
                damage == self.data_damage
        #Defend
        for type in self.type_pokemon:
            if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
                damage == self.data_defend/2
                
            elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
                damage == self.data_defend*2
                
            elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
                damage == self.data_defend
    
    def elec(self,type,damage,player):
        #Attack        
        self.type_pokemon = pokedex.information_pokemon("type")
        for type in self.type_pokemon:
            if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
                damage == self.data_damage/2
                
            elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
                damage == self.data_damage*2
                
            elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
                damage == self.data_damage
        #Defend
        for type in self.type_pokemon:
            if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
                damage == self.data_defend/2
                
            elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
                damage == self.data_defend*2
                
            elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
                damage == self.data_defend
    
    def normal(self,type,damage,player):
        #Attack        
        self.type_pokemon = pokedex.information_pokemon("type")
        for type in self.type_pokemon:
            if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
                damage == self.data_damage/2
                
            elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
                damage == self.data_damage*2
                
            elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
                damage == self.data_damage
        #Defend
        for type in self.type_pokemon:
            if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
                damage == self.data_defend/2
                
            elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
                damage == self.data_defend*2
                
            elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
                damage == self.data_defend
    
    def insecte(self,type,damage,player):
        #Attack        
        self.type_pokemon = pokedex.information_pokemon("type")
        for type in self.type_pokemon:
            if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
                damage == self.data_damage/2
                
            elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
                damage == self.data_damage*2
                
            elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
                damage == self.data_damage
        #Defend
        for type in self.type_pokemon:
            if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
                damage == self.data_defend/2
                
            elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
                damage == self.data_defend*2
                
            elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
                damage == self.data_defend
    
    def sol(self,type,damage,player):
        #Attack        
        self.type_pokemon = pokedex.information_pokemon("type")
        for type in self.type_pokemon:
            if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
                damage == self.data_damage/2
                
            elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
                damage == self.data_damage*2
                
            elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
                damage == self.data_damage
        #Defend
        for type in self.type_pokemon:
            if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
                damage == self.data_defend/2
                
            elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
                damage == self.data_defend*2
                
            elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
                damage == self.data_defend
    
    def vol(self,type,damage,player):
        #Attack        
        self.type_pokemon = pokedex.information_pokemon("type")
        for type in self.type_pokemon:
            if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
                damage == self.data_damage/2
                
            elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
                damage == self.data_damage*2
                
            elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
                damage == self.data_damage
        #Defend
        for type in self.type_pokemon:
            if type == self.type_pokemon["feu"] or self.type_pokemon["eau"]:
                damage == self.data_defend/2
                
            elif type == self.type_pokemon["plante"] or self.type_pokemon["insecte"]:
                damage == self.data_defend*2
                
            elif type == self.type_pokemon["normal"] or self.type_pokemon["elec"] or self.type_pokemon["sol"] or self.type_pokemon["vol"]:
                damage == self.data_defend
    
    