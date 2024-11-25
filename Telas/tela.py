from abc import ABC, abstractmethod

class Tela(ABC):
    @abstractmethod
    def draw(self):
        # Responsavel por desenhar os elementos da tela em questao
        pass

    @abstractmethod
    def handle_input(self):
        # Lida com as informacoes do usuario, como cliques na tela ou digitos do teclado
        pass