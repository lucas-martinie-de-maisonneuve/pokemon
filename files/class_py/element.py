import pygame
from files.class_py.screen import Screen
screen = Screen()

class Element:
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        self.green = (161, 193, 129)
        self.darkgreen = (97, 155, 138)

        self.blue = (72, 149, 239)
        self.darkgreenblue = (37, 50, 55)
        self.darkblue = (67, 97, 238)
        self.lightblue = (189, 224, 254)
        self.greyblue = (92, 103, 125)
        self.darkbluesea = (0, 40, 85)
        self.lightbluesea = (39, 76, 119)

        self.yellow = (255, 183, 3)
        self.lightyellow = (244, 226, 133)
        self.orange = (251, 133, 0)

        self.red = (242, 106, 141)
        self.darkred = (221, 45, 74)
        self.brown = (75, 67, 67)

        self.grey = (139, 140, 137)
        self.darkgrey = (100,100,100)
        self.lightgrey = (160, 160, 160)

        pygame.mixer.init()
        self.confirmation_sound = pygame.mixer.Sound('files/song/confirm_button.mp3')
        self.win_song = pygame.mixer.Sound('files/song/win.mp3')
        self.win_song_play = False

    def img(self, x, y, largeur, hauteur, image_name):
        image = pygame.image.load(f'files/image/{image_name}.png')
        image = pygame.transform.scale(image, (largeur, hauteur))
        screen.Fenetre.blit(image, (x - image.get_width()//2, y - image.get_height()//2))

    def img_grey(self, x, y, largeur, hauteur, image_name):
        image = pygame.image.load(f'files/image/{image_name}.png')
        image = pygame.transform.scale(image, (largeur, hauteur))
        image_color = image.convert()
        image_color.fill((200, 200, 200), special_flags=pygame.BLEND_RGBA_MULT)
        screen.Fenetre.blit(image_color, (x - image.get_width() // 2, y - image.get_height() // 2))

    def img_poke(self, x, y, largeur, hauteur):
        image = pygame.image.load(self.img())
        image = pygame.transform.scale(image, (largeur, hauteur))
        screen.Fenetre.blit(image, (x - image.get_width()//2, y - image.get_height()//2))
    
    def img_mir(self, x, y, largeur, hauteur, image_name):
        image = pygame.image.load(f'files/image/{image_name}.png')
        image = pygame.transform.scale(image, (largeur, hauteur))
        image = pygame.transform.flip(image, True, False)
        screen.Fenetre.blit(image, (x - image.get_width()//2, y - image.get_height()//2))

    def img_background(self, x, y, largeur, hauteur, image_name):
        image = pygame.image.load(f'files/image/{image_name}.png').convert()
        image = pygame.transform.scale(image, (largeur, hauteur))
        image.set_alpha(115)
        screen.Fenetre.blit(image, (x - image.get_width()//2, y - image.get_height()//2))

    def texte(self, texte_size, texte_content,color, x, y):
        Texte = pygame.font.Font('files/font/pokefont.ttf', texte_size).render(texte_content, True, color)
        Texte_rect = Texte.get_rect(center=(x, y))
        screen.Fenetre.blit(Texte, Texte_rect)
        
    def texte_not_align(self, texte_size, texte_content, color, x, y):
        font = pygame.font.Font('files/font/pokefont.ttf', texte_size)
        Texte = font.render(texte_content, True, color)
        Texte_rect = Texte.get_rect(topleft=(x, y))
        screen.Fenetre.blit(Texte, Texte_rect)

    def rect(self, x, y, largeur, longueur, color):
        pygame.draw.rect(screen.Fenetre, color, pygame.Rect(x - largeur //2, y - longueur //2, largeur, longueur))

    def simple_rect(self, color, x, y, largeur, longueur, epaisseur):
        pygame.draw.rect(screen.Fenetre, color, pygame.Rect(x - largeur //2, y - longueur //2, largeur, longueur),  epaisseur, 5)

    def border_rect(self, color, x, y, largeur, longueur, epaisseur):
        pygame.draw.rect(screen.Fenetre, color, pygame.Rect(x - largeur //2, y - longueur //2, largeur, longueur),  epaisseur, 100)

    def button_rect(self, color, x, y, longueur, largeur):
        pygame.draw.rect(screen.Fenetre, color, pygame.Rect(x - longueur//2, y - largeur//2, longueur, largeur),  0, 8)

    def rect_hp(self, x, y, longueur, largeur, hp, hp_max):
        if longueur * hp // hp_max >= 85:
            pygame.draw.rect(screen.Fenetre, (6, 214, 160), pygame.Rect(x, y, longueur * hp // hp_max, largeur))
        elif 85 > longueur * hp // hp_max >= 35 :
            pygame.draw.rect(screen.Fenetre, (255, 209, 102), pygame.Rect(x, y, longueur * hp // hp_max, largeur))
        else:
            pygame.draw.rect(screen.Fenetre, (239, 71, 111), pygame.Rect(x, y, longueur * hp // hp_max, largeur))
    
    def rect_exp(self, x, y, longueur, largeur, exp, exp_max):
        pygame.draw.rect(screen.Fenetre, (37, 107, 247), pygame.Rect(x, y, longueur * exp // exp_max, largeur), 0, 5)

    def draw_overlay(self, coloralpha, x, y, largeur, longueur):
        overlay_surface = pygame.Surface((largeur, longueur), pygame.SRCALPHA)
        overlay_surface.fill(coloralpha)
        screen.Fenetre.blit(overlay_surface, (x - largeur // 2, y - longueur // 2))

    def stop_and_new(self, music_name):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(f'files/song/{music_name}.mp3')
        pygame.mixer.music.play(-1)
    

    def win_music(self):
        pygame.mixer.music.stop()
        self.win_song.play()


    def play_confirmation_sound(self):
        self.confirmation_sound.play()