from database import BancoDeDados
from usuario import Usuario

banco = BancoDeDados("mongodb+srv://usertrabpoo:pizzatron3000@cluster0.ve3le.mongodb.net/?retryWrites=true&w=majority", "jogo")
usuario = Usuario(banco, "jogadorteste1", "senhateste1")
usuario.cadastrar()

usuario.fazer_login()

usuario.registrar_coins(501)

usuario.exibir_melhores_coins()