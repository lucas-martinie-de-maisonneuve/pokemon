import pygame
from files.class_py.screen import Screen
from files.class_py.element import Element
from files.class_py.pokedex import Pokedex
from files.class_py.combat import Combat
from files.class_py.experience import Experience
from files.class_py.config import sound_config

class Maps(Element, Screen, Combat, Experience):

    def __init__(self, poke_player, pokemon_random, save):
        Element.__init__(self)
        Screen.__init__(self)
        Combat.__init__(self)
        
        Experience.__init__(self, poke_player, save) 
        self.pokedex = Pokedex()
        self.pokedex.change_save(save)
        self.dmg_poke = 0
        self.combat_run = False
        self.action = 1
        self.attack_phase = False
        self.text_phase = False
        self.poke_rand_flee = False
        self.run_fail = False
        self.text = 1
        self.poke_player = poke_player
        self.poke_player_hp = poke_player['hp']
        self.poke_player_hp_max = poke_player['hp']
        self.pokemon_random = pokemon_random
        self.pokemon_random_hp = pokemon_random["hp"]
        self.pokemon_random_hp_max = pokemon_random["hp"]        
        self.pokemon_type_player = poke_player['type']
        self.type_pokemon_advers = pokemon_random['type']
        self.pokemon_def_advers  = pokemon_random['def']
        self.def_poke_player = poke_player['def']
        self.poke_advers = pokemon_random['nom']
        self.game_over = False
        self.attack_phase_advers = False
        self.attack_pkmn_random = False
        self.poke_evolve = poke_player["evol"] 
        self.levelss_poke = self.pokedex.recup_level_exp(poke_player['nom'])
        self.levels_poke = self.levelss_poke['level']
        self.poke_player_hp_before = self.poke_player_hp
        self.pokemon_random_hp_before = self.pokemon_random_hp
        # self.experiencess_pokemon = self.pokedex.recup_level_exp(poke_player)
        self.experience_pokemon = self.levelss_poke['exp']
        self.pokemon_list = self.pokedex.info_pokemon

        pygame.mixer.music.load('files/song/battle.mp3')
        pygame.mixer.music.play(-1)

        self.sound_config = sound_config
        # self.rajout_exp = self.exp_par_combat()                   

    def battle(self):
        while self.combat_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN: 
                    self.update_sound_parameters()
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if self.action < 4:
                            self.play_confirmation_sound()
                            self.action += 1
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        if self.action > 1:
                            self.play_confirmation_sound()
                            self.action -= 1
                    elif event.key == pygame.K_UP or event.key == pygame.K_z and self.action > 2:
                        self.play_confirmation_sound()
                        self.action -= 2
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s and self.action < 3:
                        self.play_confirmation_sound()
                        self.action += 2
                    elif event.key == pygame.K_RETURN and not self.attack_phase and not self.game_over:
                        if self.action == 1 and not self.attack_phase:
                            self.play_confirmation_sound()
                            self.attack_phase = True
                        elif self.action == 2 and not self.attack_phase:
                            self.combat_run = False                       
                        elif self.action == 3 and not self.attack_phase:
                            pass
                        elif self.action == 4 and not self.attack_phase:
                            self.play_confirmation_sound()
                            self.pokedex.pokedex_run = True
                            self.pokedex.show_pokedex()
                    elif event.key == pygame.K_RETURN and self.attack_phase and not self.text_phase and not self.game_over:
                        self.play_confirmation_sound()
                        self.text = 1
                        if self.action == 1:           
                            self.play_confirmation_sound()
                            self.pokemon_random_hp = self.attack(self.pokemon_random_hp, self.poke_player['attaque'],self.pokemon_type_player,self.type_pokemon_advers, self.pokemon_def_advers)                            
                            self.recup_poke_winner(self.poke_player['nom'], self.pokemon_random['nom'], self.poke_player_hp, self.pokemon_random_hp)
                            if self.game_over == True:
                                self.exp_par_combat(self.levels_poke)
                                self.experience_pokemon = self.levelss_poke['exp']
                            self.text_phase = True
                        elif self.action == 2:
                            self.play_confirmation_sound()
                            self.pokemon_random_hp = self.attack(self.pokemon_random_hp, self.poke_player['attaque'],self.pokemon_type_player,self.type_pokemon_advers, self.pokemon_def_advers)                            
                            self.recup_poke_winner(self.poke_player['nom'], self.pokemon_random['nom'], self.poke_player_hp, self.pokemon_random_hp)
                            self.text_phase = True
                        elif self.action == 3 and not self.attack_phase:
                            self.play_confirmation_sound()
                            self.attack_phase = False
                        elif self.action == 4 and not self.attack_phase:
                            self.play_confirmation_sound()
                            self.attack_phase = False
                    elif event.key == pygame.K_RETURN and self.attack_phase and not self.game_over:
                        if self.text == 3:
                            self.play_confirmation_sound()
                            self.text_phase = False
                            self.attack_phase = False
                            self.action = 1
                            self.poke_player_hp_before = self.poke_player_hp
                            self.pokemon_random_hp_before = self.pokemon_random_hp
                        if self.text_phase:
                            self.play_confirmation_sound()
                            self.text += 1
                            if self.text == 2:
                                self.attack_pkmn_random = True                      
                                self.attack_phase_advers = True
                    elif event.key == pygame.K_ESCAPE and self.attack_phase:
                        self.play_confirmation_sound()
                        self.attack_phase = False
                        self.action = 1
                    elif event.key == pygame.K_RETURN and self.game_over:
                        self.stop_and_new("bicycle")
                        self.play_confirmation_sound()
                        self.combat_run = False
    
            self.img(525, 200, 1244, 700,'combat/fight_background')
            self.img_mir(350, 350, 310, 310, f"pokemon/{self.poke_player['nom'].lower()}")
            if self.pokemon_random['numero'] <=50: 
                self.img(725, 225, 175, 175, f"pokemon/{self.pokemon_random['nom'].lower()}")
            else:
                self.img(725, 225, 175, 175, f"pokemon/default")
            # combat.afficher_capacite()
            self.button_rect(self.brown,525,650,self.W,210)            
            self.img(325, 625, 550, 150, 'combat/background_texte')           
            self.img(850, 625, 399, 150,'combat/zone_texte')

            self.button_rect(self.brown, 794, 484, 170, 12)
            self.rect_hp(709, 478, 170, 12, self.poke_player_hp, self.poke_player_hp_max)# Barre de vie player(verte)
            self.img(839, 454, 350, 128, 'combat/player_hp')#Bloc img player info pokemon          
            self.texte_not_align(25, f"{self.poke_player['nom']}", self.black, 712, 405)#Pokemon nom player
            self.texte_not_align(20, f'lvl {self.levels_poke}', self.black, 940, 405)
            self.rect_exp(706, 455, 243, 11, self.experience_pokemon, self.exp_max(self.levels_poke))
            self.img(855, 558, 430, 330, "combat/player_exp")
            self.button_rect(self.brown, 257, 130, 170, 12)
            self.rect_hp(172, 124, 170, 12, self.pokemon_random_hp, self.pokemon_random_hp_max)            
            self.img(211, 100, 350, 128, 'combat/rand_pokemon_hp')
            self.texte_not_align(25, f"{self.pokemon_random['nom']}", self.black, 52, 50)            
            self.texte_not_align(20, f'lvl {self.levels_poke}', self.black, 280, 50)            

            if not self.attack_phase:
                self.button_rect(self.darkred,765,600,145,45)
                self.simple_rect(self.red,765,600,135,35,2) 

                self.button_rect(self.darkblue,945,600,145,45)
                self.simple_rect(self.blue, 945,600,135,35,2)

                self.button_rect(self.darkgreen,765,650,145,45)
                self.simple_rect(self.green, 765,650,135,35,2)

                self.button_rect(self.orange,945,650,145,45)
                self.simple_rect(self.yellow, 945,650,135,35,2)

                if self.action == 1 :
                    self.button_attack = self.texte(19, 'ATTACK', self.white, 765, 600)
                    self.img(680, 600, 15, 15, 'combat/arrow')
                else:
                    self.button_attack = self.texte(18, 'ATTACK', self.black, 765, 600)
                if self.action == 2 :
                    self.button_run = self.texte(19, 'RUN', self.white, 945 , 600)
                    self.img(860, 600, 15, 15, 'combat/arrow')
                else:
                    self.button_run = self.texte(18, 'RUN', self.black, 945 , 600)
                if self.action == 3 :
                    self.button_bag = self.texte(19,'ITEMS', self.white, 765, 650)
                    self.img(680, 650, 15, 15, 'combat/arrow')
                else:
                    self.button_bag = self.texte(18,"ITEMS", self.black, 765, 650)
                if self.action ==4 :
                    self.button_pokedex = self.texte(19,"POKEDEX", self.white, 945, 650)
                    self.img(860, 650, 15, 15, "combat/arrow")
                else:
                    self.button_pokedex = self.texte(18,'POKEDEX', self.black, 945, 650)

            else: 
                self.button_rect(self.white,765,600,145,45)
                self.simple_rect(self.black,765,600,135,35,2)
                self.button_attack = self.texte(16, 'Capacité 1', self.black, 765, 600)

                self.button_rect(self.white,945,600,145,45)
                self.simple_rect(self.black, 945,600,135,35,2)
                self.button_run = self.texte(16, 'Capacité 2', self.black, 945 , 600)

                self.button_rect(self.white,765,650,145,45)
                self.simple_rect(self.black, 765,650,135,35,2)
                self.button_bag = self.texte(16,'Capacité 3', self.black, 765, 650)

                self.button_rect(self.white,945,650,145,45)
                self.simple_rect(self.black, 945,650,135,35,2)
                self.button_pokedex = self.texte(16,'Capacité 4', self.black, 945, 650)

                if self.action == 1 :
                    self.img(680, 600, 15, 15, f'combat/arrow')
                elif self.action == 2 :
                    self.img(860, 600, 15, 15, f'combat/arrow')
                elif self.action == 3 :
                    self.img(680, 650, 15, 15, f'combat/arrow')
                elif self.action == 4 :
                    self.img(860, 650, 15, 15, f'combat/arrow')
            if self.text_phase:
                if self.text == 1:
                    if self.pokemon_random_hp == self.pokemon_random_hp_before:
                        self.texte(20, f"{self.poke_player['nom']} a raté son attaque!", self.black, 325, 625)
                    else:
                        self.texte(20, f"{self.poke_player['nom']} inflige {int(self.dmg_poke)}", self.black, 325, 590)             
                        self.texte(20, f"a {self.pokemon_random['nom']}", self.black, 325, 620)
                elif self.text == 2:
                    if self.attack_phase_advers:
                        if self.attack_pkmn_random:
                            self.poke_player_hp = self.attack(self.poke_player_hp, self.pokemon_random['attaque'],self.type_pokemon_advers, self.pokemon_type_player, self.def_poke_player)
                            self.attack_pkmn_random = False
                        if self.poke_player_hp == self.poke_player_hp_before:
                            self.texte(20, f"{self.pokemon_random['nom']} a raté son attaque!", self.black, 325, 625)
                        else:
                            self.texte(20, f"{self.pokemon_random['nom']} inflige {int(self.dmg_poke)}", self.black, 325, 590)
                            self.texte(20, f"a {self.poke_player['nom']}", self.black, 325, 620)
                    self.recup_poke_winner(self.poke_player['nom'], self.pokemon_random['nom'], self.poke_player_hp, self.pokemon_random_hp)
            else:
                self.texte(20, f"Que doit faire {self.poke_player['nom']}?", self.black, 325, 625)         
            
            if self.game_over:
                if self.win_song_play:
                    self.win_music()
                    self.win_song_play = False 
                self.img(325, 625, 550, 150, "combat/background_texte")
                self.texte(18, f"{self.win} a gagné le combat", self.black, 325, 600)
                self.texte(12, "APPUYER SUR 'ENTRER' POUR CONTINUER", self.black, 325, 650)                               
            self.update()
            