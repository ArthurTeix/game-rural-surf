import pygame


class Botao:
    def __init__(self, imagem_inicial, centro, imagem_hover=None):
        self.imagem = pygame.image.load(imagem_inicial).convert_alpha()
        self.imagem_hover = pygame.image.load(imagem_hover).convert_alpha() if imagem_hover else self.imagem
        self.rect = self.imagem.get_rect(center=centro)

    def desenhar(self, tela):
        tela.blit(self.obter_imagem_atual(), self.rect)

    def obter_imagem_atual(self):
        return self.imagem_hover if self.esta_em_hover() else self.imagem

    def esta_em_hover(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def clicado(self, pos_clique):
        return self.rect.collidepoint(pos_clique)
