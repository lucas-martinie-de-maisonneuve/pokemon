import json
import random
import pygame
from files.class_py.element import Element
from files.class_py.screen import Screen

class Pokedex(Element):
    def __init__(self):
        self.info_pokemon = self.ouverture_pokemonjson()
        self.pokedex_run = False
        self.detailed_pokemon = False

    def ouverture_pokemonjson(self):
        with open('pokemon.json', 'r') as fichier:
            self.donnees_pokemon = json.load(fichier)
            return self.donnees_pokemon
        
    def get_last_pokemon_number(self):
        last_pokemon = self.info_pokemon[-1]
        return last_pokemon['numero']
    
    def starter(self):
        self.starter1 = self.info_pokemon[0]
        self.starter2 = self.info_pokemon[3]
        self.starter3 = self.info_pokemon[6]
        self.starter4 = self.info_pokemon[9]
        return self.starter1, self.starter2, self.starter3, self.starter4 
#### Liste de tout les pokemon ####
    def information_pokemon(self, data):
        self.pokemon_liste = []
        for info_pokemon in self.info_pokemon:
            self.pokemon_liste(info_pokemon[data])  

    def rand_pokemon(self,data):
        self.pokeliste = []
        for pokemon in self.info_pokemon:
            self.pokeliste.append(pokemon)
        self.poke_random = random.choice(self.pokeliste)
        return self.poke_random[data]

    def rand_pokemon(self):
        random_pokemon = random.choice(self.info_pokemon)
        return {
            'numero': random_pokemon['numero'],
            'nom': random_pokemon['nom'],
            'fin': random_pokemon['evol'],
            'type': random_pokemon['type'],
            'attaque': random_pokemon['attaque'],
            'hp': random_pokemon['hp'],
            'def': random_pokemon['def']
        }
     
    def show_pokedex(self):
        poke_choose = 1
        while self.pokedex_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if poke_choose < self.get_last_pokemon_number() +1:
                            poke_choose += 1
                        if poke_choose == self.get_last_pokemon_number() +1:
                            poke_choose = 1
                    elif event.key == pygame.K_LEFT:
                        if poke_choose > 0:
                            poke_choose -= 1
                        if poke_choose == 0:
                            poke_choose = self.get_last_pokemon_number()
                    elif event.key == pygame.K_UP and not self.detailed_pokemon:
                        if poke_choose > 9:
                            poke_choose -= 9
                    elif event.key == pygame.K_DOWN and not self.detailed_pokemon:
                        if poke_choose < 45:
                            poke_choose += 9
                    elif event.key == pygame.K_RETURN:
                        self.detailed_pokemon = True
                    elif event.key == pygame.K_ESCAPE:
                        if self.detailed_pokemon:
                            self.detailed_pokemon = False
                        else:
                            self.pokedex_run = False

            element.img(525, 350, 1050, 743, 'pokedex/background')
            if self.detailed_pokemon == False:
                for i, pokemon in enumerate(self.info_pokemon):
                    column = i % 9
                    row = i // 9
                    self.pokemon_name = pokemon['nom'].lower()
                    if pokemon['numero'] == poke_choose:
                        element.img(75 + column * 110, 90 + row * 110, 110, 110, f'pokemon/{self.pokemon_name}')
                        element.simple_rect((255,255,255),75 + column * 110, 90 + row * 110, 120, 120,3)

                    else:
                        element.img(75 + column * 110, 90 + row * 110, 85, 85, f'pokemon/{self.pokemon_name}')
                screen.update()

            if self.detailed_pokemon:
                element.img(525, 350, 1050, 743, 'pokedex/background')
                for pokemon in self.info_pokemon:
                    if poke_choose == pokemon['numero']:
                        element.img(320,365, 340 ,360, f"pokedex/bg.{pokemon['type']}")
                        element.img(525, 350, 800, 600, 'pokedex/pokedex')
                        element.img(320, 360, 300, 300, f"pokemon/{pokemon['nom']}")
                        element.img(750, 280, 150, 150, f"pokedex/{pokemon['type']}")
                        element.texte(18, f"Num {pokemon['numero']} - {pokemon['nom']}", (0,0,0), 750, 380)
                        element.texte(18, f"HP : {pokemon['hp']}", (0,0,0), 750, 430)
                        element.texte(18, f"Atq : {pokemon['attaque']}", (0,0,0), 750, 480)
                        element.texte(18, f"Def : {pokemon['def']}", (0,0,0), 750, 530)
                        screen.update()
    
    def ajout_pokemon(self):
        enregistre = False
        info_pokemon = ""
        categories = ["numero", "nom", "evol", "type", "debut", "fin", "attaque", "hp", "def", "vitesse"]
        current_category_index = 0
        active = True

        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_ESCAPE:
                        active = False
                    if event.key == pygame.K_RETURN:
                        # Ouvrir le fichier JSON existant
                        data_pokemon = self.ouverture_pokemonjson()
                        nouveau_pokemon = {
                            "numero": info_pokemon,
                            "nom": info_pokemon,
                            "evol": info_pokemon,
                            "type": info_pokemon,
                            "debut": info_pokemon,
                            "fin": info_pokemon,
                            "attaque": info_pokemon,
                            "hp": info_pokemon,
                            "def": info_pokemon,
                            "vitesse": info_pokemon
                        }
                        data_pokemon.append(nouveau_pokemon)

                        # Écrire les données mises à jour dans le fichier JSON
                        with open("pokemon.json", "w") as fichier:
                            json.dump(data_pokemon, fichier)
                        enregistre = True               
                    elif event.key == pygame.K_BACKSPACE:
                        info_pokemon = info_pokemon[:-1]
                    elif event.key == pygame.K_SPACE:                        
                        current_category_index = (current_category_index + 1) % len(categories)
                    else:
                        info_pokemon += event.unicode
                        
            
            self.img(525, 350, 1050, 743, "img_ajout_pokemon/test_img")
            self.texte(20, "Saisir les informations du Pokémon :", element.black, 525, 250)
            self.texte(20, info_pokemon, (38, 0, 255), 525, 320)           

            if enregistre:
                self.texte(16, "Pokemon ajouté avec succes dans le fichier pokemon.json", (219, 19, 209), 525, 380)
                enregistre = False
                active = False
                screen.clock.tick(240)              
            screen.update()


            
         


# pokedex.info_rand_pokemon('type')
# pokedex.info_rand_pokemon('debut')
pokedex = Pokedex()
element = Element()
screen = Screen()
# pokedex.show_pokedex()