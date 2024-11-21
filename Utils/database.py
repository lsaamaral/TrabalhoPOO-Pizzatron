from pymongo import MongoClient
import bcrypt
from datetime import datetime

class BancoDeDados():
    def __init__(self, uri, db_name):
        try:
            self.cliente = MongoClient(uri)
            self.db = self.cliente[db_name]
            print("Conectado ao MongoDB na nuvem")
        except Exception as e:
            print(f"Erro ao conectar ao MongoDB na nuvem: {e}")
            self.db = None
    

    def cadastrar_usuario(self, login, senha):
        try:
            # Verifica se o usuario existe
            if self.db.usuarios.find_one({"login": login}):
                print("Usuario ja existe no jogo. Tente um login diferente.")
                return False  # Usuario ja existe
            senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
            usuario = {
                "login": login,
                "senha": senha_hash,
            }
            self.db.usuarios.insert_one(usuario)
            print("Usuario cadastrado")
            return True  # Cadastro feito
        except Exception as e:
            print(f"Erro no cadastro do usuario: {e}")
            return False  # Erro no cadastro

    def verificar_login(self, login, senha):
        try:
            usuario = self.db.usuarios.find_one({"login": login})
            if usuario and bcrypt.checkpw(senha.encode(), usuario['senha']):
                return usuario['_id']
            else:
                return None
        except Exception as e:
            print(f"Erro verificando login do usuario: {e}")

    def armazenar_coins(self, usuario_id, coins):
        try:
            registro = {
                "usuario_id": usuario_id,
                "coins": coins,
                "data_hora": datetime.now()
            }
            self.db.coins.insert_one(registro)
            print("Coins registrados")
        except Exception as e:
            print(f"Erro ao armazenar coins no banco: {e}")

    def melhores_coins(self, usuario_id, limite=5):
        try:
            melhores_coins = self.db.coins.find({"usuario_id":usuario_id}).sort("coins", -1).limit(limite)
            return [(registro["coins"], registro["data_hora"]) for registro in melhores_coins]
        except Exception as e:
            print(f"Erro mostrando os melhores coins: {e}")
