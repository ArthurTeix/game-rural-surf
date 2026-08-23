import pygame
from game.entidades.tela.func_tela import desenhar_inicio_jogo
from game.entidades.jogador.func_jogador import movimento_jogador
from game.entidades.obstaculo.func_obstaculo import criar_obstaculo, mover_obstaculos, verificar_colisao_obstaculo
from game.entidades.obstaculo.obstaculo import criar_obstaculos

pygame.init()

# título do jogo
pygame.display.set_caption("RURAL RUN")

fim_de_jogo = False
while not fim_de_jogo:
    desenhar_inicio_jogo()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_de_jogo = True

        if evento.type == criar_obstaculos:
            quantidade_por_vez = 2
            for quant in range(quantidade_por_vez):
                criar_obstaculo()

    movimento_jogador(evento)

    mover_obstaculos()

    if verificar_colisao_obstaculo():
        fim_de_jogo = True

    pygame.time.wait(1)
    pygame.display.flip()

pygame.quit()
