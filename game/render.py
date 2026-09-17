import pygame

from game.configuracoes import IMG_FUNDOS, LARGURA_TELA, FONTE_PONTOS
from game.ui.botao import botao_jogar, botao_ranking, botao_perfil, botao_sair
from game.util.cores import cores

def desenhar_jogo(tela, personagem, gerenciador_obstaculos, pontos):
    # desenha o fundo primeiro, pra ele ficar "atrás" de tudo
    tela.blit(IMG_FUNDOS[0], (0, 0))

    # desenha o personagem
    personagem.desenhar(tela)

    # desenha todos os obstáculos que estão na tela
    gerenciador_obstaculos.desenhar_obstaculos(tela)

    # desenha o texto com a pontuação, no canto superior direito
    texto_pontos = FONTE_PONTOS.render(f"Pontuação: {pontos}", 1, cores['amarelo'])
    tela.blit(texto_pontos, (LARGURA_TELA - 10 - texto_pontos.get_width(), 10))

    # atualiza a tela pra mostrar tudo que foi desenhado
    pygame.display.update()


def desenhar_menu(tela):
    tela.fill((50, 150, 200))
    botao_jogar.desenhar(tela)
    botao_ranking.desenhar(tela)
    botao_perfil.desenhar(tela)
    botao_sair.desenhar(tela)
    pygame.display.update()
