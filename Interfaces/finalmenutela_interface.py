from abc import ABC, abstractmethod

class InterfaceFinalMenuTela(ABC):
    @abstractmethod
    def handle_input(self, evento: int)-> str:
        ''' Lida com interacoes do usuario '''
        pass

    @abstractmethod
    def draw(self)-> None:
        ''' Desenha a tela com suas respectivas caracteristicas '''
        pass
