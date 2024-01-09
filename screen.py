import pygame
class Screen:
    def __init__(self):
        self.Fenetre = pygame.display.set_mode((1050, 700))
        pygame.display.set_caption("Pokemon")
        self.clock = pygame.time.Clock()

    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(60)
        self.Fenetre.fill((0, 0, 0))


    def get_size(self):
        return self.Fenetre.get_size()

    def get_display(self):
        return self.Fenetre

    def img(self, x, y, largeur, hauteur, image_name):
        image = pygame.image.load(f'image/{image_name}.png')
        image = pygame.transform.scale(image, (largeur, hauteur))
        self.Fenetre.blit(image, (x - image.get_width()//2, y - image.get_height()//2))
    
    def img_mir(self, x, y, largeur, hauteur, image_name):
        image = pygame.image.load(f'image/{image_name}.png')
        image = pygame.transform.scale(image, (largeur, hauteur))
        image = pygame.transform.flip(image, True, False)
        self.Fenetre.blit(image, (x - image.get_width()//2, y - image.get_height()//2))


    def rect(self, x, y, largeur, longueur, Texte):
        menu_button_rect = pygame.Rect(x, y, largeur, longueur)
        menu_text = pygame.font.Font(None, 30).render(Texte, True, (210, 180, 222))
        menu_text_rect = menu_text.get_rect(center=menu_button_rect.center)
        pygame.draw.rect(self.Fenetre, (69, 90, 100), menu_button_rect)
        self.Fenetre.blit(menu_text, menu_text_rect)