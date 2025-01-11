from abc import ABC, abstractmethod

class InterfaceJogoTela(ABC):
    @abstractmethod
    def handle_input(self, evento: int)-> str:
        ''' Lida com interacoes do usuario '''
        pass

    @abstractmethod
    def draw(self)-> None:
        ''' Desenha a tela de jogo '''
        pass

    abstractmethod
    def update(self)-> None:
        ''' Atualiza o estado do jogo dependendo das condicoes de niveis '''
        pass
