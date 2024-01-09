class Pokemon:
    def __init__(self,numero, nom, type, niv_evo, attack, defense, vitesse):
        self.numero = numero
        self.nom = nom
        self.type = type
        self.niv_evo = niv_evo
        self.attack = attack
        self.defense = defense
        self.vitesse = vitesse
    
    def get_numero(self):
        return self.numero
    def get_nom(self):
        return self.nom
    def get_type(self):
        return self.type
    def get_niv_evo(self):
        return self.niv_evo
    def get_attack(self):
        return self.attack
    def get_defense(self):
        return self.defense
    def get_vitesse(self):
        return self.vitesse

    def set_nom(self, nom):
        self.nom = nom
    def set_type(self, type):
        self.type = type
    def set_niv_evo(self, niv_evo):
        self.niv_evo = niv_evo
    def set_attack(self, attack):
        self.attack = attack
    def set_defense(self, defense):
        self.defense = defense
    def set_vitesse(self, vitesse):
        self.vitesse = vitesse

    