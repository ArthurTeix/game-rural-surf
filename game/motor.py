import pygame

from game.elements.personagem import Personagem
from game.elements.obstaculo import GerenciadorObstaculos
from game.render import desenhar_jogo
from game.configuracoes import LARGURA_TELA, ALTURA_TELA, TITULO_JOGO


class Motor:
    FPS = 45

    def __init__(self):
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption(TITULO_JOGO)

        self.watch = pygame.time.Clock()
        self.rodando = True
        self.pontos = 0

        # velocidade em pixels por frame (a 30 FPS, velocidade=5 -> 150px/segundo)
        self.personagem = Personagem(LARGURA_TELA, velocidade=7)

        self.gerenciador_obstaculos = GerenciadorObstaculos(
            largura_tela=LARGURA_TELA,
            altura_tela=ALTURA_TELA,
            velocidade=5,
            intervalo_ms=1800
        )

    def jogo(self):
        while self.rodando:
            self.watch.tick(self.FPS)

            self.capturar_eventos_e_movimento()
            self.atualizar_obstaculos()

            desenhar_jogo(self.tela, self.personagem, self.gerenciador_obstaculos, self.pontos)

    def capturar_eventos_e_movimento(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.encerrar_jogo()

            if evento.type == self.gerenciador_obstaculos.EVENTO_CRIAR_OBSTACULO:
                self.gerenciador_obstaculos.criar_obstaculo()

        self.personagem.mover()

    def atualizar_obstaculos(self):
        obstaculos_que_sairam = self.gerenciador_obstaculos.mover_obstaculos()
        self.pontos += obstaculos_que_sairam

        if self.gerenciador_obstaculos.verificar_colisao(self.personagem):
            self.encerrar_jogo()

    def encerrar_jogo(self):
        self.rodando = False
        pygame.quit()
        quit()
