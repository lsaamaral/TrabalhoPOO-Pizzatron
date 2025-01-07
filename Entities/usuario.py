class Usuario():
    def __init__(self, banco, login, senha):
        self.banco = banco
        self.login = login
        self.__senha = senha
        self.id = None
    
    def get_senha(self):
        return self.__senha
    def cadastrar(self):
        if not self.banco.cadastrar_usuario(self.login, self.get_senha()):
            print("Nao foi possivel cadastrar o usuario")

    def fazer_login(self):
        self.id = self.banco.verificar_login(self.login, self.get_senha())
        if self.id:
            print(f"Ola {self.login}!")
        else:
            print("Login ou senha incorretos. Tente de novo")

    def registrar_coins(self, coins):
        if self.id:
            self.banco.armazenar_coins(self.id, coins)
        else:
            print("Usuario nao esta logado")

    def exibir_melhores_coins(self, limite=5):
        if self.id:
            melhores_coins = self.banco.melhores_coins(self.id, limite)
            if melhores_coins:
                print(f"Melhores pontuacoes de {self.login}:")
                for coins, _ in melhores_coins:
                    print(f"Coins: {coins}")
            else:
                print("Nenhuma pontuacao registrada")
        else: 
            print("Usuario nao esta logado")