from abc import ABC, abstractmethod

class InterfaceNivel(ABC):
    @abstractmethod
    def criar_pizza_usuario(self)-> None:
        ''' Cria a pizza do usuario no respectivo nivel '''
        pass

    @abstractmethod
    def criar_pizza_cardapio(self, progresso: list)-> None:
        ''' Cria a pizza do cardapio de acordo com o nivel e com o progresso do jogador '''
        pass

    @abstractmethod
    def mudar_nivel(self)-> None:
        ''' Muda o nivel da rodada '''
        pass

    @abstractmethod
    def atualizar_esteira(self)-> None:
        ''' Responsavel pela animacao da esteira, mudando a posicao de cada sprite dependendo da velocidade desejada '''
        pass

    @abstractmethod
    def desenhar_esteira(self)-> None:
        ''' Desenha a animacao da esteira '''
        pass

    @abstractmethod
    def atualizar_pizza_usuario(self)-> None:
        ''' Cria outra pizza do usuario resetada assim que a pizza antiga sai da tela '''
        pass

    @abstractmethod
    def desenhar_pizza_usuario(self)-> None:
        ''' Desenha a pizza do usuario '''
        pass

    @abstractmethod
    def comparar_pizzas(self)-> None:
        ''' Identifica se o usuario colocou algum ingrediente que nao existe no cardapio enquanto a pizza nao esta na sua posicao final '''
        pass

    @abstractmethod
    def comparar_pizzas_final(self)-> None:
        ''' Compara as pizzas do cardapio e do usuario no final da esteira '''
        pass

    @abstractmethod
    def resultado(self)-> str:
        ''' Retorna o resultado finla do jogo, dependendo dos erros e das pizzas feitas pelo usuario. Existem 4 finais diferentes: vitoria, meia vitoria, meia derrota e derrota '''
        pass