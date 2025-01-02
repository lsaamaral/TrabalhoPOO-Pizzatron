import pygame
from Telas.tela import Tela
from Entities.molho import Molho
from Entities.nivel import Nivel
from Entities.pizza import *
from Entities.ingredientes import IngredientesManager

class JogoTela(Tela):
    def __init__(self, tela):
        self.tela = tela

        # Imagens fixas do cenario
        self.cozinha = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Cozinha.png"), (1300, 475))

        self.telao = pygame.transform.scale(pygame.image.load("Assets/Cardapio/Telao.png"), (500, 375))

        self.bancada = pygame.transform.scale(pygame.image.load("Assets/Sprites/Bancada.png"), (1300, 420))

        self.cubaqueijo = pygame.transform.scale(pygame.image.load("Assets/CubasIngredientes/Queijo.png"), (220, 160))
        self.cubaalga = pygame.transform.scale(pygame.image.load("Assets/CubasIngredientes/Alga.png"), (230, 131))
        self.cubacamarao = pygame.transform.scale(pygame.image.load("Assets/CubasIngredientes/Camarao.png"), (210, 138))
        self.cubalula = pygame.transform.scale(pygame.image.load("Assets/CubasIngredientes/Lula.png"), (210, 143))
        self.cubapeixe = pygame.transform.scale(pygame.image.load("Assets/CubasIngredientes/Peixe.png"), (198, 124))

        self.suportecaixa = pygame.transform.scale(pygame.image.load("Assets/SuporteMolhos/Caixa.png"), (330, 497))
        self.suportetomate = pygame.transform.scale(pygame.image.load("Assets/SuporteMolhos/Tomate.png"), (120, 160))
        self.suportehot = pygame.transform.scale(pygame.image.load("Assets/SuporteMolhos/Hot.png"), (37, 204))
        self.molhotomate = Molho(tela, "Assets/Molhos/Tomate.png", (250, 320))
        self.apertar_molhotomate = pygame.transform.scale(pygame.image.load("Assets/Molhos/Apertar_Tomate.png"), (250, 320))
        self.molhohot = Molho(tela, "Assets/Molhos/Hot.png", (245, 310))
        self.apertar_molhohot = pygame.transform.scale(pygame.image.load("Assets/Molhos/Apertar_Hot.png"), (245, 310))
        self.suportetomatefrente = pygame.transform.scale(pygame.image.load("Assets/SuporteMolhos/Tomate_Frente.png"), (110, 130))

        # Posicoes
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

        # Posicao dos molhos
        self.rect_molhotomate = pygame.Rect(
            self.molhotomate_pos[0] + 100,  # Esquerda/direita
            self.molhotomate_pos[1] + 100,  # Cima/baixo
            self.molhotomate.get_width() - 200,  # Largura
            self.molhotomate.get_height() - 155  # Altura
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

        self.nivel = Nivel(self.tela)
        
        self.ingredientes_manager = IngredientesManager(self.tela)
        self.carregando_ingrediente = False
        self.ingrediente_atual = None

        self.running = True

    def draw(self):
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
        
        self.update()
        self.nivel.atualizar_esteira()
        self.nivel.desenhar_esteira()

        self.nivel.pizza_usuario.desenhar(self.tela)

        if self.nivel.pizza_cardapio:
            self.nivel.pizza_cardapio.desenhar(self.tela)

        if not self.carregando_molhotomate:
            self.tela.blit(self.molhotomate.get_molho(), self.molhotomate_pos)
        else:
            self.molhotomate.draw_animation(self.apertar_molhotomate, pygame.mouse.get_pos(), 38, 103, self.molho_frames_tomate)

        if not self.carregando_molhohot:
            self.tela.blit(self.molhohot.get_molho(), self.molhohot_pos)
        else:
            self.molhohot.draw_animation(self.apertar_molhohot, pygame.mouse.get_pos(), 55, 65, self.molho_frames_hot)

        self.tela.blit(self.suportetomatefrente, self.suportetomatefrente_pos)

        for nome, posicoes in self.nivel.pizza_usuario.ingredientes.items():
            if isinstance(posicoes, list):
                for pos_relativa in posicoes:
                    pos_absoluta = (
                        self.nivel.pizza_usuario.posicao[0] + pos_relativa[0] - 55,
                        self.nivel.pizza_usuario.posicao[1] + pos_relativa[1] - 55
                    )
                    self.tela.blit(self.ingredientes_manager.ingredientes_imgs[nome], pos_absoluta)            

        self.ingredientes_manager.draw()
        if self.carregando_ingrediente and self.ingrediente_atual:
                pos_mouse = pygame.mouse.get_pos()
                img_width, img_height = self.ingrediente_atual.get_size()
                x, y = pos_mouse[0] - img_width // 2, pos_mouse[1] - img_height // 2
                self.tela.blit(self.ingrediente_atual, (x, y))

    def handle_input(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                self.running = False

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            pos_mouse = pygame.mouse.get_pos()

            self.ingrediente_atual = self.ingredientes_manager.get_ingrediente_em_clique(pos_mouse)
            if self.ingrediente_atual:
                self.carregando_ingrediente = True
            
            if self.rect_molhotomate.collidepoint(pos_mouse):
                self.carregando_molhotomate = True
            elif self.rect_molhohot.collidepoint(pos_mouse):
                self.carregando_molhohot = True

        if evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
            pos_mouse = pygame.mouse.get_pos()

            if self.carregando_ingrediente and self.ingrediente_atual:
                if self.nivel.pizza_usuario.esta_sobre(pos_mouse):
                    nome_ingrediente = next(
                        (key for key, img in self.ingredientes_manager.ingredientes_imgs.items() if img == self.ingrediente_atual),
                        None
                    )
                    if nome_ingrediente == "queijo":
                        if not self.nivel.pizza_usuario.ingredientes["queijo"]:
                            self.nivel.pizza_usuario.ingredientes["queijo"] = True
                            self.nivel.pizza_usuario.queijo_sprite = pygame.transform.scale(
                                pygame.image.load("Assets/Pizza/Queijo.png"),
                                (295, 192)
                            )
                    elif nome_ingrediente in self.nivel.pizza_usuario.ingredientes:
                        if isinstance(self.nivel.pizza_usuario.ingredientes[nome_ingrediente], list):
                            pos_relativa = (
                                pos_mouse[0] - self.nivel.pizza_usuario.posicao[0],
                                pos_mouse[1] - self.nivel.pizza_usuario.posicao[1]
                            )
                            self.nivel.pizza_usuario.ingredientes[nome_ingrediente].append(pos_relativa)
                            print(self.nivel.pizza_usuario.ingredientes)
                    self.carregando_ingrediente = False
                    self.ingrediente_atual = None

            self.carregando_molhotomate = False
            self.carregando_molhohot = False

    def update(self):
        self.nivel.pizza_usuario.mover()

        if self.nivel.pizza_usuario.esta_fora_da_tela():
            self.nivel.pizza_usuario.resetar()


        