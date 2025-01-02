import pygame
from Entities.pizza import *

class Nivel():
    def __init__(self, tela):
        self.tela = tela
        self.velocidade = 5 
        self.nivel = 1

        self.esteira = pygame.transform.scale(pygame.image.load("Assets/Sprites/Esteira.png"), (240, 230))

        self.num_esteiras = (1200 // 240) + 2
        self.esteiras_posicoes = [(i*240, 523) for i in range (-1, self.num_esteiras)]

        self.clock = pygame.time.Clock()

        self.criar_pizza_cardapio()
        self.criar_pizza_usuario()

    def get_velocidade(self):
        return self.velocidade
    
    def get_nivel(self):
        return self.nivel
    
    def criar_pizza_usuario(self):
        self.pizza_usuario = PizzaUsuario()
    
    def criar_pizza_cardapio(self):
        self.pizza_cardapio = PizzaCardapio()
        self.pizza_cardapio.gerar_pizza(self.nivel)
        self.pizza_cardapio.gerar_nome()
        self.pizza_cardapio.desenhar(self.tela)

    def mudar_nivel(self):
        self.nivel += 1
        self.velocidade += 0.5
        self.criar_pizza_cardapio()

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

    def atualizar_pizza_usuario(self):
        if self.pizza_usuario.esta_fora_da_tela():
            self.criar_pizza_usuario()
            
        self.pizza_usuario.mover()

    def desenhar_pizza_usuario(self):
        self.pizza_usuario.desenhar(self.tela)

    def executar(self, mouse_pos, mouse_held, ingrediente_atual):
        self.atualizar_esteira()
        self.atualizar_pizza_usuario(mouse_pos, mouse_held, ingrediente_atual)

        self.desenhar_esteira()
        self.desenhar_pizza_usuario()
        self.pizza_cardapio.desenhar(self.tela)

        pygame.display.flip()
        self.clock.tick(60)

