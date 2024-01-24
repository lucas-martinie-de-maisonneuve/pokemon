import pygame
from files.class_py.screen import Screen
from files.class_py.element import Element
from files.class_py.pokedex import Pokedex
from files.class_py.maps_combat import Maps
from files.class_py.combat import Combat
from files.class_py.starter import Starter
from files.class_py.add_pokemon import AddPokemon
from files.class_py.setting import Setting

pokedex = Pokedex()
combat = Combat()
starter = Starter()
addpokemon = AddPokemon()
setting = Setting()

class Menu(Element, Screen):
    def __init__(self):
        Element.__init__(self)
        Screen.__init__(self)
        self.menu_run = True
        self.show_home = True
        self.load_home = False

        #initilisation de la musique
        pygame.mixer.music.load('files/song/opening.mp3')
        pygame.mixer.music.play(-1)

    def home(self):
        c = 1
        d = 1 
        while self.menu_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and not setting.setting_run:
                    if self.show_home:
                        self.show_home = False
                        self.load_home = True
                        break
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if c < 5 and not self.load_home and not self.show_home:
                            self.play_confirmation_sound()
                            c += 1
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        if c > 1 and not self.load_home and not self.show_home:
                            self.play_confirmation_sound()
                            c -= 1
                    elif event.key == pygame.K_UP or event.key == pygame.K_z:
                        if d > 1 and self.load_home:
                            self.play_confirmation_sound()
                            d -= 1
                        if c == 3 or c == 4 or c == 5 and not self.load_home and not self.show_home:
                            self.play_confirmation_sound()
                            c = 6
                        elif c == 1 or c == 2 and not self.load_home and not self.show_home:
                            self.play_confirmation_sound()
                            c = 0                        
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if d < 3 and self.load_home:
                            self.play_confirmation_sound()
                            d += 1
                        if c == 6 and not self.load_home and not self.show_home:
                            self.play_confirmation_sound()
                            c = 5
                        elif c == 0 and not self.load_home and not self.show_home:
                            self.play_confirmation_sound()
                            c = 1                  
                    elif event.key == pygame.K_RETURN and self.load_home and not self.show_home:
                        if d == 1 and self.load_home:
                            self.play_confirmation_sound()
                            self.load_home = False
                            c = 1
                        if d == 2 and self.load_home:
                            self.play_confirmation_sound()
                            self.load_home = False
                            # + fonction_save
                        if d == 3 and self.load_home:
                            pygame.quit()
                            quit()
                    elif event.key == pygame.K_RETURN and not self.load_home:
                        if c == 1:
                            self.play_confirmation_sound()
                            self.load_home = False
                            if starter.poke_player == "":
                                self.play_confirmation_sound()
                                starter.choose_starter = True
                                starter.starter()
                                if not any(pokemon['nom'] == starter.poke_player["nom"] for pokemon in pokedex.pkmn_rencontre):
                                    pokedex.poke_rencontre(starter.poke_player["nom"])
                            else:
                                self.play_confirmation_sound()
                                self.stop_and_new("battle")
                                pokemon_random = pokedex.rand_pokemon()                           
                                maps = Maps(starter.poke_player,pokemon_random)
                                maps.battle()
                                maps.combat_run = True
                                pokedex.poke_rencontre(pokemon_random["nom"])
                                self.stop_and_new("bicycle")


                        elif c == 2:
                            self.play_confirmation_sound()
                            self.stop_and_new("pokedex")
                            pokedex.pokedex_run = True
                            pokedex.show_pokedex()
                            self.stop_and_new("bicycle")
                        elif c == 4:
                            self.play_confirmation_sound()
                            addpokemon.ajout_pokemon()
                        elif c == 5:
                            self.play_confirmation_sound()
                            starter.changing_pokemon = True
                            starter.change_pokemon()
                        elif c == 6:
                            self.play_confirmation_sound()
                            setting.setting_run = True
                            setting.setting()
                        elif c == 0:
                            self.play_confirmation_sound()
                            self.load_home = True
                            
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
                
            
            if self.load_home and not self.show_home:
                self.img(525, 350, 1244, 700, "menu_load/img_background_load")
                self.img(525, 180, 540, 220, "menu_load/titre_jeu-removebg-preview")
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
                                

            if not self.show_home and not self.load_home:      
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
