import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import pygame
from Utils.database import BancoDeDados
from Telas.login_tela import LoginTela
from Telas.menu_tela import MenuTela
from Telas.jogo_tela import JogoTela
from Telas.final_tela import FinalTela
from Interfaces.jogo_interface import InterfaceJogo

class Jogo(InterfaceJogo):
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # Inicializa o mixer de áudio do pygame
        self.tela = pygame.display.set_mode((1200, 750))
        pygame.display.set_caption("Pizzatron 3000")
        self.clock = pygame.time.Clock()
        
        # Carregar as músicas de cada tela
        self.musica_login = "Assets/Sounds/GEGAGEDIGEDAGEDAG.mp3"
        self.musica_jogo = "Assets/Sounds/Sounds_Music.mp3"

        self.tocar_musica(self.musica_login)

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
        self.final_tela = None
    
    def tocar_musica(self, caminho_musica):
        """Para a música atual e toca a nova música."""
        pygame.mixer.music.stop()
        pygame.mixer.music.load(caminho_musica)
        pygame.mixer.music.set_volume(0.5)  # Ajustar volume (0.0 a 1.0)
        pygame.mixer.music.play(-1)  # Tocar em loop

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(30)

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
                if evento.type == pygame.MOUSEBUTTONDOWN and self.login_tela.botao_inicio.collidepoint(evento.pos):
                    self.usuario = self.login_tela.authenticate()
                    if self.usuario:
                        self.tela_atual="menu"
                        self.menu_tela=MenuTela(self.tela,self.usuario)
            elif self.tela_atual == "menu" and self.menu_tela:
                acao = self.menu_tela.handle_input(evento)
                if acao == "play":
                    self.tela_atual = "jogo"
                    self.jogo_tela = JogoTela(self.tela)

                    # Trocar a música ao entrar no jogo
                    self.tocar_musica(self.musica_jogo)

                elif acao == "logout":
                    self.usuario = None
                    self.tela_atual = "login"

                    # Voltar para a música da tela de login
                    self.tocar_musica(self.musica_login)

            elif self.tela_atual == "jogo" and self.jogo_tela:
                self.jogo_tela.handle_input(evento)

                if not self.jogo_tela.running:
                    self.tela_atual = "final"
                    self.final_tela = FinalTela(self.tela, self.jogo_tela.nivel.resultado(), self.jogo_tela.nivel.pizza_cardapio.pizzas_feitas, self.jogo_tela.nivel.pizza_cardapio.moedas)
            elif self.tela_atual == "final" and self.final_tela:
                acao = self.final_tela.handle_input(evento)
                if acao == "menu":
                    if self.usuario:
                        self.usuario.registrar_coins(self.final_tela.moedas_totais)
                    self.tela_atual = "menu"
                if acao == "sair":
                    if self.usuario:
                        self.usuario.registrar_coins(self.final_tela.moedas_totais)
                    self.quit()

                    # Voltar para a música do menu (opcional)
                    self.tocar_musica(self.musica_login)


    def update(self):
        pass  # A atualização esta sendo feita no handle input

    def draw(self):
        if self.tela_atual == "login":
            self.tela.fill((255, 255, 255))
            self.login_tela.draw()
        elif self.tela_atual == "menu" and self.menu_tela:
            self.tela.fill((255, 255, 255))
            self.menu_tela.draw()
        elif self.tela_atual == "jogo" and self.jogo_tela:
            self.tela.fill((255, 255, 255))
            self.jogo_tela.draw()
        elif self.tela_atual == "final" and self.final_tela:
            self.final_tela.draw()
