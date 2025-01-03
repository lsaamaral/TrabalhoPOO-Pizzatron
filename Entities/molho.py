import pygame

import pygame

class Molho():
    def __init__(self, tela, endereco_img, escala):
        self.tela = tela
        try:
            self.carregar_img = pygame.image.load(endereco_img)
            self.molho = pygame.transform.scale(self.carregar_img, escala)
        except pygame.error as e:
            print(f"Erro ao carregar a imagem: {endereco_img}\n{e}")
            raise

        self.current_frame = 0
        self.frame_timer = 0
        self.frame_interval = 100  # Intervalo em milissegundos entre frames
        self.num_frames = 0

        # Adições para pintura e preenchimento
        self.escala = escala
        self.molho_surface = pygame.Surface(escala, pygame.SRCALPHA)  # Superfície para pintura
        self.mask_surface = pygame.Surface(escala, pygame.SRCALPHA)  # Máscara circular
        pygame.draw.circle(self.mask_surface, (255, 255, 255), (escala[0] // 2, escala[1] // 2), escala[0] // 2)
        self.molho_mask = pygame.mask.from_surface(self.mask_surface)  # Máscara binária
        self.pixels_totais = self.molho_mask.count()  # Pixels totais da máscara
        self.pixels_preenchidos = 0
        self.molho_completo = False
        self.molho_sprite = pygame.image.load("Assets/Pizza/Tomate_Pingando.png")
        self.molho_sprite = pygame.transform.scale(self.molho_sprite, (15, 15))
        self.limite_preenchimento = 0.7  # 70% para completar

    def get_molho(self):
        return self.molho

    def get_width(self):
        return self.molho.get_width()
    
    def get_height(self):
        return self.molho.get_height()

    def get_current_frame(self):
        return self.current_frame

    def animation(self, endereco_sprite, frame_width, frame_height, numero_frames):
        self.num_frames = numero_frames
        self.molho_spritesheet = pygame.image.load(endereco_sprite)

        self.molho_frames = [
            self.molho_spritesheet.subsurface(pygame.Rect(x * frame_width, 0, frame_width, frame_height))
            for x in range(numero_frames)
        ]
        return self.molho_frames

    
    def draw_animation(self, imagem, pos_mouse, offset_x, offset_y, molho_frames):
        img_largura, img_altura = imagem.get_size()
        x, y = pos_mouse[0] - img_largura // 2, pos_mouse[1] - img_altura // 2
        self.tela.blit(imagem, (x, y))

        if molho_frames:
            gif_x = x
            gif_y = y + img_altura // 2  # Ajusta para baixo do molho
            self.tela.blit(molho_frames[self.current_frame], (gif_x + offset_x, gif_y + offset_y))

            # Atualiza o frame do GIF
            self.frame_timer += pygame.time.get_ticks()
            if self.frame_timer > self.frame_interval:
                self.current_frame = (self.current_frame + 1) % self.num_frames
                self.frame_timer = 0

    def pintar(self, pos_mouse, pizza_pos):
        """
        Aplica molho na posição indicada pelo mouse.
        """
        if not self.molho_completo:
            rel_x = pos_mouse[0] - pizza_pos[0]
            rel_y = pos_mouse[1] - pizza_pos[1]

            # Verifica se está dentro da máscara
            if 0 <= rel_x < self.escala[0] and 0 <= rel_y < self.escala[1] and self.molho_mask.get_at((rel_x, rel_y)):
                pygame.draw.circle(self.molho_surface, (255, 0, 0, 255), (rel_x, rel_y), 10)
                self.molho_surface.blit(self.molho_sprite, (rel_x - 15, rel_y - 15))
                
                # Calcula pixels preenchidos
                self.pixels_preenchidos = sum(
                    1 for y in range(self.escala[1])
                    for x in range(self.escala[0])
                    if self.molho_mask.get_at((x, y)) and self.molho_surface.get_at((x, y))[3] > 0
                )

                if self.pixels_preenchidos / self.pixels_totais >= self.limite_preenchimento:
                    self.molho_completo = True
                    self.preencher_completo()

    def desenhar(self, tela, pizza_pos):
        """
        Desenha o molho na tela, na posição da pizza.
        """
        tela.blit(self.molho_surface, pizza_pos)

        def preencher_completo(self):
            """
            Preenche automaticamente a área restante com molho.
            """
            self.molho_surface.fill((0, 0, 0, 0))  # Limpa
            pygame.draw.circle(self.molho_surface, (200, 0, 0, 200), (self.escala[0] // 2, self.escala[1] // 2), self.escala[0] // 2)

    def desenhar(self, tela, pizza_pos):
        """
        Desenha o molho na tela, na posição da pizza.
        """
        tela.blit(self.molho_surface, pizza_pos)
