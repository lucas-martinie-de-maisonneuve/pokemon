import pygame
from files.class_py.screen import Screen
screen = Screen()

class Element:
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (35, 247, 7)
        self.blue = (72, 149, 239)
        self.lightblue = (189, 224, 254)
        self.brown = (75, 67, 67)
        self.red = (242, 106, 141)
        self.darkred = (221, 45, 74)
        self.darkblue = (67, 97, 238)
        self.yellow = (255, 183, 3)
        self.orange = (251, 133, 0)
        self.green = (161, 193, 129)
        self.darkgreen = (97, 155, 138)

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

    def rect(self, x, y, largeur, longueur, Texte):
        menu_button_rect = pygame.Rect(x, y, largeur, longueur)
        menu_text = pygame.font.Font(None, 30).render(Texte, True, (210, 180, 222))
        menu_text_rect = menu_text.get_rect(center=menu_button_rect.center)
        pygame.draw.rect(screen.Fenetre, (69, 90, 100), menu_button_rect)
        screen.Fenetre.blit(menu_text, menu_text_rect)

    def simple_rect(self, color, x, y, largeur, longueur, epaisseur):
        pygame.draw.rect(screen.Fenetre, color, pygame.Rect(x - largeur //2, y - longueur //2, largeur, longueur),  epaisseur, 5)
        # pygame.draw.rect(screen.Fenetre, (0,0,0), pygame.Rect(200, 550, 120, 120),  2)

    def button_rect(self, color, x, y, longueur, largeur):
        pygame.draw.rect(screen.Fenetre, color, pygame.Rect(x - longueur//2, y - largeur//2, longueur, largeur),  0, 8)

    def rect_hp(self, x, y, longueur, largeur, hp, hp_max):
        if longueur * hp // hp_max >= 85:
            pygame.draw.rect(screen.Fenetre, (6, 214, 160), pygame.Rect(x, y, longueur * hp // hp_max, largeur))
        elif 85 > longueur * hp // hp_max >= 42 :
            pygame.draw.rect(screen.Fenetre, (255, 209, 102), pygame.Rect(x, y, longueur * hp // hp_max, largeur))
        else:
            pygame.draw.rect(screen.Fenetre, (239, 71, 111), pygame.Rect(x, y, longueur * hp // hp_max, largeur))
