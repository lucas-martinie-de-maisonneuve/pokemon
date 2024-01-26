import pygame
from files.class_py.element import Element
from files.class_py.screen import Screen
from files.class_py.pokedex import Pokedex
from files.class_py.config import confirmation_sound,current_volume,volume_levels
class Setting(Element,Screen):
    def __init__(self):
        Element.__init__(self)
        Screen.__init__(self)
        self.confirmation_sound = confirmation_sound
        self.current_volume = current_volume
        self.volume_levels = volume_levels
        self.verif_quitter = False
        self.setting_run = False
        self.verif_reset = False
        self.reset = False

    def setting(self):
        pokedex = Pokedex()
        m = 1
        c_quit = 1
        c_stat = 0
        c_verif_quit = 1
        c_verif_reset = 1
        horiz_c_audio = 0
        vert_c_audio = 1
        self.top_pokemon = sorted(pokedex.pkmn_rencontre,key=lambda x: x['rencontre'], reverse=True)
        while self.setting_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
#Touche Gauche
                    if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        #Gauche verif quit
                        if m == 4 and self.verif_quitter and c_verif_quit == 2:
                            self.play_confirmation_sound()
                            c_verif_quit = 1
                        #Gauche stat
                        elif m == 2 and c_stat > 0:
                            self.play_confirmation_sound()
                            c_stat -= 1
                        #Gauche reset
                        elif m == 2 and self.verif_reset and c_verif_reset == 2:
                            self.play_confirmation_sound()
                            c_verif_reset = 1
                        #Gauche audio
                        elif m == 3 and horiz_c_audio > 0:
                            self.play_confirmation_sound()
                            horiz_c_audio -= 1
                            if horiz_c_audio == 0:
                                vert_c_audio = 1
#Touche Droite
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        #Droite vérif quitter
                        if m == 4 and self.verif_quitter and c_verif_quit == 1:
                            self.play_confirmation_sound()
                            c_verif_quit = 2
                        #Droite stat
                        elif m == 2 and c_stat < 1:
                            self.play_confirmation_sound()
                            c_stat += 1
                        # Droite reset
                        elif m == 2 and self.verif_reset and c_verif_reset == 1:
                            self.play_confirmation_sound()
                            c_verif_reset = 2
                        #Droite audio
                        elif m == 3 and horiz_c_audio < 4 :
                            self.play_confirmation_sound()
                            horiz_c_audio += 1
                        
#Touche Haut
                    elif event.key == pygame.K_UP or event.key == pygame.K_z:
                        #menu haut
                        if not self.verif_quitter and not self.verif_reset and m > 0 and horiz_c_audio < 1 and vert_c_audio == 1:
                            self.play_confirmation_sound()
                            m -= 1
                        if m == 3 and horiz_c_audio > 0 and vert_c_audio > 0:
                            vert_c_audio -= 1
#Touche Bas
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        #menu bas
                        if not self.verif_quitter and not self.verif_reset and m < 4 and horiz_c_audio < 1:
                            self.play_confirmation_sound()
                            m += 1
                        if m == 3 and horiz_c_audio > 0 and vert_c_audio < 2:
                            vert_c_audio += 1
#Touche Entrée
                    elif event.key == pygame.K_RETURN:
                        #Croix exit setting
                        if m == 0:
                            self.play_confirmation_sound()
                            self.setting_run = False
                        #Lance la fonction "voulez vous vraiment quitter"
                        elif m == 4 and not self.verif_quitter and not self.verif_reset:
                            self.play_confirmation_sound()
                            self.verif_quitter = True
                        #Action à "non" à "voulez vous vraiment quitter"
                        elif c_verif_quit == 1 and self.verif_quitter:
                            self.play_confirmation_sound()
                            self.verif_quitter = False
                        #Action à "oui" à "voulez vous vraiment quitter"
                        elif c_verif_quit == 2 :
                            pygame.quit()
                            quit()
                        #Vérification reset
                        elif c_stat == 1 and m == 2 and not self.verif_reset:
                            self.play_confirmation_sound()
                            self.verif_reset = True
                        #Action à "non" au reset
                        elif c_verif_reset == 1 and self.verif_reset:
                            self.play_confirmation_sound()
                            self.verif_reset = False
                        #Action à "oui" au reset 
                        elif c_verif_reset == 2 and self.verif_reset:
                            self.play_confirmation_sound()
                            pokedex.vider_fichier_json()
                            self.top_pokemon = sorted(pokedex.pkmn_rencontre,key=lambda x: x['rencontre'], reverse=True)
                            self.verif_reset = False
                            self.reset = True
                        #Action mute son confirm
                        elif m == 3 and horiz_c_audio == 1 and vert_c_audio == 2:
                            self.set_volume_level('mute')
                        elif m == 3 and horiz_c_audio == 2 and vert_c_audio == 2:
                            self.set_volume_level('low')
                            self.play_confirmation_sound()
                        elif m == 3 and horiz_c_audio == 3 and vert_c_audio == 2:
                            self.set_volume_level('medium')
                            self.play_confirmation_sound()
                        elif m == 3 and horiz_c_audio == 4 and vert_c_audio == 2:
                            self.set_volume_level('high')
                            self.play_confirmation_sound()

#Touche Echap
                    elif event.key == pygame.K_ESCAPE:
                        #Quitter les paramètre 
                        if not self.verif_quitter and not self.verif_reset:
                            self.play_confirmation_sound()
                            self.setting_run = False
                        #Quitter verif_quitter 
                        elif self.verif_quitter :
                            self.play_confirmation_sound()
                            self.verif_quitter = False
                            c_verif_quit = 1
                        #Quitter verif_reset
                        elif self.verif_reset :
                            self.play_confirmation_sound()
                            self.verif_reset = False
                            c_verif_reset = 1
                        #Quitter audio reset variable
                        elif m == 3 and vert_c_audio > 1:
                            vert_c_audio = 1

                self.img(525, 350, 1244, 700, 'menu/backgroundmenu')
                self.img(990, 60, 80, 80, 'menu/settings')
                self.draw_overlay((0,0,0,200), 525,350, self.W, self.H)
                self.texte(14,'Settings',self.black,990,110)     
                
                self.button_rect(self.grey,525,350,830,560) #Bloc Principal Parametre
                
                self.button_rect(self.darkgreenblue,205,350,170,350) #Bloc Menu
                self.simple_rect(self.black,205,350,170,350,2) #Bordure Menu

                self.button_rect(self.greyblue,615,350,610,500) #Bloc Détails
                self.simple_rect(self.black,615,350,610,500,2) #Bordure Détails

                #Croix exit
                if m == 0:
                    self.img(140,100,46,46,"/setting/croix_jaune")
                    self.img(205,576,150,150,"/setting/pikachu_sleep")
                else:
                    self.img(140,100,46,46,"/setting/croix_rouge")

                # Selecteur 1 Controles
                if m == 1:
                    self.button_rect(self.lightbluesea, 205, 220, 160, 40)  # Boutton selectionné
                    
                    #Pikachu
                    self.img(205,576,150,150,"/setting/pikachu_sleep")

                    #Touche Echap
                    self.img(500,250,50,50,"/setting/key_echap")
                    self.texte(15,"Retour",self.black,500,280)
                    self.texte(15,"Quitter",self.black,500,300)

                    #Touche Entrée
                    self.img(720,240,70,70,"/setting/key_return")
                    self.texte(15,"Selectionné",self.black,720,290)

                    #Bloc touche ZQSD
                    self.img(450,450,50,50,"/setting/key_q")
                    self.img(500,450,50,50,"/setting/key_s")
                    self.img(500,400,50,50,"/setting/key_z")
                    self.img(550,450,50,50,"/setting/key_d")

                    #"Ou"
                    self.texte(15,"ou",self.black,610,450)
                    
                    #Bloc touche flèche directionnels
                    self.img(670,450,50,50,"/setting/key_left")
                    self.img(720,450,50,50,"/setting/key_down")
                    self.img(770,450,50,50,"/setting/key_right")
                    self.img(720,400,50,50,"/setting/key_up")
                else:
                    self.button_rect(self.darkgreenblue, 205, 220, 160, 40)  # Couleur de base
                    self.img(205,576,150,150,"/setting/pikachu_sleep")
                self.texte(15, 'Controles', self.white, 205, 220)

                # Selecteur 2 Statistiques/Reset
                if m == 2 and not self.verif_reset:
                    self.button_rect(self.lightbluesea, 205, 307, 160, 40)
                    self.img(205,576,150,150,"/setting/pikachu_awake")

                    # Statistiques parties pokemon
                    self.texte_not_align(15,f"Nombre de pokemon rencontré: {len(pokedex.pkmn_rencontre)}/{pokedex.get_last_pokemon_number()}", self.black,320,130)
                    self.texte_not_align(15,f"Nombre de combat gagné: ", self.black,320,180)
                    self.texte_not_align(15,f"Nombre de fuite: ", self.black,320,230)
                    self.texte_not_align(15,f"Pokemon les plus rencontres:", self.black,320, 340)
                    if self.top_pokemon:
                        self.texte_not_align(15, f"Dernier pokemon découvert: {pokedex.pkmn_rencontre[-1]['nom']}", self.black, 320, 280)

                        self.button_rect(self.black,430, 560, 150,50)#cadre noir titre nom
                        self.button_rect(self.lightgrey,430, 475, 150,150) #cadre gris clair pokemon
                        self.img(430, 475, 150,150,f"/pokemon/{self.top_pokemon[0]['nom'].lower()}") #img pokemon
                        self.texte(15, f"(x{self.top_pokemon[0]['rencontre']})", self.black,470, 540) #nombre de fois rencontrer
                        self.texte(15, f"{self.top_pokemon[0]['nom']}", self.white,430, 565) #nom pokemon dans cadre noir

                        if len(self.top_pokemon) > 1:
                            self.button_rect(self.black,620, 560, 150,50)
                            self.button_rect(self.lightgrey,620, 475, 150,150)
                            self.img(620, 475, 150,150,f"/pokemon/{self.top_pokemon[1]['nom'].lower()}")
                            self.texte(15, f"(x{self.top_pokemon[1]['rencontre']})", self.black,660, 540) 
                            self.texte(15, f"{self.top_pokemon[1]['nom']}", self.white,620, 565) 
                        else:
                            self.texte_not_align(15, f"Aucun", self.black, 640, 340)
                        if len(self.top_pokemon) > 2:
                            self.button_rect(self.black,810, 560, 150,50)
                            self.button_rect(self.lightgrey,810, 475, 150,150)
                            self.img(810, 475, 150,150,f"/pokemon/{self.top_pokemon[2]['nom'].lower()}")
                            self.texte(15, f"(x{self.top_pokemon[2]['rencontre']})", self.black,850, 540) 
                            self.texte(15, f"{self.top_pokemon[2]['nom']}", self.white,810, 565) 
                        else:
                            self.texte_not_align(15, f"Aucun", self.black, 640, 320)
                    else: 
                        self.texte_not_align(15, f"Dernier pokemon découvert: Aucun", self.black, 320, 280)
                        self.texte_not_align(15, f"Aucun", self.black, 640, 340)

                    if c_stat == 1:
                        self.button_rect(self.darkbluesea,880,140,50,50)
                        self.img_mir(880,140,30,30,"/setting/logo_reset")

                    else:
                        self.button_rect(self.darkgreenblue,880,140,50,50)
                        self.img_mir(880,140,30,30,"/setting/logo_reset")
                else:
                    self.button_rect((37, 50, 55), 205, 307, 160, 40)
                self.texte(15, 'Statistiques', self.white, 205, 307)

                # Selecteur 3 Audio
                if m == 3:
                    self.img(205,596,150,150,"/setting/pikachu_music")
                    self.button_rect(self.lightbluesea, 205, 394, 160, 40)

                    #Titre musique
                    self.button_rect(self.lightgrey,615,190,500,50)
                    self.texte_not_align(15,"Musique :",self.black,380,183)
                    #Titre effets sonore
                    self.button_rect(self.lightgrey,615,390,500,50)
                    self.texte_not_align(15,"Effets Sonores :",self.black,380,383)
                    #Vertical 1 Rectangle 1 Mute
                    if horiz_c_audio == 1 and vert_c_audio == 1:
                        self.button_rect(self.darkbluesea,460,270,60,60) 
                        self.img(460,270,45,45,"/setting/light_mute")
                    else:
                        self.button_rect(self.lightgrey,460,270,60,60)
                        self.img(460,270,45,45,"/setting/solid_mute")
                    #Vertical 1 Rectangle 2 Low volume
                    if horiz_c_audio == 2 and vert_c_audio == 1:
                        self.button_rect(self.darkbluesea,560,270,60,60) 
                        self.img(560,270,45,45,"/setting/light_low_volume")
                    else:
                        self.button_rect(self.lightgrey,560,270,60,60) 
                        self.img(560,270,45,45,"/setting/solid_low_volume")
                    #Vertical 1 Rectangle 3 Medium volume
                    if horiz_c_audio == 3 and vert_c_audio == 1:
                        self.button_rect(self.darkbluesea,660,270,60,60) 
                        self.img(660,270,45,45,"/setting/light_medium_volume")
                    else:
                        self.button_rect(self.lightgrey,660,270,60,60) 
                        self.img(660,270,45,45,"/setting/solid_medium_volume")
                    #Vertical 1 Rectangle 4 High volume
                    if horiz_c_audio == 4 and vert_c_audio == 1:
                        self.button_rect(self.darkbluesea,760,270,60,60)
                        self.img(760,270,45,45,"/setting/light_high_volume")
                    else:
                        self.button_rect(self.lightgrey,760,270,60,60)
                        self.img(760,270,45,45,"/setting/solid_high_volume")

                    #Vertical 2 Rectangle 1 Mute
                    if horiz_c_audio == 1 and vert_c_audio == 2:
                        self.button_rect(self.darkbluesea,460,470,60,60) 
                        self.img(460,470,45,45,"/setting/light_mute")
                    else:
                        self.button_rect(self.lightgrey,460,470,60,60)
                        self.img(460,470,45,45,"/setting/solid_mute")
                    #Vertical 2 Rectangle 2 Low volume
                    if horiz_c_audio == 2 and vert_c_audio == 2:
                        self.button_rect(self.darkbluesea,560,470,60,60) 
                        self.img(560,470,45,45,"/setting/light_low_volume")
                    else:
                        self.button_rect(self.lightgrey,560,470,60,60) 
                        self.img(560,470,45,45,"/setting/solid_low_volume")
                    #Vertical 2 Rectangle 3 Medium volume
                    if horiz_c_audio == 3 and vert_c_audio == 2:
                        self.button_rect(self.darkbluesea,660,470,60,60) 
                        self.img(660,470,45,45,"/setting/light_medium_volume")
                    else:
                        self.button_rect(self.lightgrey,660,470,60,60) 
                        self.img(660,470,45,45,"/setting/solid_medium_volume")
                    #Vertical 2 Rectangle 4 High volume
                    if horiz_c_audio == 4 and vert_c_audio == 2:
                        self.button_rect(self.darkbluesea,760,470,60,60)
                        self.img(760,470,45,45,"/setting/light_high_volume")
                    else:
                        self.button_rect(self.lightgrey,760,470,60,60) 
                        self.img(760,470,45,45,"/setting/solid_high_volume")
                else:
                    self.button_rect(self.darkgreenblue, 205, 394, 160, 40)
                self.texte(15, 'Audio', self.white, 205, 394)

                # Selecteur 4 Quitter
                if m == 4:
                    self.button_rect((39, 76, 119), 205, 481, 160, 40)
                    self.img(205,576,150,150,"/setting/pikachu_angry")
                    self.button_rect(self.lightgrey,615,350,500,200)
                    self.simple_rect(self.black,615,350,500,200,2)
                    self.texte(18,"Quitter le jeu",self.black,615,340)

                    if  c_quit == 1:
                        self.button_rect(self.darkbluesea,615,400,100,50)
                        self.texte(13,"Oui", self.white,615,400)
                    else:
                        self.button_rect((37, 50, 55),615,400,100,50)
                        self.texte(13,"Oui", self.white,615,400)
                else:
                    self.button_rect((37, 50, 55), 205, 481, 160, 40)
                self.texte(15, 'Quitter', self.white, 205, 481)

                #Affichage verif reset
                if self.verif_reset:
                    self.button_rect(self.lightgrey,615,375,350,350) #Rectangle gris
                    self.button_rect(self.darkbluesea,615,175,350,50) #Rectangle bleu
                    self.texte(20,"Effacer les données",self.white,615,175)
                    self.simple_rect(self.black,615,350,350,400,2) #Bordure
                    self.texte(13,"Les données de sauvergarde  ",self.darkgreenblue,615,245)
                    self.texte(13,"de Pokémon seront",self.darkgreenblue,615,270)
                    self.texte(13,"complétements effacées.",self.darkgreenblue,615,295)
                    self.texte(13,"Une fois effacées,",self.darkgreenblue,615,320)
                    self.texte(13,"les données ne pourront",self.darkgreenblue,615,345)
                    self.texte(13,"plus etre utilisées ou récupérées.",self.darkgreenblue,615,370)
                    self.texte(13,"Voulez vous continuer ?",self.darkgreenblue,615,395)

    
                    if c_verif_reset == 1:
                        self.button_rect(self.darkbluesea,515,500,70,50)
                        self.texte(13,"Non", self.white,515,500)
                    else:
                        self.button_rect(self.darkgreenblue,515,500,70,50)
                        self.texte(13,"Non", self.white,515,500)
                    
                    if c_verif_reset == 2:
                        self.button_rect(self.darkbluesea, 715,500,70,50)
                        self.texte(13,"Oui", self.white,715,500)
                    else:
                        self.button_rect(self.darkgreenblue,715,500,70,50)
                        self.texte(13,"Oui", self.white,715,500)
                #Affichage verif quitter
                if self.verif_quitter:
                    self.button_rect(self.darkgrey,615,350,500,200)
                    self.simple_rect(self.black,615,350,500,200,2)
                    self.texte(18,"Voulez vous vraiment quitter ?", self.white,615,340)

                    if c_verif_quit == 1:
                        self.button_rect(self.darkbluesea,515,400,70,50)
                        self.texte(13,"Non", self.white,515,400)
                    else:
                        self.button_rect(self.darkgreenblue,515,400,70,50)
                        self.texte(13,"Non", self.white,515,400)
                    
                    if c_verif_quit == 2:
                        self.button_rect(self.darkbluesea, 715,400,70,50)
                        self.texte(13,"Oui", self.white,715,400)
                    else:
                        self.button_rect(self.darkgreenblue,715,400,70,50)
                        self.texte(13,"Oui", self.white,715,400)
                self.update()

    def toggle_confirmation(self):
        self.confirmation_sound = not self.confirmation_sound
    
    def play_confirmation_sound(self):
        if self.confirmation_sound:
            volume = self.volume_levels[self.current_volume]
            self.confirmation_sound.set_volume(volume)
            self.confirmation_sound.play()

    def set_volume_level(self, volume_option):
        if volume_option in self.volume_levels:
            self.current_volume = volume_option

#if event.type == pygame.KEYDOWN:
#   print(f"""
#       menu: {m}
#       horiz: {horiz_c_audio}
#       verti: {vert_c_audio}""")