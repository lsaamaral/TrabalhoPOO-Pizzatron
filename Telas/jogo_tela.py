import pygame
from Telas.tela import Tela
from Entities.molho import Molho

class JogoTela(Tela):
    def __init__(self, tela):
        self.tela = tela

        # Imagens fixas do cenario
        self.cozinha = pygame.image.load("Assets/Backgrounds/Cozinha.png")
        self.cozinha = pygame.transform.scale(self.cozinha, (1300, 475))

        self.telao = pygame.image.load("Assets/Pedidos/Telao.png")
        self.telao = pygame.transform.scale(self.telao, (500, 375))

        self.bancada = pygame.image.load("Assets/Sprites/Bancada.png")
        self.bancada = pygame.transform.scale(self.bancada, (1300, 420))

        self.cubaqueijo = pygame.image.load("Assets/CubasIngredientes/Queijo.png")
        self.cubaqueijo = pygame.transform.scale(self.cubaqueijo, (220, 160))
        self.cubaalga = pygame.image.load("Assets/CubasIngredientes/Alga.png")
        self.cubaalga = pygame.transform.scale(self.cubaalga, (230, 131))
        self.cubacamarao = pygame.image.load("Assets/CubasIngredientes/Camarao.png")
        self.cubacamarao = pygame.transform.scale(self.cubacamarao, (210, 138))
        self.cubalula = pygame.image.load("Assets/CubasIngredientes/Lula.png")
        self.cubalula = pygame.transform.scale(self.cubalula, (210, 143))
        self.cubapeixe = pygame.image.load("Assets/CubasIngredientes/Peixe.png")
        self.cubapeixe = pygame.transform.scale(self.cubapeixe, (198, 124))

        self.suportecaixa = pygame.image.load("Assets/SuporteMolhos/Caixa.png")
        self.suportecaixa = pygame.transform.scale(self.suportecaixa, (330, 497))
        self.suportetomate = pygame.image.load("Assets/SuporteMolhos/Tomate.png")
        self.suportetomate = pygame.transform.scale(self.suportetomate, (120, 160))
        self.suportehot = pygame.image.load("Assets/SuporteMolhos/Hot.png")
        self.suportehot = pygame.transform.scale(self.suportehot, (37, 204))
        self.molhotomate = Molho(tela, "Assets/Molhos/Tomate.png", (250, 320))
        self.apertar_molhotomate = pygame.image.load("Assets/Molhos/Apertar_Tomate.png")
        self.apertar_molhotomate = pygame.transform.scale(self.apertar_molhotomate, (250, 320))
        self.molhohot = Molho(tela, "Assets/Molhos/Hot.png", (245, 310))
        self.apertar_molhohot = pygame.image.load("Assets/Molhos/Apertar_Hot.png")
        self.apertar_molhohot = pygame.transform.scale(self.apertar_molhohot, (245, 310))
        self.suportetomatefrente = pygame.image.load("Assets/SuporteMolhos/Tomate_Frente.png")
        self.suportetomatefrente = pygame.transform.scale(self.suportetomatefrente, (110, 130))

        # Posições
        self.cozinha_pos = (-10,-10)
        self.telao_pos = (610, 42)
        self.bancada_pos = (-10, 410)
        self.cubaqueijo_pos = (275, 356)
        self.cubaalga_pos = (468, 391)
        self.cubacamarao_pos = (676, 390)
        self.cubalula_pos = (865, 400)
        self.cubapeixe_pos = (1050, 395)
        self.suportecaixa_pos = (-50, 222)
        self.suportetomate_pos = (8, 336)
        self.suportehot_pos = (200, 290)
        self.molhotomate_pos = (-30, 200)
        self.molhohot_pos = (60, 200)
        self.suportetomatefrente_pos = (15, 340)

        # Posição dos molhos
        self.rect_molhotomate = pygame.Rect(
            self.molhotomate_pos[0] + 100,  # Ajuste para esquerda/direita
            self.molhotomate_pos[1] + 100,  # Ajuste para cima/baixo
            self.molhotomate.get_width() - 200,  # Reduz largura
            self.molhotomate.get_height() - 155  # Reduz altura
        )
    
        self.rect_molhohot = pygame.Rect(
            self.molhohot_pos[0] + 95,
            self.molhohot_pos[1] + 95,
            self.molhohot.get_width() - 190,
            self.molhohot.get_height() - 152
        )

        self.carregando_molhotomate = False
        self.carregando_molhohot = False

        self.molho_frames_tomate = self.molhotomate.animation("Assets/Molhos/Espremer_Tomate.png", 189, 96, 6)
        self.molho_frames_hot = self.molhohot.animation("Assets/Molhos/Espremer_Hot.png", 154, 94, 8)

        self.running = True

    def draw(self, pos_mouse):
        self.tela.blit(self.cozinha, self.cozinha_pos)
        self.tela.blit(self.telao, self.telao_pos)
        self.tela.blit(self.bancada, self.bancada_pos)
        self.tela.blit(self.cubaqueijo, self.cubaqueijo_pos)
        self.tela.blit(self.cubaalga, self.cubaalga_pos)
        self.tela.blit(self.cubacamarao, self.cubacamarao_pos)
        self.tela.blit(self.cubalula, self.cubalula_pos)
        self.tela.blit(self.cubapeixe, self.cubapeixe_pos)
        self.tela.blit(self.suportecaixa, self.suportecaixa_pos)
        self.tela.blit(self.suportetomate, self.suportetomate_pos)
        self.tela.blit(self.suportehot, self.suportehot_pos)

        # Desenhando o molho de tomate
        if not self.carregando_molhotomate:
            self.tela.blit(self.molhotomate.get_molho(), self.molhotomate_pos)
        else:
            self.molhotomate.draw_animation(self.apertar_molhotomate, pos_mouse, 38, 103, self.molho_frames_tomate)

        # Desenhando o molho hot
        if not self.carregando_molhohot:
            self.tela.blit(self.molhohot.get_molho(), self.molhohot_pos)
        else:
            self.molhohot.draw_animation(self.apertar_molhohot, pos_mouse, 55, 65, self.molho_frames_hot)
            
        self.tela.blit(self.suportetomatefrente, self.suportetomatefrente_pos)


    def handle_input(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                self.running = False

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            pos_mouse = pygame.mouse.get_pos()
            
            if self.rect_molhotomate.collidepoint(pos_mouse):
                self.carregando_molhotomate = True
            elif self.rect_molhohot.collidepoint(pos_mouse):
                self.carregando_molhohot = True

        if evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
            self.carregando_molhotomate = False
            self.carregando_molhohot = False

        