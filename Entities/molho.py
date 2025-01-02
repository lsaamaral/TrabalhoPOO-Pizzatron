import pygame

class Molho():
    def __init__(self, tela, endereco_img, escala):
        self.tela = tela
        self.carregar_img = pygame.image.load(endereco_img)
        self.molho = pygame.transform.scale(self.carregar_img, escala)

        self.current_frame = 0
        self.frame_timer = 0
        self.frame_interval = 100  # Intervalo em milissegundos entre frames
        self.num_frames = 0

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
            gif_y = y + img_altura // 2 # Ajusta para baixo do molho
            self.tela.blit(molho_frames[self.current_frame], (gif_x + offset_x, gif_y + offset_y))

            # Atualiza o frame do GIF
            self.frame_timer += pygame.time.get_ticks()
            if self.frame_timer > self.frame_interval:
                self.current_frame = (self.current_frame + 1) % self.num_frames
                self.frame_timer = 0

