from database import BancoDeDados
from usuario import Usuario
import pygame
"""
banco = BancoDeDados("mongodb+srv://usertrabpoo:pizzatron3000@cluster0.ve3le.mongodb.net/?retryWrites=true&w=majority", "jogo")
usuario = Usuario(banco, "jogadorteste1", "senhateste1")
usuario.cadastrar()

usuario.fazer_login()

usuario.registrar_coins(501)

usuario.exibir_melhores_coins()
"""
pygame.init()

screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption("Pizzatron 3000")

background = pygame.image.load("Sprites/Backgrounds/BgMenuInicial.png")
background = pygame.transform.scale(background, (1200, 750))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    pygame.display.update()

pygame.quit()

