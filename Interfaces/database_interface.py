from abc import ABC, abstractmethod

class InterfaceDatabase(ABC):
    @abstractmethod
    def cadastrar_usuario(self, login: str, senha: str)-> bool:
        ''' Verifica se o usuario existe, se nao existir cria um '''
        pass

    @abstractmethod
    def verificar_login(self, login: str, senha: str)-> str:
        ''' Verifica se o login e a senha estao de acordo com o banco de dados '''
        pass

    @abstractmethod
    def armazenar_coins(self, usuario_id: str, coins: int)-> None:
        ''' Armazena as moedas do jogador no banco de dados '''
        pass

    @abstractmethod
    def melhores_coins(self, usuario_id: str, limite: int)-> list:
        ''' Retorna as 5 melhores pontuacoes do jogador '''
        pass
