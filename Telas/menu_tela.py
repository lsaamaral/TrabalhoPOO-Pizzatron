import pygame
from Telas.tela import Tela

class MenuTela(Tela):
    def __init__(self, tela, usuario):
        self.tela = tela
        self.usuario = usuario
        self.fonte = pygame.font.Font("Assets/BurbankSmallBold.ttf", 32)
        self.background = pygame.image.load("Assets/Backgrounds/MenuJogo.png")
        self.background = pygame.transform.scale(self.background, (1200, 750))
        self.botao_play = pygame.Rect(300, 400, 200, 50)
        self.botao_sair = pygame.Rect(300, 500, 200, 50)
        self.melhores_coins = self.usuario.banco.melhores_coins(self.usuario.id)

    def draw(self):
        self.tela.blit(self.background, (0, 0))

        pygame.draw.rect(self.tela, (0, 255, 0), self.botao_play)
        play_texto = self.fonte.render("Play", True, (0, 0, 0))
        self.tela.blit(play_texto, (self.botao_play.x + 70, self.botao_play.y + 5))
        
        pygame.draw.rect(self.tela, (255, 0, 0), self.botao_sair)
        sair_texto = self.fonte.render("Quit", True, (0, 0, 0))
        self.tela.blit(sair_texto, (self.botao_sair.x + 70, self.botao_sair.y + 5))

        if not self.melhores_coins:
            texto = self.fonte.render("Nenhuma pontuacao registrada", True, (0, 0, 0))
            self.tela.blit(texto, (20, 20))
        else:
            y = 50
            for coins, data in self.melhores_coins:
                texto = self.fonte.render(f"Coins: {coins} - Data: {data.strftime('%d/%m/%Y %H:%M:%S')}", True, (0, 0, 0))
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