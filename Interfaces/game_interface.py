from abc import ABC, abstractmethod

class InterfaceJogo(ABC):
    @abstractmethod
    def run(self):
        # Inicia o loop principal do jogo
        pass

    @abstractmethod
    def quit(self):
        # Encerra o jogo
        pass

    @abstractmethod
    def handle_input(self):
        # Lida com os eventos de entrada do jogador
        pass

    @abstractmethod
    def update(self):
        # Atualiza o estado do jogo
        pass

    @abstractmethod
    def draw(self):
        # Renderiza os elementos visuais do jogo
        pass