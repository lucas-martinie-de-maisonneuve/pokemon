import json
import random
import pygame

pygame.init()
class Combat:
    def __init__(self) -> None:
        pass
    
    def ouverture_pokemonjson(self):
        with open('pokemon.json', 'r') as fichier:
            donnees_pokemon = json.load(fichier)
            return donnees_pokemon
    
    def recuperer_typeAdvers(self):
        info_pokemon = self.ouverture_pokemonjson()
        types_pokemon = []
        
        for pokemon in info_pokemon:
            types_pokemon.append(pokemon["type"])
        
        return random.choice(types_pokemon)
            
    def recuperer_puissanceAdvers(self):
        donnee_puissanceAdvers = self.ouverture_pokemonjson()
        puissances_adversaires = [] 
        
        for puissance in donnee_puissanceAdvers:
            puissance_adversaire = {
                "attaque": puissance["attaque"],
                "hp": puissance["hp"],
                "def": puissance["def"],
                "vitesse": puissance["vitesse"]
            }
            puissances_adversaires.append(puissance_adversaire)
        
        return random.choice(puissances_adversaires)
    
    def capacites(self):
        button_attack = pygame.draw.rect(ecran, )
    
    def calcule_combatPrincipal(self):
        pass
    
    def recup_pokemonGagnant(self):
        mon_pokemon = self.apparition_pokemon()
        pokemon = self.apparition_pokemon()
        
                

combat = Combat()
types_adversaires_random = combat.recuperer_typeAdvers()
puissances_adversaires_random = combat.recuperer_puissanceAdvers()

print("Types d'adversaires:", types_adversaires_random)
print("Puissances d'adversaires:", puissances_adversaires_random)
