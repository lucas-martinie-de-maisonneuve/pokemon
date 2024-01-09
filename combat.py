import json
import random

class Combat:
    def __init__(self) -> None:
        pass
    
    def ouverture_pokemonjson(self):
        with open('pokemon.json', 'r') as fichier:
            donnees_pokemon = json.load(fichier)
            return donnees_pokemon
    
    def recuperer_typeAdvers(self):
        info_pokemon = self.ouverture_pokemonjson()       
        
        for pokemon in info_pokemon:
            type_pokemon = random.choice(pokemon["type"])       
        return type_pokemon
            
    def recuperer_puissanceAdvers(self):
        donnee_puissanceAdvers = self.ouverture_pokemonjson()        
        
        for puissance in donnee_puissanceAdvers:
            puissance_adversaire = {
                "attaque": puissance["attaque"],
                "hp": puissance["hp"],
                "def": puissance["def"],
                "vitesse": puissance["vitesse"]
            }        
        return puissance_adversaire

# Utilisation de la classe
combat = Combat()
types_adversaires = combat.recuperer_typeAdvers()
puissances_adversaires = combat.recuperer_puissanceAdvers()

print("Types d'adversaires:", types_adversaires)
print("Puissances d'adversaires:", puissances_adversaires)
