import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import pygame
from Utils.database import BancoDeDados
from Telas.login_tela import LoginTela
from Telas.menu_tela import MenuTela
from Telas.jogo_tela import JogoTela
from Telas.ingredientes_manager import IngredientesManager

def main():
    pygame.init()
    tela = pygame.display.set_mode((1200, 750))
    pygame.display.set_caption("Pizzatron 3000")
    clock = pygame.time.Clock()
    pos_mouse = pygame.mouse.get_pos()


    banco = BancoDeDados(
        "mongodb+srv://usertrabpoo:pizzatron3000@cluster0.ve3le.mongodb.net/?retryWrites=true&w=majority",
        "jogo"
    )

  
    tela_atual = "login"
    login_tela = LoginTela(tela, banco)
    usuario = None
    menu_tela = None
    jogo_tela = None
    ingredientes_manager = None  

    
    carregando_ingrediente = False
    ingrediente_atual = None
    pos_mouse = (0, 0)

    while True:
        tela.fill((255, 255, 255))
        pos_mouse = pygame.mouse.get_pos()  
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
                    tela_atual = "jogo"
                    jogo_tela = JogoTela(tela)
                    ingredientes_manager = IngredientesManager(tela)  
                elif acao == "logout":
                    usuario = None
                    tela_atual = "login"
            elif tela_atual == "jogo" and jogo_tela:
                jogo_tela.handle_input(evento)
                

                
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  
                    ingrediente_atual = ingredientes_manager.get_ingrediente_em_clique(pos_mouse)
                    if ingrediente_atual:
                        carregando_ingrediente = True

                
                if evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
                    carregando_ingrediente = False
                    ingrediente_atual = None

                if not jogo_tela.running:  
                    tela_atual = "menu"

        
        if tela_atual == "login":
            login_tela.draw()
        elif tela_atual == "menu" and menu_tela:
            menu_tela.draw()
        elif tela_atual == "jogo" and jogo_tela:
            jogo_tela.draw()
            ingredientes_manager.draw()  

            
            if carregando_ingrediente and ingrediente_atual:
                img_width, img_height = ingrediente_atual.get_size()
                x, y = pos_mouse[0] - img_width // 2, pos_mouse[1] - img_height // 2
                tela.blit(ingrediente_atual, (x, y))

        
        pygame.display.update()
        clock.tick(60)


main()
