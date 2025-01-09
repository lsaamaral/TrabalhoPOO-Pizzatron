from abc import ABC, abstractmethod

class InterfaceIngredientes(ABC):
    @abstractmethod
    def get_ingrediente_em_clique(self, pos: list)-> str:
        ''' Fornece qual eh o nome do ingrediente que foi selecionado pelo mouse '''
        pass

    @abstractmethod
    def draw(self)-> None:
        ''' Desenha os retangulos que serao reconhecidos como as posicoes das cubas de ingredientes '''
        pass