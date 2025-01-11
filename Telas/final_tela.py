import pygame
from Telas.tela import Tela
from Interfaces.finalmenutela_interface import InterfaceFinalMenuTela

class FinalTela(Tela, InterfaceFinalMenuTela):
    def __init__(self, tela, resultado, pizzas_feitas, moedas_totais):
        self.tela = tela
        self.resultado = resultado
        self.pizzas_feitas = pizzas_feitas
        self.moedas_totais = moedas_totais

        self.fundos = {
            "vitoria": pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Final4.png"), (1200, 750)),
            "meia_derrota": pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Final2.png"), (1200, 750)),
            "meia_vitoria": pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Final3.png"), (1200, 750)),
            "derrota": pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Final1.png"), (1200, 750)),
        }

        self.botao = pygame.transform.scale(pygame.image.load("Assets/Botoes/End.png"), (300, 70))
        self.botao_hover = pygame.transform.scale(pygame.image.load("Assets/Botoes/End_Hover.png"), (300, 70))

    def handle_input(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = pygame.mouse.get_pos()
            if self.botao_jogar_rect.collidepoint(pos_mouse):
                return "menu"
            elif self.botao_sair_rect.collidepoint(pos_mouse):
                return "sair"
        return None

    def draw(self):
        caminho_fonte = "Assets/BurbankSmallBold.ttf"
        font_score = pygame.font.Font(caminho_fonte, 30)
        font_titulo = pygame.font.Font(caminho_fonte, 40)
        font_botao = pygame.font.Font(caminho_fonte, 22)
        
        fundo = self.fundos.get(self.resultado, self.fundos["derrota"])
        self.tela.blit(fundo, (0, 0))

        score_texto = "SCORE"
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            titulo_sombreado = font_titulo.render(score_texto, True, (0, 0, 0))
            self.tela.blit(titulo_sombreado, (20 + dx, 20 + dy))
        titulo_principal = font_titulo.render(score_texto, True, (255, 255, 255))
        self.tela.blit(titulo_principal, (20, 20))

        score_text = [
            f"PIZZAS FEITAS: {self.pizzas_feitas}",
            f"MOEDAS TOTAIS: {self.moedas_totais}",
        ]
        for i, linha in enumerate(score_text):
            texto_render = font_score.render(linha, True, (0, 0, 0))
            self.tela.blit(texto_render, (20, 80 + i * 40)) 

        pos_mouse = pygame.mouse.get_pos()
        botao_espacamento = 30
        base_x, base_y = 20, self.tela.get_height() - 180 

        self.botao_jogar_rect = self.botao.get_rect(topleft=(base_x, base_y))
        self.botao_sair_rect = self.botao.get_rect(topleft=(base_x, base_y + 70 + botao_espacamento))

        if self.botao_jogar_rect.collidepoint(pos_mouse):
            self.tela.blit(self.botao_hover, self.botao_jogar_rect.topleft)
        else:
            self.tela.blit(self.botao, self.botao_jogar_rect.topleft)

        jogar_texto = "JOGAR NOVAMENTE"
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            jogar_sombreado = font_botao.render(jogar_texto, True, (139, 0, 0))
            self.tela.blit(jogar_sombreado, (base_x + 55 + dx, base_y + 20 + dy))
        jogar_texto_render = font_botao.render(jogar_texto, True, (255, 255, 255))
        self.tela.blit(jogar_texto_render, (base_x + 55, base_y + 20))

        if self.botao_sair_rect.collidepoint(pos_mouse):
            self.tela.blit(self.botao_hover, self.botao_sair_rect.topleft)
        else:
            self.tela.blit(self.botao, self.botao_sair_rect.topleft)
        sair_texto = "SAIR"
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            sair_sombreado = font_botao.render(sair_texto, True, (139, 0, 0))
            self.tela.blit(sair_sombreado, (base_x + 125 + dx, base_y + 90 + botao_espacamento + dy))
        sair_texto_render = font_botao.render(sair_texto, True, (255, 255, 255))
        self.tela.blit(sair_texto_render, (base_x + 125, base_y + 90 + botao_espacamento))
