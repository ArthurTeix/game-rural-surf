import pygame
from pathlib import Path

# configurações dos obstáculos
largura_obstaculo = 80
altura_obstaculo = 40
velocidade_obstaculo = 1

lista_obstaculos = []  # cada obstáculo é um pygame.Rect

raiz_projeto = Path(__file__).resolve().parents[3]  # sobe 3 níveis
caminho_img = raiz_projeto / "src" / "img" / "elementos" / "obstaculos.png"

obstaculo_img = pygame.image.load(str(caminho_img)).convert_alpha()

# redimensiona a imagem para sempre estar alinhada
obstaculo_img = pygame.transform.scale(obstaculo_img, (largura_obstaculo, altura_obstaculo))

# criar obstáculos periodicamente
criar_obstaculos = pygame.USEREVENT + 1
pygame.time.set_timer(criar_obstaculos, 700)  # a cada 0.7seg
