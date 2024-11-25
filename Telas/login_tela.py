import pygame
from Entities.usuario import Usuario
from Telas.tela import Tela

class LoginTela(Tela):
    def __init__(self, tela, banco):
        self.tela = tela
        self.banco = banco
        self.fonte = pygame.font.Font("Assets/BurbankSmallBold.ttf", 32)
        self.background = pygame.image.load("Assets/Backgrounds/MenuLogin.png")
        self.background = pygame.transform.scale(self.background, (1200, 750))
        self.input_ativo = {"login": False, "senha": False}
        self.inputs = {"login": "", "senha": ""}
        self.msg_erro = ""

    def draw(self): 
        self.tela.blit(self.background, (0, 0))
        login_box = self.fonte.render(f"Login: {self.inputs['login']}", True, (0, 0, 0))
        senha_box = self.fonte.render(f"Senha: {'*' * len(self.inputs['senha'])}", True, (0, 0, 0))
        erro_msg = self.fonte.render(self.msg_erro, True, (255, 0, 0))

        pygame.draw.rect(self.tela, (255, 255, 255), (300, 200, 300, 70))
        pygame.draw.rect(self.tela, (255, 255, 255), (300, 300, 300, 70))
        self.tela.blit(login_box, (310, 210))
        self.tela.blit(senha_box, (310, 310))
        self.tela.blit(erro_msg, (300, 400))

    def handle_input(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(300, 200, 200, 40).collidepoint(evento.pos):
                self.input_ativo["login"] = True
                self.input_ativo["senha"] = False
            elif pygame.Rect(300, 300, 200, 40).collidepoint(evento.pos):
                self.input_ativo["login"] = False
                self.input_ativo["senha"] = True
            else:
                self.input_ativo = {"login": False, "senha": False}

        if evento.type == pygame.KEYDOWN:
            if self.input_ativo["login"]:
                if evento.key == pygame.K_BACKSPACE:
                    self.inputs["login"] = self.inputs["login"][:-1]
                else:
                    self.inputs["login"] += evento.unicode
            elif self.input_ativo["senha"]:
                if evento.key == pygame.K_BACKSPACE:
                    self.inputs["senha"] = self.inputs["senha"][:-1]
                else:
                    self.inputs["senha"] += evento.unicode

    def authenticate(self):
        usuario = Usuario(self.banco, self.inputs["login"], self.inputs["senha"])
        usuario.fazer_login()
        if usuario.id:
            return usuario
        else:
            # Tentativa de cadastrar o usuario caso a conta nao exista
            print("Usuario nao encontrado. Tentando cadastrar...")
            usuario.cadastrar()
            usuario.fazer_login()  # Tenta login depois do cadastro
            if usuario.id:
                return usuario
            else:
                self.msg_erro = "Erro ao cadastrar ou autenticar usuario."
                return None
