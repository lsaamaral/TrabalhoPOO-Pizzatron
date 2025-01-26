from Interfaces.usuario_interface import InterfaceUsuario

class Usuario(InterfaceUsuario):
    def __init__(self, banco, login, senha):
        self.banco = banco
        self.__login = login
        self.__senha = senha
        self.__id = None
    
    def get_login(self):
        return self.__login
    
    def get_senha(self):
        return self.__senha
    
    def get_id(self):
        return self.__id
    
    def set_id(self, a):
        self.__id = a  
               
    def cadastrar(self):
        if not self.banco.cadastrar_usuario(self.get_login(), self.get_senha()):
            print("Nao foi possivel cadastrar o usuario")

    def fazer_login(self):
        self.set_id(self.banco.verificar_login(self.get_login(), self.get_senha()))
        if self.get_id():
            print(f"Ola {self.get_login()}!")
        else:
            print("Login ou senha incorretos. Tente de novo")

    def registrar_coins(self, coins):
        if self.get_id():
            self.banco.armazenar_coins(self.get_id(), coins)
        else:
            print("Usuario nao esta logado")

    def exibir_melhores_coins(self, limite=5):
        if self.get_id():
            melhores_coins = self.banco.melhores_coins(self.get_id(), limite)
            if melhores_coins:
                print(f"Melhores pontuacoes de {self.get_login()}:")
                for coins, _ in melhores_coins:
                    print(f"Coins: {coins}")
            else:
                print("Nenhuma pontuacao registrada")
        else: 
            print("Usuario nao esta logado")