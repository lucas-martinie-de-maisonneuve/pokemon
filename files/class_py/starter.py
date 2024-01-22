import pygame
from files.class_py.pokedex import Pokedex
from files.class_py.element import Element
from files.class_py.screen import Screen

pygame.font.init()

class Starter(Element, Screen):
    def __init__(self):
        Screen.__init__(self)
        Element.__init__(self)
        self.pokedex = Pokedex()
        self.action = 1
        self.poke_player = ""
        self.choose_starter = False
        self.changing_pokemon = False
        self.pokechoose = 1

    def starter(self):
        while self.choose_starter:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if self.action < 4:
                            self.action += 1
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        if self.action > 1:
                            self.action -= 1
                    elif event.key == pygame.K_RETURN:
                        if self.action == 1:
                            self.poke_player = self.pokedex.starter()[0]
                            self.choose_starter = False
                            return self.poke_player
                        elif self.action == 2:
                            self.poke_player = self.pokedex.starter()[1]
                            self.choose_starter = False
                            return self.poke_player
                        elif self.action == 3:
                            self.poke_player = self.pokedex.starter()[2]
                            self.choose_starter = False
                            return self.poke_player
                        elif self.action == 4:
                            self.poke_player = self.pokedex.starter()[3]
                            self.choose_starter = False
                            return self.poke_player
                                                
            self.img_background(525, 350, 1050, 700, "starter/starterbg")
            self.texte(30, "Choisissez un Pokémon", self.white, 525, 220)
            self.img(160, 435, 180, 180, f"pokemon/{self.pokedex.starter()[0]['nom'].lower()}")
            self.img(400, 435, 180, 180, f"pokemon/{self.pokedex.starter()[1]['nom'].lower()}")
            self.img(620, 435, 180, 180, f"pokemon/{self.pokedex.starter()[2]['nom'].lower()}")
            self.img(900, 435, 180, 180, f"pokemon/{self.pokedex.starter()[3]['nom'].lower()}")

            if self.action == 1:
                self.img(160, 570, 130, 130, "starter/pokeball")
            else:
                self.img(160, 570, 110, 110, "starter/pokeball")

            if self.action == 2:
                self.img(400, 570, 130, 130, "starter/pokeball")
            else:
                self.img(400, 570, 110, 110, "starter/pokeball")

            if self.action == 3:
                self.img(620, 570, 130, 130, "starter/pokeball")
            else:
                self.img(620, 570, 110, 110, "starter/pokeball")

            if self.action == 4:
                self.img(880, 570, 130, 130, "starter/pokeball")
            else:
                self.img(880, 570, 110, 110, "starter/pokeball")
                
            self.update()

    def change_pokemon(self):
        self.pokedex.ouverture_pokemonrencontre()
        self.pokechoose = 1
        while self.changing_pokemon:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if self.pokechoose < self.pokedex.get_last_pokemon_rencontre_number() +1:
                            self.pokechoose += 1
                        if self.pokechoose == self.pokedex.get_last_pokemon_rencontre_number() +1:
                            self.pokechoose = 1
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        if self.pokechoose > 0:
                            self.pokechoose -= 1
                        if self.pokechoose == 0:
                            self.pokechoose = self.pokedex.get_last_pokemon_rencontre_number()
                    elif event.key == pygame.K_UP or event.key == pygame.K_z and not self.pokedex.detailed_pokemon:
                        if self.pokechoose > 9:
                            self.pokechoose -= 9
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s and not self.pokedex.detailed_pokemon:
                        if self.pokechoose < 45:
                            self.pokechoose += 9
                    elif event.key == pygame.K_RETURN:
                        return self.poke_player
                    elif event.key == pygame.K_ESCAPE:
                        self.changing_pokemon = False

            self.img(525, 350, 1050, 743, 'pokedex/background')
            for i, pokemon in enumerate(self.pokedex.pkmn_rencontre):
                for poke_info_index, poke_info in enumerate(self.pokedex.info_pokemon):
                    if poke_info['nom'] == pokemon['nom']:
                        column = i % 9
                        row = i // 9
                        self.pokemon_name = poke_info['nom'].lower()
                        if pokemon['numero'] == self.pokechoose:
                            self.poke_player = self.pokedex.info_pokemon[poke_info_index]
                            if poke_info['numero'] <= 50:
                                self.img(75 + column * 110, 90 + row * 110, 110, 110, f'pokemon/{self.pokemon_name}')
                            else:
                                self.img(75 + column * 110, 90 + row * 110, 110, 110, f'pokemon/default')
                            self.simple_rect((255,255,255),75 + column * 110, 90 + row * 110, 120, 120,3)
                            self.texte(18, f"{pokemon['numero']} / {self.pokedex.get_last_pokemon_number()}",(255,255,255),1000, 680)
                        else:
                            if poke_info['numero'] <= 50:
                                self.img(75 + column * 110, 90 + row * 110, 85, 85, f'pokemon/{self.pokemon_name}')
                            else:
                                self.img(75 + column * 110, 90 + row * 110, 85, 85, f'pokemon/default')

            self.update()