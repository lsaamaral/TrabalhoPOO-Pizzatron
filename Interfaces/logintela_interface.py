from abc import ABC, abstractmethod

class InterfaceLoginTela(ABC):
    @abstractmethod
    def handle_input(self, evento: int)-> str:
        ''' Lida com interacoes do usuario '''
        pass

    @abstractmethod
    def draw(self)-> None:
        ''' Desenha a tela de login '''
        pass

    abstractmethod
    def authenticate(self)-> str:
        ''' Cria um objeto usuario, fazendo o cadastro dele '''
        pass
