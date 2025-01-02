import pygame
import random

class Pizza():
    def __init__(self):
        '''
        Classe base para a pizza
        '''

    def adicionar_ingrediente(self, ingrediente, quantidade):
        '''
        Adiciona quantidade de ingrediente na pizza
        '''
        if ingrediente in self.ingredientes and ingrediente != "queijo":
            self.ingredientes[ingrediente] += quantidade


class PizzaCardapio(Pizza):
    def __init__(self):
        '''
        Classe para a pizza do cardapio
        '''
        self.molho = random.choice(["tomate", "hot"])
        self.ingredientes = {"queijo": True, "alga": 0, "camarao": 0, "lula": 0, "peixe": 0}
        
        if self.molho == "tomate":
            self.sprite = pygame.image.load("Assets/Cardapio/Tomate.png")
        elif self.molho == "hot":
            self.sprite = pygame.image.load("Assets/Cardapio/Hot.png")
        self.sprite = pygame.transform.scale(self.sprite, (150, 98))
        self.nome = self.gerar_nome()
        self.pizzas_feitas = 0
        self.pizzas_restantes = 40
        self.erros = 0
        self.moedas = 0

    def gerar_pizza(self, nivel):
        if nivel <= 4:
            return

        ingredientes_possiveis = ["alga", "camarao", "lula", "peixe"]
        ingredientes_diferentes = random.randint(1, 3)
        ingredientes_escolhidos = random.sample(ingredientes_possiveis, ingredientes_diferentes)

        for ingrediente in ingredientes_escolhidos:
            quantidade = random.choice([2, 5])
            self.adicionar_ingrediente(ingrediente, quantidade)

    def gerar_nome(self):
        '''
        Gera o nome da pizza de acordo com os ingredientes
        '''
        ingredientes_extras = [ingrediente for ingrediente, quantidade in self.ingredientes.items() if ingrediente != "queijo" and quantidade > 0]
        if len(ingredientes_extras) == 1:
            return f"Pizza de {ingredientes_extras[0]}"
        elif len(ingredientes_extras) == 2:
            return f"Pizza de {ingredientes_extras[0]} e {ingredientes_extras[1]}"
        elif len(ingredientes_extras) == 3:
            return f"Pizza de {', '.join(ingredientes_extras[:-1])} e {ingredientes_extras[-1]}"
        else:
            return "Pizza de queijo"
        
    def adicionar_ingrediente(self, ingrediente, quantidade):
        '''
        Adiciona ingredientes e atualiza o nome da pizza
        '''
        super().adicionar_ingrediente(ingrediente, quantidade)
        self.nome = self.gerar_nome()

    def desenhar(self, tela):
        '''
        Desenha o cardapio da tela
        '''
        fonte_titulo = pygame.font.Font("Assets/BurbankSmallBold.ttf", 26)
        fonte_texto = pygame.font.Font("Assets/BurbankSmallBold.ttf", 20)
        fonte_moedas = pygame.font.Font("Assets/BurbankSmallBold.ttf", 30)
        azul_escuro = (0, 0, 139)
        preto = (0, 0, 0)
        rosa_claro = (255, 235, 238)

        texto_nome = fonte_titulo.render(self.nome, True, azul_escuro)
        tela.blit(texto_nome, (640, 55))

        tela.blit(self.sprite, (670, 110))

        y_offset = 180
        texto_molho = fonte_texto.render(f"Molho {self.molho.capitalize()}", True, azul_escuro)
        tela.blit(texto_molho, (850, 160))
        for ingrediente, quantidade in self.ingredientes.items():
            if ingrediente != "queijo" and quantidade > 0:
                texto_ingrediente = fonte_texto.render(f"{ingrediente.capitalize()}: {quantidade}", True, azul_escuro)
                tela.blit(texto_ingrediente, (850, y_offset))
                y_offset += 20

        x_offset = 610
        for ingrediente, quantidade in self.ingredientes.items():
            if ingrediente != "queijo" and quantidade > 0:
                if ingrediente == "alga":
                    sprite_ingrediente = pygame.image.load("Assets/Ingredientes/Alga1.png")
                elif ingrediente == "camarao":
                    sprite_ingrediente = pygame.image.load("Assets/Ingredientes/Camarao1.png")
                elif ingrediente == "lula":
                    sprite_ingrediente = pygame.image.load("Assets/Ingredientes/Lula1.png")
                elif ingrediente == "peixe":
                    sprite_ingrediente = pygame.image.load("Assets/Ingredientes/Peixe1.png")
                sprite_ingrediente = pygame.transform.scale(sprite_ingrediente, (140, 170))
                tela.blit(sprite_ingrediente, (x_offset, 185))
                x_offset += 85

        texto_pizzas_feitas = fonte_texto.render(f"Pizzas Feitas: {self.pizzas_feitas}", True, preto)
        texto_pizzas_restantes = fonte_texto.render(f"Pizzas Restantes: {self.pizzas_restantes}", True, preto)
        texto_erros = fonte_texto.render(f"Erros: {self.erros}", True, preto)
        pygame.draw.rect(tela, rosa_claro, pygame.Rect(877, 90, 215, 70))
        tela.blit(texto_pizzas_feitas, (882, 90))
        tela.blit(texto_pizzas_restantes, (882, 110))
        tela.blit(texto_erros, (882, 130))

        texto_moedas = fonte_moedas.render(f"Moedas: {self.moedas}", True, preto)
        tela.blit(texto_moedas, (910, 290))


class PizzaUsuario(Pizza):
    def __init__(self):
        self.borda_sprite = pygame.transform.scale(pygame.image.load("Assets/Pizza/Borda.png"), (295, 192))
        self.massa_sprite = pygame.transform.scale(pygame.image.load("Assets/Pizza/Massa.png"), (295, 192))
        self.ingredientes = self.criar_lista_ingredientes()
        self.queijo_sprite = None
        self.posicao = [-270, 540]
        self.velocidade = 5
        self.raio = 100

        self.raio_x = (self.massa_sprite.get_width()) // 2
        self.raio_y = (self.massa_sprite.get_height()) // 2
    
    def criar_lista_ingredientes(self):
        return {"molho": None, "queijo": False, "alga": [], "camarao": [], "lula": [], "peixe": []}
    
    def mover(self):
        self.posicao[0] += self.velocidade
    
    def esta_fora_da_tela(self):
        return self.posicao[0] > 1350

    def desenhar(self, tela):
        tela.blit(self.massa_sprite, self.posicao)
        if self.queijo_sprite:
            tela.blit(self.queijo_sprite, self.posicao)
        tela.blit(self.borda_sprite, self.posicao)

    def esta_sobre(self, pos_mouse):
        dx = pos_mouse[0] - (self.posicao[0] + self.raio_x -40)
        dy = pos_mouse[1] - (self.posicao[1] + self.raio_y -40)
        
        return (dx**2 / self.raio_x**2) + (dy**2 / self.raio_y**2) <= 1
    
    def resetar(self):
        self.posicao = [-270, 540]
        self.ingredientes = self.criar_lista_ingredientes()
        self.queijo_sprite = None

