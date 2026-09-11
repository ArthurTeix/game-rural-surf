import pygame


# configurações da tela
LARGURA_TELA = 462
ALTURA_TELA = 606

IMG_FUNDOS = [
    pygame.image.load('./img/telas/fundo-teste.png')
]

# título do jogo
TITULO_JOGO = "RURAL SURF"

IMG_PERSONAGENS = [
    pygame.image.load('./img/personagens/personagem-teste.png')
]

# mensagens do jogo
pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)
