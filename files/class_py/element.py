import pygame
from files.class_py.screen import Screen
screen = Screen()

class Element:
    def img(self, x, y, largeur, hauteur, image_name):
        image = pygame.image.load(f'files/image/{image_name}.png')
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
        pygame.draw.rect(self.Fenetre, (69, 90, 100), menu_button_rect)
        screen.Fenetre.blit(menu_text, menu_text_rect)