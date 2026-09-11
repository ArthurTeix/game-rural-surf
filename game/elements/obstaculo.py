import pygame
from pathlib import Path
from random import randint


class Obstaculo:
    # imagem compartilhada entre todas as instâncias (carregada só uma vez)
    _imagem = None

    def __init__(self, x, y, largura, altura):
        self.rect = pygame.Rect(x, y, largura, altura)

        if Obstaculo._imagem is None:
            raiz_projeto = Path(__file__).resolve().parents[3]  # sobe 3 níveis
            caminho_img = raiz_projeto / "src" / "img" / "elementos" / "obstaculos.png"

            imagem = pygame.image.load(str(caminho_img)).convert_alpha()
            Obstaculo._imagem = pygame.transform.scale(imagem, (largura, altura))

        self.imagem = Obstaculo._imagem

    def mover(self, velocidade):
        self.rect.y += velocidade

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)


class GerenciadorObstaculos:
    EVENTO_CRIAR_OBSTACULO = pygame.USEREVENT + 1

    def __init__(self, altura_tela, largura=80, altura=40, velocidade=1, intervalo_ms=700):
        self.altura_tela = altura_tela
        self.largura = largura
        self.altura = altura
        self.velocidade = velocidade

        self.lista_obstaculos = []

        # criar obstáculos periodicamente
        pygame.time.set_timer(self.EVENTO_CRIAR_OBSTACULO, intervalo_ms)

    def criar_obstaculo(self):
        x = randint(15, 405)  # obstáculos nascem aleatoriamente entre o px 15 e 405 de largura
        novo_obstaculo = Obstaculo(x, -self.altura, self.largura, self.altura)
        self.lista_obstaculos.append(novo_obstaculo)

    def mover_obstaculos(self):
        for obstaculo in self.lista_obstaculos:
            obstaculo.mover(self.velocidade)

        # remove obstáculos que já saíram da tela
        self.lista_obstaculos[:] = [
            obstaculo for obstaculo in self.lista_obstaculos
            if obstaculo.rect.y < self.altura_tela
        ]

    def desenhar_obstaculos(self, tela):
        for obstaculo in self.lista_obstaculos:
            obstaculo.desenhar(tela)

    def verificar_colisao(self, jogador):
        for obstaculo in self.lista_obstaculos:
            if jogador.rect.colliderect(obstaculo.rect):
                return True
        return False
