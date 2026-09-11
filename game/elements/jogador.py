import pygame
from pathlib import Path


class Jogador:
    def __init__(self, largura_tela, x=231, y=470, largura=57, altura=114, velocidade=1):
        self.largura_tela = largura_tela
        self.largura = largura
        self.altura = altura
        self.velocidade = velocidade

        self.rect = pygame.Rect(x, y, largura, altura)

        # carrega e redimensiona a imagem
        raiz_projeto = Path(__file__).resolve().parents[3]  # sobe 3 níveis
        caminho_img = raiz_projeto / "src" / "img" / "personagens" / "Robozin.png"

        self.imagem = pygame.image.load(str(caminho_img)).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (largura, altura))

    def mover(self):
        tecla = pygame.key.get_pressed()

        if (tecla[pygame.K_RIGHT] or tecla[pygame.K_d]) and self.rect.x < self.largura_tela - self.largura:
            self.rect.x += self.velocidade

        if (tecla[pygame.K_LEFT] or tecla[pygame.K_a]) and self.rect.x > 0:
            self.rect.x -= self.velocidade

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)
