import json
import random
import pygame
from files.class_py.element import Element
from files.class_py.screen import Screen

class Pokedex(Element, Screen):
    def __init__(self):
        Element.__init__(self)
        Screen.__init__(self)
        self.choose_save = 'save1'
        self.info_pokemon = self.ouverture_pokemonjson()
        self.pkmn_rencontre = self.ouverture_pokemonrencontre()
        self.pokedex_run = False
        self.detailed_pokemon = False

    def print_pkmn(self):
        print(self.pkmn_rencontre)

    def ouverture_pokemonjson(self):
        with open('pokemon.json', 'r') as fichier:
            self.donnees_pokemon = json.load(fichier)
            return self.donnees_pokemon

    def ouverture_pokemonrencontre(self):
        with open(f'{self.choose_save}.json', 'r') as file:
            self.donnees_rencontre = json.load(file)
            return self.donnees_rencontre

    def vider_fichier_json(self):
        with open(f'{self.choose_save}.json', 'w') as fichier:
            json.dump([], fichier)
        self.pkmn_rencontre = self.ouverture_pokemonrencontre()
        
        return self.pkmn_rencontre

    def get_last_pokemon_number(self):
        last_pokemon = self.info_pokemon[-1]
        return last_pokemon['numero']

    def get_last_pokemon_rencontre_number(self):
        with open(f'{self.choose_save}.json', 'r') as fichier:
            data = json.load(fichier)
            max_poke_rencontre = len(data)
        return max_poke_rencontre

    def starter(self):
        self.starter1 = self.info_pokemon[0]
        self.starter2 = self.info_pokemon[3]
        self.starter3 = self.info_pokemon[6]
        self.starter4 = self.info_pokemon[9]
        return self.starter1, self.starter2, self.starter3, self.starter4
    
    def information_pokemon(self, data):
        self.pokemon_liste = []
        for info_pokemon in self.info_pokemon:
            self.pokemon_liste(info_pokemon[data])  

    def poke_rencontre(self, pokemon_name):
        self.ouverture_pokemonrencontre()
        existe = False
        for pokemon in self.pkmn_rencontre:
            if pokemon['nom'] == pokemon_name:
                pokemon['rencontre'] += 1
                existe = True

        if not existe:
            for index, pokemon_info in enumerate(self.info_pokemon):
                if pokemon_info['nom'] == pokemon_name:
                    pokemon_num = pokemon_info['numero']
            rencontre_num = self.get_last_pokemon_rencontre_number()
            self.pkmn_rencontre.append({'numero': rencontre_num + 1, 'nom': pokemon_name, 'rencontre': 1, 'true_num': pokemon_num, 'level': 1})

        with open(f'{self.choose_save}.json', 'w') as file:
            json.dump(self.pkmn_rencontre, file, indent=2)

        return False
    
    def info_rencontre(self):
        self.liste_rencontre = []
        for pokemon in self.pkmn_rencontre:
            self.liste_rencontre(pokemon)

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
        self.info_pokemon = self.ouverture_pokemonjson()
        self.pkmn_rencontre = self.ouverture_pokemonrencontre()
        poke_choose = 1
        pkmn_rencontre_liste = []
        while self.pokedex_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if poke_choose < self.get_last_pokemon_number() +1:
                            poke_choose += 1
                        if poke_choose == self.get_last_pokemon_number() +1:
                            poke_choose = 1
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        if poke_choose > 0:
                            poke_choose -= 1
                        if poke_choose == 0:
                            poke_choose = self.get_last_pokemon_number()
                    elif event.key == pygame.K_UP or event.key == pygame.K_z and not self.detailed_pokemon:
                        if poke_choose > 9:
                            poke_choose -= 9
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s and not self.detailed_pokemon:
                        if poke_choose < 45:
                            poke_choose += 9
                    elif event.key == pygame.K_RETURN:
                        self.detailed_pokemon = True
                    elif event.key == pygame.K_ESCAPE:
                        if self.detailed_pokemon:
                            self.detailed_pokemon = False
                        else:
                            self.pokedex_run = False

            for pokemon in self.pkmn_rencontre:
                pkmn_rencontre_liste.append(pokemon['nom'])

            self.img(525, 350, 1050, 743, 'pokedex/background')
            if self.detailed_pokemon == False:
                for i, pokemon in enumerate(self.info_pokemon):
                    column = i % 9
                    row = i // 9
                    self.pokemon_name = pokemon['nom'].lower()
                    if pokemon['nom'] in pkmn_rencontre_liste:
                        if pokemon['numero'] == poke_choose:
                            if pokemon['numero'] <= 50:
                                self.img(75 + column * 110, 90 + row * 110, 110, 110, f'pokemon/{self.pokemon_name}')
                            else:
                                self.img(75 + column * 110, 90 + row * 110, 110, 110, f'pokemon/default')
                            self.simple_rect((255,255,255),75 + column * 110, 90 + row * 110, 120, 120,3)
                            self.texte(18, f"{pokemon['numero']} / {self.get_last_pokemon_number()}",(255,255,255),1000, 680)
                        else:
                            if pokemon['numero'] <= 50:
                                self.img(75 + column * 110, 90 + row * 110, 85, 85, f'pokemon/{self.pokemon_name}')
                            else:
                                self.img(75 + column * 110, 90 + row * 110, 85, 85, f'pokemon/default')
                    else:
                        if pokemon['numero'] == poke_choose:
                            self.simple_rect((255,255,255),75 + column * 110, 90 + row * 110, 120, 120,3)
                            self.img(75 + column * 110, 90 + row * 110, 85, 85, f'pokemon/unknown')
                            self.texte(30, "?", (255, 255, 255), 75 + column * 110, 90 + row * 110)
                            self.texte(18, f"{pokemon['numero']} / {self.get_last_pokemon_number()}",(255,255,255),1000, 680)
                        else:
                            self.img(75 + column * 110, 90 + row * 110, 85, 85, f'pokemon/unknown')
                            self.texte(30, "?", (255, 255, 255), 75 + column * 110, 90 + row * 110)
                self.update()

            if self.detailed_pokemon:
                self.img(525, 350, 1050, 743, 'pokedex/background')
                for pokemon in self.info_pokemon:
                    if pokemon['nom'] in pkmn_rencontre_liste:
                        if poke_choose == pokemon['numero']:
                            self.img(320,365, 340 ,360, f"pokedex/bg.{pokemon['type']}")
                            self.img(525, 350, 800, 600, 'pokedex/pokedex')
                            if pokemon['numero'] <= 50: 
                                self.img(320, 360, 300, 300, f"pokemon/{pokemon['nom']}")
                            else:
                                self.img(320, 360, 300, 300, f"pokemon/default")                                
                            self.img(750, 280, 150, 150, f"pokedex/{pokemon['type']}")
                            self.texte(18, f"Num {pokemon['numero']} - {pokemon['nom']}", (0,0,0), 750, 380)
                            self.texte(18, f"HP : {pokemon['hp']}", (0,0,0), 750, 430)
                            self.texte(18, f"Atq : {pokemon['attaque']}", (0,0,0), 750, 480)
                            self.texte(18, f"Def : {pokemon['def']}", (0,0,0), 750, 530)
                            self.texte(18, f"{pokemon['numero']} / {self.get_last_pokemon_number()}",(255,255,255),1000, 680)
                    elif pokemon['nom'] not in pkmn_rencontre_liste:
                        if poke_choose == pokemon['numero']:
                            self.img(525, 350, 800, 600, 'pokedex/pokedex')
                            self.img(320, 360, 300, 300, f"pokemon/unknown")
                            self.texte(100, "?", (255,255,255), 325, 360)
                            self.img(750, 280, 150, 150, f"pokedex/unknowntype")
                            self.texte(50, "?", (255,255,255), 750, 290)
                            self.texte(18, "Num ??? - ???", (0,0,0), 750, 380)
                            self.texte(18, "HP : ???", (0,0,0), 750, 430)
                            self.texte(18, "Atq : ???", (0,0,0), 750, 480)
                            self.texte(18, "Def : ???", (0,0,0), 750, 530)
                            self.texte(18, f"{pokemon['numero']} / {self.get_last_pokemon_number()}",(255,255,255),1000, 680)

                self.update()
