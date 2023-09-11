import random
""""
    Utilizaremos listas para representar o tabuleiro e as jogadas dos jogadores.
    Cada posição do tabuleiro será representada por um int.
    O jogador 1 será representado pelo número 1 e o jogador 2 pelo número 2.
    O tabuleiro será uma lista de listas, onde cada lista interna representa uma linha do tabuleiro.
    As jogadas dos jogadores serão armazenadas em uma lista de tuplas, onde cada tupla contém as coordenadas da jogada.
    A função principal do jogo será responsável por alternar entre os jogadores, receber as jogadas e verificar o vencedor.

    estruturalmente utilizamos:
    especificamente no tabuleiro: lista de listas, onde cada lista interna representa uma linha do tabuleiro.
    para as jogadas: lista de tuplas, onde cada tupla contém as coordenadas da jogada.
"""
"""
    Função principal, a main do jogo da velha.
    Permite escolher entre jogar contra um segundo jogador ou contra a máquina.
"""
def jogo_da_velha():

    print("Bem-vindo ao Jogo da Velha 4x4!")

    while True:
        modo_jogo = input("Escolha o modo de jogo (1 para dois jogadores, 2 para jogar contra a máquina): ")
        
        if modo_jogo == "1":
            jogar_dois_jogadores()
            break
        elif modo_jogo == "2":
            jogar_contra_maquina()
            break
        else:
            print("Escolha uma opção válida (1 ou 2).")
"""
    Imprime o tabuleiro atual.
"""
def imprimir_tabuleiro(tabuleiro):

    print("\nTabuleiro:")
    for linha in tabuleiro:
        print(" | ".join(["X" if posicao == 1 else "O" if posicao == 2 else " " for posicao in linha]))
        print("-" * 13)
"""
    Permite que dois jogadores joguem um contra o outro.
"""
def jogar_dois_jogadores():

    tabuleiro = [[0, 0, 0, 0] for _ in range(4)]
    jogadas = []
    jogador_atual = 1
    num_jogadas = 0

    while True:
        imprimir_tabuleiro(tabuleiro)
        if jogador_atual == 1:
            jogada = receber_jogada(jogador_atual)
        else:
            jogada = receber_jogada(jogador_atual)
        
        if not verificar_jogada_valida(jogada, tabuleiro):
            print("Jogada inválida. Tente novamente.")
            continue

        tabuleiro[jogada[0]][jogada[1]] = jogador_atual
        jogadas.append(jogada)

        if verificar_vencedor(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        if num_jogadas == 16:
            imprimir_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            break

        jogador_atual = 2 if jogador_atual == 1 else 1
        num_jogadas += 1
"""
    Permite que um jogador jogue contra a máquina.
"""
def jogar_contra_maquina():

    tabuleiro = [[0, 0, 0, 0] for _ in range(4)]
    jogadas = []
    jogador_atual = 1
    num_jogadas = 0

    while True:
        imprimir_tabuleiro(tabuleiro)

        if jogador_atual == 1:
            jogada = receber_jogada(jogador_atual)

            if not verificar_jogada_valida(jogada, tabuleiro):
                print("Jogada inválida. Tente novamente.")
                continue
        else:
            jogada = fazer_jogada_maquina(tabuleiro)
            print(f"A máquina jogou na linha {jogada[0]} e coluna {jogada[1]}.")

        tabuleiro[jogada[0]][jogada[1]] = jogador_atual
        jogadas.append(jogada)

        if verificar_vencedor(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            if jogador_atual == 1:
                print("Você venceu!")
            else:
                print("A máquina venceu!")
            break

        if num_jogadas == 16:
            imprimir_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            break

        jogador_atual = 2 if jogador_atual == 1 else 1
        num_jogadas += 1
"""
    Faz a jogada da máquina, escolhendo uma posição aleatória no tabuleiro vazio.
    Retorna as coordenadas da jogada como uma tupla (linha, coluna).
"""
def fazer_jogada_maquina(tabuleiro):

    while True:
        linha = random.randint(0, 3)
        coluna = random.randint(0, 3)
        if tabuleiro[linha][coluna] == 0:
            return linha, coluna
"""
    Recebe a jogada do jogador atual.
    Retorna as coordenadas da jogada como uma tupla (linha, coluna).
"""
def receber_jogada(jogador_atual):

    print(f"Jogador {jogador_atual}, é sua vez.")
    while True:
        try:
            linha = int(input("Digite a linha da sua jogada (0-3): "))
            coluna = int(input("Digite a coluna da sua jogada (0-3): "))
            if 0 <= linha <= 3 and 0 <= coluna <= 3:
                return linha, coluna
            else:
                print("Coordenadas fora do intervalo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
"""
    Verifica se a jogada é válida.
    Retorna True se a jogada é válida, False caso contrário.
"""
def verificar_jogada_valida(jogada, tabuleiro):

    linha, coluna = jogada
    if linha < 0 or linha > 3 or coluna < 0 or coluna > 3:
        return False
    if tabuleiro[linha][coluna] != 0:
        return False
    return True
"""
    Verifica se há um vencedor.
    Retorna True se há um vencedor, False caso contrário.
"""
def verificar_vencedor(tabuleiro):

    for linha in tabuleiro:
        if linha.count(1) == 4 or linha.count(2) == 4:
            return True

    for coluna in range(4):
        if [tabuleiro[linha][coluna] for linha in range(4)].count(1) == 4 or [tabuleiro[linha][coluna] for linha in range(4)].count(2) == 4:
            return True

    if [tabuleiro[i][i] for i in range(4)].count(1) == 4 or [tabuleiro[i][i] for i in range(4)].count(2) == 4:
        return True

    if [tabuleiro[i][3-i] for i in range(4)].count(1) == 4 or [tabuleiro[i][3-i] for i in range(4)].count(2) == 4:
        return True

    return False

"""chamada dafunção principal que chama as outras funções para o perfeito funcionamento da main """
jogo_da_velha()