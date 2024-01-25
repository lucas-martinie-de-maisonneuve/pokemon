import pygame
from files.class_py.pokedex import Pokedex
from files.class_py.maps_combat import Maps
from files.class_py.combat import Combat
from files.class_py.starter import Starter
from files.class_py.add_pokemon import AddPokemon
from files.class_py.setting import Setting

combat = Combat()
starter = Starter()
addpokemon = AddPokemon()
setting = Setting()


class Menu(Pokedex):
    def __init__(self):
        Pokedex.__init__(self)
        self.menu_run = True
        self.show_home = True
        self.load_home = False
        self.load_game = False
        self.new_game = False
        self.home_bag = False

    def default_pkmn(self):
        if self.pkmn_rencontre != []:
            self.pkmn_rencontre = self.ouverture_pokemonrencontre()
            pokemon_default = self.pkmn_rencontre[0]['true_num']
            self.poke_player = self.info_pokemon[pokemon_default - 1]
            starter.poke_player = self.info_pokemon[pokemon_default - 1]

    def home(self):
        self.pkmn_rencontre = self.ouverture_pokemonrencontre()
        if self.pkmn_rencontre != []:
            pokemon_default = self.pkmn_rencontre[0]['true_num']
            starter.poke_player = self.info_pokemon[pokemon_default - 1]
            self.poke_player = self.info_pokemon[pokemon_default - 1]
            starter.starter_choosed = True

        c = 1 #Navigation menu home
        d = 1 #Navigation menu sauvegarde
        while self.menu_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and not setting.setting_run:
                    if self.show_home:
                        self.show_home = False
                        self.load_home = True
                        break
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if c < 5:
                            if not self.load_home and not self.show_home:
                                c += 1
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        if c > 1:
                            if not self.load_home and not self.show_home:
                                c -= 1
                    elif event.key == pygame.K_UP or event.key == pygame.K_z:
                        if d > 1:
                            if self.load_home:
                                d -= 1
                        if c >= 3:
                            if not self.load_home and not self.show_home:
                                c = 6
                        elif c < 3: 
                            if not self.load_home and not self.show_home:
                                c = 0                        
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if d < 3: 
                            if self.load_home:
                                d += 1
                        if c == 6: 
                            if not self.load_home and not self.show_home:
                                c = 5
                        elif c == 0: 
                            if not self.load_home and not self.show_home:
                                c = 1

# Menu New/Load/Quit
                    elif event.key == pygame.K_RETURN and self.load_home:
                        if d == 1: 
                            if self.load_home:
                                if not self.load_game and not self.new_game: # Menu New/Load/Quit
                                    self.new_game = True
                                elif self.new_game:                          # Menu New_game
                                    self.new_game_save1()
                                    self.poke_player = ""
                                    starter.poke_player = ""
                                    self.new_game = False
                                    self.load_home = False
                                elif self.load_game:                         # Menu charger partie
                                    self.default_pkmn()
                                    self.load_game = False
                                    self.load_home = False

                        if d == 2:
                            if self.load_home:
                                if not self.load_game and not self.new_game: # Menu New/Load/Quit
                                    self.load_game = True
                                    d = 1
                                elif self.new_game:                          # Menu New_game
                                    self.new_game_save2()
                                    self.poke_player = ""
                                    starter.poke_player = ""
                                    self.new_game = False
                                    self.load_home = False
                                elif self.load_game:                         # Menu charger partie
                                    self.default_pkmn()
                                    self.load_game = False
                                    self.load_home = False

                        if d == 3: 
                            if self.load_home:
                                if not self.load_game and not self.new_game: # Menu New/Load/Quit
                                    pygame.quit()
                                    quit()
                                elif self.new_game:                          # Menu New_game
                                    self.new_game_save3()
                                    self.load_home = False
                                    self.poke_player = ""
                                    starter.poke_player = ""
                                    self.new_game = False
                                elif self.load_game:                         # Menu charger partie
                                    self.default_pkmn()
                                    self.load_game = False
                                    self.load_home = False

# Menu principal
                    elif event.key == pygame.K_RETURN and not self.load_home and not self.show_home:
                        if c == 1:
                            if starter.poke_player == "":
                                starter.choose_starter = True
                                starter.starter()
                                self.poke_rencontre(starter.poke_player["nom"])
                            else:
                                self.pkmn_rencontre = self.ouverture_pokemonrencontre()
  
                                pokemon_random = self.rand_pokemon()                           
                                maps = Maps(starter.poke_player,pokemon_random, self.choose_save)
                                maps.combat_run = True
                                self.poke_rencontre(pokemon_random["nom"])
                                maps.home()
                        elif c == 2:
                            self.pokedex_run = True
                            self.show_pokedex()
                        elif c == 3:
                            self.home_bag = True
                        elif c == 4:
                            addpokemon.ajout_pokemon()
                        elif c == 5:
                            self.changing_pokemon = True
                            self.change_pokemon()
                        elif c == 6:
                            setting.setting_run = True
                            setting.setting()
                        elif c == 0:
                            if not self.load_home:
                                self.maj_save()
                            self.load_home = True
                    elif event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                        if self.home_bag:
                            self.home_bag = False
                        elif self.load_game:
                            self.load_home = True
                            self.load_game = False
                        elif self.new_game:
                            self.load_home = True
                            self.new_game = False

            if self.pokemon_changed:
                self.pkmn_rencontre = self.ouverture_pokemonrencontre()
                starter.poke_player = self.poke_player
                self.pokedex_changed = False

            if setting.reset :
                self.vider_fichier_json()
                self.poke_player = ""
                starter.poke_player = ""
                setting.reset = False

# 1er menu lancement du jeu
            if self.show_home:  
                self.img_background(525, 350, 1244, 700, 'background')
                self.img(1000, 650, 70, 70,'pokeball')
                self.img_mir(50, 50, 70,70,'pokeball')
                self.texte(30, 'Appuyer sur une touche pour continuer', self.white, self.W // 2, self.H // 2)
                self.img(385, 660, 20, 20, 'menu/copyright')
                self.texte(15, '2024 - LaPlateforme', self.white, 525, 660)
                self.img(100, 680, 17,17, 'menu/copyright')
                self.texte(15, "Le  patron  (Lucas)  -  L'autre  Lucas  avec  les  lunettes (rondes)  -  Keviiiineu (le bg au yeux bleu)", self.white, 525, 680)
                self.update()

#Menu Save/Load/Quit
            if self.load_home and not self.show_home:
                self.img(525, 350, 1244, 700, "menu_load/img_background_load")
                self.img(525, 180, 540, 220, "menu_load/titre_jeu-removebg-preview")

                if not self.load_game and not self.new_game:
                    if d == 1:
                        self.button_rect(self.black, 525, 385, 300, 60 )
                        self.texte(20, "Nouvelle Partie", self.white, 525, 385)
                    else:
                        self.button_rect(self.white, 525, 385, 300, 60 )
                        self.texte(20, "Nouvelle Partie", self.black, 525, 385)

                    if d == 2:
                        self.button_rect(self.black, 525, 510, 300, 60 )
                        self.texte(20, "Charger une partie", self.white, 525, 510)
                    else:
                        self.button_rect(self.white, 525, 510, 300, 60 )
                        self.texte(20, "Charger une partie", self.black, 525, 510)

                    if d == 3:
                        self.button_rect(self.black, 525, 635, 300, 60  )
                        self.texte(20, "Quitter le jeu", self.white, 525, 635)
                    else:
                        self.button_rect(self.white, 525, 635, 300, 60 )
                        self.texte(20, "Quitter le jeu", self.black, 525, 635) 
                    self.update()

# Menu New_game
            if self.new_game:
                if d == 1:
                    self.button_rect(self.black, 275, 400, 300, 60 )
                    self.texte(20, "Save1", self.white, 275, 400)
                    self.choose_save = 'save1'
                else:
                    self.button_rect(self.white, 275, 400, 300, 60 )
                    self.texte(20, "Save1", self.black, 275, 400)

                if d == 2:
                    self.button_rect(self.black, 525, 400, 300, 60 )
                    self.texte(20, "Save2", self.white, 525, 400)
                    self.choose_save = 'save2'
                else:
                    self.button_rect(self.white, 525, 400, 300, 60 )
                    self.texte(20, "Save2", self.black, 525, 400)

                if d == 3:
                    self.button_rect(self.black, 775, 400, 300, 60  )
                    self.texte(20, "Save3", self.white, 775, 400)
                    self.choose_save = 'save3'
                else:
                    self.button_rect(self.white, 775, 400, 300, 60 )
                    self.texte(20, "Save3", self.black, 775, 400)   
                self.update()

#Menu Charger partie
            if self.load_game:
                self.img(600, 350, 600, 480, 'menu_load/load_game')
                if d == 1:
                    self.button_rect(self.white, 100, 175, 120, 120)
                    self.texte(22, "Save 1", self.black, 600, 145)
                    self.img_rotate(100, 175, 100, 100, 'menu_load/loading', 5)
                    self.choose_save = 'save1'
                    if self.pkm_save1 != []:
                        self.texte_not_align(18, f"Dernier pokemon découvert: {self.pkm_save1[-1]['nom']}", self.black, 320 , 280)
                        self.img(600, 450, 250,250, f"pokemon/{self.pkm_save1[-1]['nom'].lower()}")
                        self.texte_not_align(18, f"Nombre de pokemon dans le Pokedex: {len(self.pkm_save1)}/50", self.black, 320 , 230)
                    else:
                        self.texte_not_align(18, f"Aucun pokemon dans le pokedex", self.black, 320 , 280)
                else:
                    self.button_rect(self.white, 100, 175, 100, 100)
                    self.texte(20, "Save 1", self.black, 100, 175)

                if d == 2:
                    self.button_rect(self.white, 100, 350, 120, 120)
                    self.texte(22, "Save 2", self.black, 600, 145)
                    self.img_rotate(100, 350, 100, 100, 'menu_load/loading', 5)
                    self.choose_save = 'save2'
                    if self.pkm_save2 != []:
                        self.texte_not_align(18, f"Dernier pokemon découvert: {self.pkm_save2[-1]['nom']}", self.black, 320 , 280)
                        self.img(600, 450, 250,250, f"pokemon/{self.pkm_save2[-1]['nom'].lower()}")

                        self.texte_not_align(18, f"Nombre de pokemon dans le Pokedex: {len(self.pkm_save2)}/50", self.black, 320 , 230)
                    else:
                        self.texte_not_align(18, f"Aucun pokemon dans le pokedex", self.black, 320 , 280)
                else:
                    self.button_rect(self.white, 100, 350, 100, 100)
                    self.texte(20, "Save 2", self.black, 100, 350)

                if d == 3:
                    self.button_rect(self.white, 100, 525, 120, 120)
                    self.texte(22, "Save 3", self.black, 600, 145)
                    self.img_rotate(100, 525, 100, 100, 'menu_load/loading', 5)
                    self.choose_save = 'save3'
                    if self.pkm_save3 != []:
                        self.texte_not_align(18, f"Dernier pokemon découvert: {self.pkm_save3[-1]['nom']}", self.black, 320 , 280)
                        self.img(600, 450, 250,250, f"pokemon/{self.pkm_save3[-1]['nom'].lower()}")
                        self.texte_not_align(18, f"Nombre de pokemon dans le Pokedex: {len(self.pkm_save3)}/50", self.black, 320 , 230)
                    else:
                        self.texte_not_align(18, f"Aucun pokemon dans le pokedex", self.black, 320 , 280)                
                else:
                    self.button_rect(self.white, 100, 525, 100, 100)
                    self.texte(20, "Save 3", self.black, 100, 525)

                self.update()

# Menu Sac
            if self.home_bag:
                self.img(525, 350, 1244, 700, 'bag/background_bag')
                # self.img(525, 350, 600, 580,'bag/background_texte')
                self.texte(30,"Votre sac est actuellement vide",(0, 255, 233), 525, 350)
                self.update()

# Menu principal
            if not self.show_home and not self.load_home and not self.home_bag:      
                self.img(525, 350, 1244, 700, 'menu/backgroundmenu')
                if starter.poke_player != "":
                    self.img(525, 250, 400, 400, f'pokemon/{starter.poke_player["nom"].lower()}')
                if c == 0:
                    self.img(30, 30, 53, 53, "setting/croix_jaune")                
                else:
                    self.img(30, 30, 46, 46, "setting/croix_rouge")
                if c == 1 : 
                    self.img(125, 550, 120, 120, 'menu/play')
                    self.texte(20,'Play',self.white,125,630)
                else:
                    self.img(125, 550, 100, 100, 'menu/play')
                    self.texte(16,'Play',self.black,125,620)
                if c == 2:
                    self.img(325, 550, 120, 120, 'menu/pokedex')
                    self.texte(20,'Pokedex',self.white,325,630)
                else:
                    self.img(325, 550, 100, 100, 'menu/pokedex')
                    self.texte(16,'Pokedex',self.black,325,620)
                if c == 3:
                    self.img(525, 550, 120, 120, 'menu/bag')
                    self.texte(20,'Bag',self.white,525,630)
                else: 
                    self.img(525, 550, 100, 100, 'menu/bag')
                    self.texte(16,'Bag',self.black,525,620)
                if c == 4:                 
                    self.img(725, 550, 120, 120, 'menu/add_poke')
                    self.texte(20,'Add Pokemon',self.white,725,630)
                else:
                    self.img(725, 550, 100, 100, 'menu/add_poke')
                    self.texte(16,'Add Pokemon',self.black,725,620)
                if c == 5:
                    self.img(925, 550, 120, 120, 'menu/settings')
                    self.texte(20,'Changer de',self.white,925,630)
                    self.texte(20,'Pokemon',self.white,925,650)
                else:
                    self.img(925, 550, 100, 100, 'menu/settings')
                    self.texte(16,'Changer de',self.black,925,620)
                    self.texte(16,'Pokemon',self.black,925,640)
                if c == 6:
                    self.img(990, 60, 100, 100, 'menu/settings')
                    self.texte(17,'Settings',self.white,990,120)
                else:
                    self.img(990, 60, 80, 80, 'menu/settings')
                    self.texte(14,'Settings',self.black,990,110)

                self.update()