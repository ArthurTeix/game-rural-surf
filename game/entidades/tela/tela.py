import pygame
from pathlib import Path

# configurações da tela
tamanho_tela = (462, 606)
largura_tela, altura_tela = tamanho_tela
tela = pygame.display.set_mode(tamanho_tela)

raiz_projeto = Path(__file__).resolve().parents[3]  # sobe 3 níveis
caminho_fundo = raiz_projeto / "src" / "img" / "telas" / "background.png"

# carrega a imagem de fundo
fundo = pygame.image.load(caminho_fundo)
