class Type:
    def __init__(self) -> None:
        pass
    
    def normal(self,type,damage):        
        if type:
            return damage                        
                
    def feu(self,type,damage):
        if type == "feu" or type == "eau" or type == "eau.vol" or type == "feu.vol":
            damage = damage // 2
            return damage
            
        elif type == "plante" or type == "insecte":
            damage = damage * 2
            return damage
            
        elif type == "normal" or type == "elec" or type == "sol" or type == "vol" or type == "elec.vol":
            damage = damage
            return damage
        
    def eau(self,type,damage):        
        if type == "feu" or type == "sol" or type == "feu.vol":
            damage = damage * 2
            return damage
            
        elif type == "eau" or type == "plante" or type == "eau.vol":
            damage = damage // 2
            return damage
            
        elif type == "normal" or type == "elec" or type == "insecte" or type == "vol" or type == "elec.vol":
            damage = damage
            return damage
        
    def plante(self,type,damage):
        if type == "feu" or type == "plante" or type == "vol" or type == "insecte" or type == "elec.vol" or type == "feu.vol":
            damage = damage // 2
            return damage
            
        elif type == "eau" or type == "sol":
            damage = damage * 2
            return damage
            
        elif type == "normal" or type == "elec" or type == "eau.vol":
            damage = damage
            return damage
        
    def elec(self,type,damage):
        if type == "plante" or type == "elec":
            damage = damage // 2
            return damage
            
        elif type == "eau" or type == "vol" or type == "eau.vol" or type == "feu.vol":
            damage = damage * 2
            return damage
            
        elif type == "normal" or type == "feu" or type == "sol" or type == "insecte" or type == "elec.vol":
            damage = damage
            return damage
        
    def sol(self,type,damage):
        if type == "plante" or type ==  "insecte" or type == "eau.vol":
            damage = damage // 2
            return damage
        
        elif type == "feu" or type == "elec":
            damage = damage * 2
            return damage
            
        elif type == "normal" or type == "eau" or type == "sol" or type == "vol" or type == "elec.vol" or type == "feu.vol":
            damage = damage
            return damage
        
    def vol(self,type,damage):
        if type == "elec" or type == "elec.vol":
            damage = damage // 2
            
            
            return damage
        
        elif type == "plante" or type == "insecte":
            damage = damage * 2
            return damage
        
        elif type == "normal" or type == "feu" or type == "eau" or type == "sol" or type == "vol" or type == "eau.vol" or type == "feu.vol":
            damage = damage
            return damage
        
    def insecte(self,type,damage):
        if type == "feu" or type ==  "vol" or type == "feu.vol" or type == "elec.vol" or type == "eau.vol":
            damage = damage // 2
            return damage
            
        elif type == "plante":
            damage = damage * 2
            
            
            return damage
            
        elif type == "normal" or type == type == "eau" or type == "elec" or type == "sol" or type == "insecte":
            damage = damage
            return damage
        
    def elecvol(self,type,damage):
        if type == "elec" or type ==  "sol" or type == "elec.vol":
            damage = damage // 2
            return damage
            
        elif type == "eau" or type == "vol" or type == "insecte" or type == "eau.vol":
            damage = damage * 2
            return damage
            
        elif type == "normal" or type == type == "feu" or type == "plante" or type == "feu.vol":
            damage = damage
            return damage
        
    def feuvol(self,type,damage):
        if type == "feu" or type ==  "eau" or type == "elec" or type == "eau.vol":
            damage = damage // 2
            return damage
            
        elif type == "plante" or type == "insecte" or type == "feu.vol":
            damage = damage * 2
            return damage
            
        elif type == "normal" or type == type == "vol" or type == "sol" or type == "elec.vol":
            damage = damage
            return damage
        
    def eauvol(self,type,damage):
        if type == "eau" or type ==  "elec" or type == "elec.vol":
            damage = damage // 2
            return damage
            
        elif type == "feu" or type == "insecte" or type == "sol" or type == "feu.vol":
            damage = damage * 2
            return damage
            
        elif type == "normal" or type == "plante" or type == "vol" or type == "eau.vol":
            damage = damage
            return damage