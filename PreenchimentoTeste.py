import pygame
import sys

class Molho:
    """
    Classe responsável por gerenciar o molho na pizza.
    Inclui lógica de pintura, preenchimento e detecção de progresso.
    """
    def __init__(self, escala=(200, 200), limite_preenchimento=0.7):
        """
        Inicializa a camada de molho e os elementos relacionados.
        :param escala: Tamanho da camada de molho (largura, altura).
        :param limite_preenchimento: Percentual necessário para considerar o molho completo.
        """
        self.escala = escala
        self.limite_preenchimento = limite_preenchimento  # Percentual necessário para completar o molho
        self.molho_surface = pygame.Surface(escala, pygame.SRCALPHA)  # Superfície transparente para pintar o molho
        self.mask_surface = pygame.Surface(escala, pygame.SRCALPHA)  # Máscara circular para limitar a área de pintura
        pygame.draw.circle(self.mask_surface, (255, 255, 255), (escala[0] // 2, escala[1] // 2), escala[0] // 2)
        self.molho_mask = pygame.mask.from_surface(self.mask_surface)  # Máscara binária baseada na superfície

        self.molho_sprite = pygame.image.load("image.png")  # Sprite do molho para respingos
        self.molho_sprite = pygame.transform.scale(self.molho_sprite, (15, 15))  # Aumentar escala do sprite

        self.pixels_totais = self.molho_mask.count()  # Quantidade total de pixels na área da máscara
        self.pixels_preenchidos = 0  # Quantidade de pixels preenchidos até agora
        self.molho_completo = False  # Indica se o molho foi completamente aplicado

    def pintar(self, mouse_pos, pizza_pos):
        """
        Aplica molho na posição indicada pelo mouse, desde que dentro da máscara e da área da pizza.
        :param mouse_pos: Posição atual do mouse (x, y).
        :param pizza_pos: Posição da pizza na tela (x, y).
        """
        if not self.molho_completo:  # Somente pinta se o molho ainda não estiver completo
            rel_x = mouse_pos[0] - pizza_pos[0]
            rel_y = mouse_pos[1] - pizza_pos[1]

            # Verifica se a posição relativa está dentro da área da máscara
            if 0 <= rel_x < self.escala[0] and 0 <= rel_y < self.escala[1] and self.molho_mask.get_at((rel_x, rel_y)):
                pygame.draw.circle(self.molho_surface, (255, 0, 0, 255), (rel_x, rel_y), 20)  # Aumentar o raio do círculo
                self.molho_surface.blit(self.molho_sprite, (rel_x - 15, rel_y - 15))  # Ajustar respingos

                # Calcula pixels preenchidos dentro da máscara
                self.pixels_preenchidos = sum(
                    1 for y in range(self.escala[1])
                    for x in range(self.escala[0])
                    if self.molho_mask.get_at((x, y)) and self.molho_surface.get_at((x, y))[3] > 0
                )

                # Verifica se a porcentagem preenchida excede o limite necessário
                if self.pixels_preenchidos / self.pixels_totais >= self.limite_preenchimento:
                    self.molho_completo = True
                    self.preencher_completo()

    def preencher_completo(self):
        """
        Preenche automaticamente o molho se a porcentagem necessária for alcançada.
        """
        self.molho_surface.fill((0, 0, 0, 0))  # Limpa a superfície
        pygame.draw.circle(self.molho_surface, (200, 0, 0, 200), (self.escala[0] // 2, self.escala[1] // 2), self.escala[0] // 2)

    def desenhar(self, tela, pizza_pos):
        """
        Desenha o molho na tela, na posição atual da pizza.
        :param tela: Superfície principal do jogo onde tudo é desenhado.
        :param pizza_pos: Posição da pizza na tela (x, y).
        """
        tela.blit(self.molho_surface, pizza_pos)

def main():
    pygame.init()

    # Configurações principais
    LARGURA, ALTURA = 800, 600
    TELA = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Pizzatron 3000 - Pintando a Pizza")

    # Cores
    BRANCO = (255, 255, 255)

    # FPS e relógio
    clock = pygame.time.Clock()
    FPS = 60

    # Carregar imagens
    esteira_img = pygame.image.load("1.png")
    pizza_img = pygame.image.load("Massa.png")
    pizza_img = pygame.transform.scale(pizza_img, (200, 200))

    # Configurações iniciais
    pizza_x = 100
    pizza_y = 300
    esteira_y = 400
    velocidade_pizza = 2

    # Instanciar classe Molho
    molho = Molho()

    pintando = False  # Controle do mouse

    # Loop principal do jogo
    while True:
        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pintando = True
            elif evento.type == pygame.MOUSEBUTTONUP:
                pintando = False

        # Atualizar posição da pizza
        pizza_x += velocidade_pizza
        if pizza_x > LARGURA:
            pizza_x = -200

        # Atualizar pintura
        if pintando:
            mouse_pos = pygame.mouse.get_pos()
            molho.pintar(mouse_pos, (pizza_x, pizza_y))

        # Desenhar elementos na tela
        TELA.fill(BRANCO)
        TELA.blit(esteira_img, (0, esteira_y))
        TELA.blit(pizza_img, (pizza_x, pizza_y))
        molho.desenhar(TELA, (pizza_x, pizza_y))

        # Atualizar display
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
