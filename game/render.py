def desenhar_inicio_jogo():
    tela.blit(fundo, (0, 0))

    # desenhando jogador na tela
    tela.blit(jogador_img, jogador)

    # desenhando os obstáculos na tela
    for obstaculo in lista_obstaculos:
        tela.blit(obstaculo_img, obstaculo)
