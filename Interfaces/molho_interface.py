from abc import ABC, abstractmethod

class InterfaceMolho(ABC):
    @abstractmethod
    def animation(self, endereco_sprite: str, frame_width: int, frame_height: int, numero_frames: int)-> list:
        ''' Cria a lista de frames da animacao do molho que sai dos frascos '''
        pass

    @abstractmethod
    def draw_animation(self, imagem: str, pos_mouse: list, offset_x: int, offset_y: int, molho_frames: int)-> None:
        ''' Desenha a animacao dos frascos na tela '''
        pass
