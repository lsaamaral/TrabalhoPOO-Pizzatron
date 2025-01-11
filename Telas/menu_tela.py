import pygame
from Telas.tela import Tela
from Interfaces.finalmenutela_interface import InterfaceFinalMenuTela

class MenuTela(Tela, InterfaceFinalMenuTela):
    def __init__(self, tela, usuario):
        self.tela = tela
        self.usuario = usuario
        self.fonte = pygame.font.Font("Assets/BurbankSmallBold.ttf", 30)
        self.fonte_pontuacoes = pygame.font.Font("Assets/BurbankSmallBold.ttf", 28)
        self.background = pygame.image.load("Assets/Backgrounds/MenuJogo.png")
        self.background = pygame.transform.scale(self.background, (1200, 750))
        self.melhores_coins = self.usuario.banco.melhores_coins(self.usuario.id)

        self.botao_sprite = pygame.transform.scale(pygame.image.load("Assets/Botoes/Start.png"), (200, 50))

        self.botao_play = pygame.Rect(50, 550, 200, 50)
        self.botao_sair = pygame.Rect(50, 650, 200, 50)

    def draw(self):
        self.tela.blit(self.background, (0, 0))

        mouse_pos = pygame.mouse.get_pos()
        hover_play = self.botao_play.collidepoint(mouse_pos)
        hover_sair = self.botao_sair.collidepoint(mouse_pos)

        self.tela.blit(self.botao_sprite, (self.botao_play.x, self.botao_play.y))
        self.tela.blit(self.botao_sprite, (self.botao_sair.x, self.botao_sair.y))

        play_texto = self.fonte.render("Jogar", True, (105, 0, 0))
        sair_texto = self.fonte.render("Sair", True, (105, 0, 0))

        if hover_play:
            borda_play = self.fonte.render("Jogar", True, (255, 255, 255))
            self.tela.blit(borda_play, (self.botao_play.x + 63, self.botao_play.y + 8))
        if hover_sair:
            borda_sair = self.fonte.render("Sair", True, (255, 255, 255))
            self.tela.blit(borda_sair, (self.botao_sair.x + 73, self.botao_sair.y + 8))

        self.tela.blit(play_texto, (self.botao_play.x + 60, self.botao_play.y + 5))
        self.tela.blit(sair_texto, (self.botao_sair.x + 70, self.botao_sair.y + 5))

        if not self.melhores_coins:
            texto = self.fonte.render("Nenhuma pontuacao registrada", True, (105, 0, 0))
            self.tela.blit(texto, (20, 20))
        else:
            y = 50
            for coins, data in self.melhores_coins:
                texto = self.fonte_pontuacoes.render(f"Moedas: {coins} - Data: {data.strftime('%d/%m/%Y %H:%M:%S')}", True, (105, 0, 0))
                self.tela.blit(texto, (20, y))
                y += 40

    def handle_input(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_sair.collidepoint(evento.pos):
                return "logout"
            elif self.botao_play.collidepoint(evento.pos):
                return "play"
            
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                return "play"
            elif evento.key == pygame.K_ESCAPE:
                return "sair"
        return None