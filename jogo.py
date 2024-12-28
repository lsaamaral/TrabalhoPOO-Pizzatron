import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import pygame
from Utils.database import BancoDeDados
from Telas.login_tela import LoginTela
from Telas.menu_tela import MenuTela
from Telas.jogo_tela import JogoTela
from Telas.ingredientes_manager import IngredientesManager
from Interfaces.game_interface import InterfaceJogo

class Game(InterfaceJogo):
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((1200, 750))
        pygame.display.set_caption("Pizzatron 3000")
        self.clock = pygame.time.Clock()
        self.pos_mouse = pygame.mouse.get_pos()

        banco = BancoDeDados(
            "mongodb+srv://usertrabpoo:pizzatron3000@cluster0.ve3le.mongodb.net/?retryWrites=true&w=majority",
            "jogo"
        )
  
        self.tela_atual = "login"
        self.login_tela = LoginTela(self.tela, banco)
        self.usuario = None
        self.menu_tela = None
        self.jogo_tela = None
        self.ingredientes_manager = None  
    
        self.carregando_ingrediente = False
        self.ingrediente_atual = None

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(60)

    def quit(self):
        pygame.quit()
        exit()

    def handle_input(self):
        self.pos_mouse = pygame.mouse.get_pos()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.quit()

            if self.tela_atual == "login":
                self.login_tela.handle_input(evento)
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                    self.usuario = self.login_tela.authenticate()
                    if self.usuario:
                        self.tela_atual = "menu"
                        self.menu_tela = MenuTela(self.tela, self.usuario)
            elif self.tela_atual == "menu" and self.menu_tela:
                acao = self.menu_tela.handle_input(evento)
                if acao == "play":
                    self.tela_atual = "jogo"
                    self.jogo_tela = JogoTela(self.tela)
                    self.ingredientes_manager = IngredientesManager(self.tela)
                elif acao == "logout":
                    self.usuario = None
                    self.tela_atual = "login"
            elif self.tela_atual == "jogo" and self.jogo_tela:
                self.jogo_tela.handle_input(evento)

                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    self.ingrediente_atual = self.ingredientes_manager.get_ingrediente_em_clique(self.pos_mouse)
                    if self.ingrediente_atual:
                        self.carregando_ingrediente = True

                if evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
                    self.carregando_ingrediente = False
                    self.ingrediente_atual = None

                if not self.jogo_tela.running:
                    self.tela_atual = "menu"


    def update(self):
        pass  # A atualização esta sendo feita no handle input

    def draw(self):
        self.tela.fill((255, 255, 255))

        if self.tela_atual == "login":
            self.login_tela.draw()
        elif self.tela_atual == "menu" and self.menu_tela:
            self.menu_tela.draw()
        elif self.tela_atual == "jogo" and self.jogo_tela:
            self.jogo_tela.draw()
            self.ingredientes_manager.draw()
            
            if self.carregando_ingrediente and self.ingrediente_atual:
                img_width, img_height = self.ingrediente_atual.get_size()
                x, y = self.pos_mouse[0] - img_width // 2, self.pos_mouse[1] - img_height // 2
                self.tela.blit(self.ingrediente_atual, (x, y))