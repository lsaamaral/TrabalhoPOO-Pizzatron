from abc import ABC, abstractmethod
import pygame

class InterfacePizzaUsuario(ABC):
    @abstractmethod
    def adicionar_ingrediente(self, ingrediente: str, quantidade: int)-> None:
        ''' Adiciona um ingrediente na lista de ingredientes da pizza '''
        pass

    @abstractmethod
    def criar_lista_ingredientes(self)-> list:
        ''' Cria a lista de ingredientes da pizza'''
        pass

    @abstractmethod
    def mover(self)-> None:
        ''' Move a pizza de acordo com a velocidade da esteira '''
        pass

    @abstractmethod
    def esta_fora_da_tela(self)-> bool:
        ''' Identifica se a pizza esta fora da tela ou nao '''
        pass

    @abstractmethod
    def desenhar(self, tela: pygame.display)-> None:
        ''' Desenha a pizza, seu molho e seus ingredientes na tela '''
        pass

    @abstractmethod
    def esta_sobre(self, pos_mouse: list)-> bool:
        ''' Identifica se o mouse esta sobre a pizza ou nao '''
        pass

    @abstractmethod
    def resetar(self)-> None:
        ''' Reseta a pizza do usuario, tira todos os ingredientes dela e volta para a posicao inicial '''
        pass

    @abstractmethod
    def pintar(self, mouse_pos: list, molho_tipo: str)-> None:
        ''' Pinta a pizza com o molho em pequenos circulos dependendo da posicao do mouse '''
        pass

    @abstractmethod
    def preencher_completo(self, molho: str)-> None:
        ''' Preenche completamente a pizza de molho '''
        pass