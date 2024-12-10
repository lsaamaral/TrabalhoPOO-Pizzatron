import pygame

class IngredientesManager:
    def __init__(self, tela):
        self.tela = tela
        self.novo_tamanho = (200, 200)
        self.novo_tamanho2 = (100, 100)
        self.ingredientes_imgs = {
            "queijo": pygame.transform.scale(pygame.image.load("Assets/Ingredientes/Queijo1.png"), self.novo_tamanho),
            "alga": pygame.transform.scale(pygame.image.load("Assets/Ingredientes/Alga1.png"),self.novo_tamanho2),
            "camarao": pygame.transform.scale(pygame.image.load("Assets/Ingredientes/Camarao1.png"),self.novo_tamanho2),
            "lula": pygame.transform.scale(pygame.image.load("Assets/Ingredientes/Lula1.png"), self.novo_tamanho2),
            "peixe": pygame.transform.scale(pygame.image.load("Assets/Ingredientes/Peixe1.png"), self.novo_tamanho2),
        }
        self.ingredientes_caixas = {
            "queijo": pygame.Rect(275, 400, 223, 100),
            "alga": pygame.Rect(507, 400, 170, 100),
            "camarao": pygame.Rect(687, 400, 187, 100),
            "lula": pygame.Rect(885, 400, 168, 100),
            "peixe": pygame.Rect(1064, 400, 223, 100),
        }

    def get_ingrediente_em_clique(self, pos):
        for nome, caixa in self.ingredientes_caixas.items():
            if caixa.collidepoint(pos):
                return self.ingredientes_imgs[nome]
        return None

    def draw(self):
        for nome, caixa in self.ingredientes_caixas.items():
            
            surface = pygame.Surface(caixa.size, pygame.SRCALPHA)
            
            surface.set_colorkey((255, 255, 255))
            
            pygame.draw.rect(surface, (255, 255, 255), (0, 0, caixa.width, caixa.height))
            
            self.tela.blit(surface, caixa)