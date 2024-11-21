import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import pygame
from Utils.database import BancoDeDados
from Scenes.login_tela import LoginTela
from Scenes.menu_tela import MenuTela

def main():
    pygame.init()
    tela = pygame.display.set_mode((1200, 750))
    pygame.display.set_caption("Pizzatron 3000")
    clock = pygame.time.Clock()
    banco = BancoDeDados("mongodb+srv://usertrabpoo:pizzatron3000@cluster0.ve3le.mongodb.net/?retryWrites=true&w=majority", "jogo")
    
    tela_atual = "login"
    login_tela = LoginTela(tela, banco)
    usuario = None
    menu_tela = None

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if tela_atual == "login":
                login_tela.handle_input(evento)
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                    usuario = login_tela.authenticate()
                    if usuario:
                        tela_atual = "menu"
                        menu_tela = MenuTela(tela, usuario)
            elif tela_atual == "menu" and menu_tela:
                acao = menu_tela.handle_input(evento)
                if acao == "play":
                    print("Iniciar jogo...")

        if tela_atual == "login":
            login_tela.draw()
        elif tela_atual == "menu" and menu_tela:
            menu_tela.draw()

        pygame.display.update()
        clock.tick(60)

main()