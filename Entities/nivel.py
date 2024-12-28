import random
import pygame

class Nivel():
    def __init__(self, tela):
        self.tela = tela
        self.velocidade = 4 
        self.nivel = 1

        self.esteira = pygame.image.load("Assets/Sprites/Esteira.png")
        self.esteira = pygame.transform.scale(self.esteira, (240, 230))

        self.num_esteiras = (1200 // 240) + 2
        self.esteiras_posicoes = [(i*240, 523) for i in range (-1, self.num_esteiras)]

        self.clock = pygame.time.Clock()

    def get_velocidade(self):
        return self.velocidade
    
    def criar_pizza_usuario(self):
        self.pizza_borda = pygame.image.load("Assets/Pizza/Borda.png")
        self.pizza_borda = pygame.transform.scale(self.pizza_borda, (295, 192))
        self.pizza_massa = pygame.image.load("Assets/Pizza/Massa.png")
        self.pizza_massa = pygame.transform.scale(self.pizza_massa, (295, 192))
    
    def criar_pizza_cardapio(self):
        pass

    def mudar_nivel(self):
        self.nivel += 1
        self.velocidade += 0.5

    def atualizar_esteira(self):
        novas_posicoes = []
        for x, y in self.esteiras_posicoes:
            x += self.velocidade

            if x >= 1200:
                x -= len(self.esteiras_posicoes) * 240
            
            novas_posicoes.append((x, y))
        self.esteiras_posicoes = novas_posicoes
    
    def desenhar_esteira(self):
        for posicao in self.esteiras_posicoes:
            self.tela.blit(self.esteira, posicao)