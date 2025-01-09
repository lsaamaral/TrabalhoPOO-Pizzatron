from abc import ABC, abstractmethod

class InterfaceUsuario(ABC):
    @abstractmethod
    def cadastrar(self)-> None:
        ''' Verifica se foi possivel criar o usuario no banco de dados '''
        pass

    @abstractmethod
    def fazer_login(self)-> None:
        ''' Utiliza a verificacao de login do banco de dados e tenta fazer o login '''
        pass

    @abstractmethod
    def registrar_coins(self, coins: int)-> None:
        ''' Se o usuario estiver logado, armazena as moedas do jogador no banco de dados '''
        pass

    @abstractmethod
    def exibir_melhores_coins(self, limite: int)-> None:
        ''' Exibe as 5 melhores pontuacoes do jogador '''
        pass
