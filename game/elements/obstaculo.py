import pygame
from random import randint


class Obstaculo:
    # imagem compartilhada entre todas as instâncias (carregada só uma vez)
    _imagem = None

    def __init__(self, x, y, largura, altura):
        self.rect = pygame.Rect(x, y, largura, altura)

        if Obstaculo._imagem is None:
            imagem = pygame.image.load('./img/elementos/obstaculos.png').convert_alpha()
            Obstaculo._imagem = pygame.transform.scale(imagem, (largura, altura))

        self.imagem = Obstaculo._imagem

    def mover(self, velocidade):
        self.rect.y += velocidade

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)


class GerenciadorObstaculos:
    EVENTO_CRIAR_OBSTACULO = pygame.USEREVENT + 1

    def __init__(
        self,
        largura_tela,
        altura_tela,
        largura=80,
        altura=40,
        velocidade=3,
        intervalo_ms=1400
    ):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.largura = largura
        self.altura = altura
        self.velocidade = velocidade
        self.lista_obstaculos = []

        # Avisa o pygame para disparar um evento automaticamente
        pygame.time.set_timer(
            self.EVENTO_CRIAR_OBSTACULO,
            intervalo_ms
        )

    def criar_obstaculo(self):
        metade_da_tela = self.largura_tela // 2
        margem = 15

        x_do_obstaculo_esquerdo = randint(
            margem,
            metade_da_tela - self.largura
        )

        x_do_obstaculo_direito = randint(
            metade_da_tela,
            self.largura_tela - self.largura - margem
        )

        obstaculo_esquerdo = Obstaculo(
            x_do_obstaculo_esquerdo,
            -self.altura,
            self.largura,
            self.altura
        )

        obstaculo_direito = Obstaculo(
            x_do_obstaculo_direito,
            -self.altura,
            self.largura,
            self.altura
        )

        self.lista_obstaculos.append(obstaculo_esquerdo)
        self.lista_obstaculos.append(obstaculo_direito)

    def mover_obstaculos(self):
        for obstaculo in self.lista_obstaculos:
            obstaculo.mover(self.velocidade)

        # Remove obstáculos que saíram da tela
        obstaculos_ainda_visiveis = []
        obstaculos_que_sairam = 0

        for obstaculo in self.lista_obstaculos:
            if obstaculo.rect.y < self.altura_tela:
                obstaculos_ainda_visiveis.append(obstaculo)
            else:
                obstaculos_que_sairam += 1

        self.lista_obstaculos = obstaculos_ainda_visiveis

        return obstaculos_que_sairam

    def desenhar_obstaculos(self, tela):
        for obstaculo in self.lista_obstaculos:
            obstaculo.desenhar(tela)

    def verificar_colisao(self, jogador):
        for obstaculo in self.lista_obstaculos:
            if jogador.rect.colliderect(obstaculo.rect):
                return True

        return False
