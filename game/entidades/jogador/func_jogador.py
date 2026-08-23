import pygame
from ..jogador.jogador import jogador, largura_jogador, velocidade_jogador
from ..tela.tela import largura_tela


def movimento_jogador(evento):
    tecla = pygame.key.get_pressed()

    if (tecla[pygame.K_RIGHT] or tecla[pygame.K_d]) and jogador.x < largura_tela - largura_jogador: 
        jogador.x += velocidade_jogador

    if (tecla[pygame.K_LEFT] or tecla[pygame.K_a]) and jogador.x > 0:
        jogador.x -= velocidade_jogador
