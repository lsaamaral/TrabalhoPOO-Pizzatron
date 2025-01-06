import pygame

class FinalTela:
    def __init__(self, tela, resultado):
        self.tela = tela
        self.resultado = resultado

    def handle_input(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_m:  # Voltar ao menu
                return "menu"
            elif evento.key == pygame.K_q:  # Sair do jogo
                return "sair"
        return None

    def draw(self):
        self.tela.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        if self.resultado == "vitoria":
            texto = "Parabéns! Você ganhou!"
            cor = (0, 255, 0)
        else:
            texto = "Você perdeu! Tente novamente!"
            cor = (255, 0, 0)
        mensagem = font.render(texto, True, cor)
        self.tela.blit(mensagem, (self.tela.get_width() // 2 - mensagem.get_width() // 2,
                                  self.tela.get_height() // 2 - mensagem.get_height() // 2))
        instrucoes = font.render("M: Menu | Q: Sair", True, (255, 255, 255))
        self.tela.blit(instrucoes, (self.tela.get_width() // 2 - instrucoes.get_width() // 2,
                                    self.tela.get_height() // 2 + mensagem.get_height()))
