from abc import ABC, abstractmethod
import pygame

class InterfacePizzaCardapio(ABC):
    @abstractmethod
    def gerar_pizza(self, nivel: int)-> None:
        ''' Gera uma nova pizza do cardapio dependendo do nivel atual '''
        pass

    @abstractmethod
    def gerar_nome(self)-> str:
        ''' Gera o nome da pizza dependendo dos seus ingredientes '''
        pass

    @abstractmethod
    def adicionar_ingrediente(self, ingrediente: str, quantidade: int)-> None:
        ''' Adiciona ingredientes e atualiza o nome da pizza '''
        pass

    @abstractmethod
    def desenhar(self, tela: pygame.display)-> None:
        ''' Desenha o cardapio na tela '''
        pass

    @abstractmethod
    def desenhar(self, tela: pygame.display)-> None:
        ''' Desenha a pizza, seu molho e seus ingredientes na tela '''
        pass