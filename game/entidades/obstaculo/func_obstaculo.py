from game.entidades.obstaculo.obstaculo import altura_obstaculo, largura_obstaculo, lista_obstaculos, velocidade_obstaculo
from random import randint
import pygame
from ..tela.tela import altura_tela
from ..jogador.jogador import jogador


def criar_obstaculo():
    x = randint(15, 405)  # obstaculos nascem aleatoriamente entre o px 30 e 405 de largura
    novo_obstaculo = pygame.Rect(x, -altura_obstaculo, largura_obstaculo, altura_obstaculo)
    lista_obstaculos.append(novo_obstaculo)


def mover_obstaculos():
    for obstaculo in lista_obstaculos:
        obstaculo.y += velocidade_obstaculo

    # remove obstáculos que já saíram da tela
    lista_obstaculos[:] = [obstaculo for obstaculo in lista_obstaculos if obstaculo.y < altura_tela]


def verificar_colisao_obstaculo():
    for obstaculo in lista_obstaculos:
        if jogador.colliderect(obstaculo):
            return True
    return False