import pygame
from pathlib import Path

# configurações do jogador
largura_jogador = 57
altura_jogador = 114
velocidade_jogador = 1
jogador = pygame.Rect(231, 470, largura_jogador, altura_jogador)

raiz_projeto = Path(__file__).resolve().parents[3]  # sobe 3 níveis
caminho_img = raiz_projeto / "src" / "img" / "personagens" / "Robozin.png"

jogador_img = pygame.image.load(str(caminho_img)).convert_alpha()

# redimensiona a imagem pro tamanho do retângulo do jogador
jogador_img = pygame.transform.scale(jogador_img, (largura_jogador, altura_jogador))
