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
            type_pokemon = random.choice(pokemon["types"])
            print(type_pokemon)
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
            print(puissance_adversaire)
            return puissance_adversaire

combat = Combat()
combat.recuperer_puissanceAdvers()
combat.recuperer_typeAdvers()

