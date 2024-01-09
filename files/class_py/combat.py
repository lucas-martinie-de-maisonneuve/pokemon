import json
import random
from files.class_py.element import Element
from files.class_py.menu import Menu
from main import pygame

element = Element()
menu = Menu()

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
        button_attack = element.bouton()
        button_defense = element.bouton()
        button_run = element.bouton()
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False  # Ajoute cette ligne pour sortir de la boucle lorsque la fenêtre est fermée
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos_souris = pygame.mouse.get_pos()                    
                        if button_attack(pos_souris):
                            # Il attaque et fait des dégâts
                            pass 
                        elif button_defense(pos_souris):
                            # Fonction pour se défendre
                            pass  
                        elif button_run(pos_souris):
                        # Fonction pour fuir le combat et faire apparaitre le menu ou revenir sur la map(si elle existe)
                            pass           
    
    def calcule_combatPrincipal(self):
        pass
    
    def recup_pokemonGagnant(self):
        mon_pokemon = self.apparition_pokemon()
        pokemon = self.apparition_pokemon()
        pass           

combat = Combat()
types_adversaires_random = combat.recuperer_typeAdvers()
puissances_adversaires_random = combat.recuperer_puissanceAdvers()

print("Types d'adversaires:", types_adversaires_random)
print("Puissances d'adversaires:", puissances_adversaires_random)
