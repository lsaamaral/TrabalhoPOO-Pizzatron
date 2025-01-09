import pygame
from Entities.pizza import *
from Interfaces.nivel_interface import InterfaceNivel

class Nivel(InterfaceNivel):
    def __init__(self, tela):
        self.tela = tela
        self.velocidade = 5
        self.velocidade_maior = 50
        self.velocidade_original = self.velocidade
        self.nivel = 1
        self.progresso = {"pizzas_feitas": 0, "pizzas_restantes": 40, "erros": 0, "moedas":0}

        self.esteira = pygame.transform.scale(pygame.image.load("Assets/Sprites/Esteira.png"), (240, 230))

        self.num_esteiras = (1200 // 240) + 2
        self.esteiras_posicoes = [(i*240, 523) for i in range (-1, self.num_esteiras)]

        self.clock = pygame.time.Clock()

        self.criar_pizza_cardapio(self.progresso)
        self.criar_pizza_usuario()

    def get_velocidade(self):
        return self.velocidade
    
    def get_nivel(self):
        return self.nivel
    
    def criar_pizza_usuario(self):
        self.pizza_usuario = PizzaUsuario()
    
    def criar_pizza_cardapio(self, progresso):
        self.pizza_cardapio = PizzaCardapio(progresso)
        self.pizza_cardapio.gerar_pizza(self.nivel)
        self.pizza_cardapio.gerar_nome()
        self.pizza_cardapio.desenhar(self.tela)

    def mudar_nivel(self):
        self.nivel += 1
        self.velocidade_original += 0.5
        self.progresso["pizzas_feitas"] = self.pizza_cardapio.pizzas_feitas
        self.progresso["erros"] = self.pizza_cardapio.erros
        self.progresso["moedas"] = self.pizza_cardapio.moedas
        self.criar_pizza_cardapio(self.progresso)

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
            self.velocidade = self.velocidade_original
            self.pizza_usuario.velocidade = self.velocidade_original
            self.criar_pizza_usuario()
            
        self.pizza_usuario.mover()

    def desenhar_pizza_usuario(self):
        self.pizza_usuario.desenhar(self.tela)

    def comparar_pizzas(self):
        iguais = True 
        for ingrediente, quantidade in self.pizza_cardapio.ingredientes.items():
            if ingrediente in ["alga", "camarao", "lula", "peixe"]:
                if len(self.pizza_usuario.ingredientes[ingrediente]) != quantidade:
                    iguais = False
                    break
            if ingrediente == "queijo":
                if self.pizza_usuario.ingredientes["queijo"] != self.pizza_cardapio.ingredientes["queijo"]:
                    iguais = False
                    break

        if self.pizza_usuario.ingredientes["molho"] != self.pizza_cardapio.molho:
            iguais = False
            
        if iguais:
            self.pizza_usuario.velocidade = self.velocidade_maior
            self.velocidade = self.velocidade_maior
          
        for ingrediente in ["alga", "camarao", "lula", "peixe"]:
            if self.pizza_cardapio.ingredientes.get(ingrediente, 0) == 0 and len(self.pizza_usuario.ingredientes[ingrediente]) > 0:
                self.pizza_usuario.velocidade = self.velocidade_maior
                self.velocidade = self.velocidade_maior
                break

    def comparar_pizzas_final(self):
        iguais = True
        for ingrediente, quantidade in self.pizza_cardapio.ingredientes.items():
            if ingrediente in ["alga", "camarao", "lula", "peixe"]:
                if len(self.pizza_usuario.ingredientes[ingrediente]) != quantidade:
                    iguais = False
                    break
            if ingrediente == "queijo":
                if self.pizza_usuario.ingredientes["queijo"] != self.pizza_cardapio.ingredientes["queijo"]:
                    iguais = False
                    break
            
        if self.pizza_usuario.ingredientes["molho"] != self.pizza_cardapio.molho:
            iguais = False
            
        if iguais:
            self.pizza_cardapio.pizzas_feitas += 1
            self.pizza_cardapio.moedas += 5
            self.mudar_nivel()
        else:
            self.pizza_cardapio.erros += 1

    def resultado(self):
        if self.pizza_cardapio.erros == 5 and self.pizza_cardapio.pizzas_feitas == 25:
            return "meia_derrota"
        if self.pizza_cardapio.erros == 5 and self.pizza_cardapio.pizzas_feitas == 35:
            return "meia_vitoria"
        if self.pizza_cardapio.erros == 5:
            return "derrota"
        elif self.pizza_cardapio.pizzas_feitas == 40:
            return "vitoria"