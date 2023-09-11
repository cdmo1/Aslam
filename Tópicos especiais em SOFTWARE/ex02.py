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

    print("Bem-vindo ao Jogo da Velha NxN!")

    while True:
        tamanho_tabuleiro = int(input("Digite o tamanho do tabuleiro (NxN): "))
        
        if tamanho_tabuleiro < 2:
            print("O tamanho do tabuleiro deve ser pelo menos 2x2. Tente novamente.")
            continue
        
        modo_jogo = input("Escolha o modo de jogo (1 para dois jogadores, 2 para jogar contra a máquina): ")
        
        if modo_jogo == "1":
            jogar_dois_jogadores(tamanho_tabuleiro)
            break
        elif modo_jogo == "2":
            jogar_contra_maquina(tamanho_tabuleiro)
            break
        else:
            print("Escolha uma opção válida (1 ou 2).")
"""
    Imprime o tabuleiro atual.
"""
def imprimir_tabuleiro(tabuleiro):

    tamanho = len(tabuleiro)

    print("\nTabuleiro:")
    for linha in tabuleiro:
        print(" | ".join(["X" if posicao == 1 else "O" if posicao == 2 else " " for posicao in linha]))
        print("-" * (4 * tamanho - 1)) 
"""
    Permite que dois jogadores joguem um contra o outro.
"""
def jogar_dois_jogadores(tamanho_tabuleiro):

    tabuleiro = [[0] * tamanho_tabuleiro for _ in range(tamanho_tabuleiro)]
    jogadas = []
    jogador_atual = 1
    num_jogadas = 0

    while True:
        imprimir_tabuleiro(tabuleiro)
        if jogador_atual == 1:
            jogada = receber_jogada(jogador_atual, tamanho_tabuleiro)
        else:
            jogada = receber_jogada(jogador_atual, tamanho_tabuleiro)
        
        if not verificar_jogada_valida(jogada, tabuleiro):
            print("Jogada inválida. Tente novamente.")
            continue

        tabuleiro[jogada[0]][jogada[1]] = jogador_atual
        jogadas.append(jogada)

        if verificar_vencedor(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        if num_jogadas == tamanho_tabuleiro * tamanho_tabuleiro:
            imprimir_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            break

        jogador_atual = 2 if jogador_atual == 1 else 1
        num_jogadas += 1
"""
    Permite que um jogador jogue contra a máquina.
"""
def jogar_contra_maquina(tamanho_tabuleiro):

    tabuleiro = [[0] * tamanho_tabuleiro for _ in range(tamanho_tabuleiro)]
    jogadas = []
    jogador_atual = 1
    num_jogadas = 0

    while True:
        imprimir_tabuleiro(tabuleiro)

        if jogador_atual == 1:
            jogada = receber_jogada(jogador_atual, tamanho_tabuleiro)

            if not verificar_jogada_valida(jogada, tabuleiro):
                print("Jogada inválida. Tente novamente.")
                continue
        else:
            jogada = fazer_jogada_maquina(tabuleiro, tamanho_tabuleiro)
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

        if num_jogadas == tamanho_tabuleiro * tamanho_tabuleiro:
            imprimir_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            break

        jogador_atual = 2 if jogador_atual == 1 else 1
        num_jogadas += 1
"""
    Faz a jogada da máquina, escolhendo uma posição aleatória no tabuleiro vazio.
    Retorna as coordenadas da jogada como uma tupla (linha, coluna).
"""
def fazer_jogada_maquina(tabuleiro, tamanho_tabuleiro):

    while True:
        linha = random.randint(0, tamanho_tabuleiro - 1)
        coluna = random.randint(0, tamanho_tabuleiro - 1)
        if tabuleiro[linha][coluna] == 0:
            return linha, coluna
"""
    Recebe a jogada do jogador atual.
    Retorna as coordenadas da jogada como uma tupla (linha, coluna).
"""
def receber_jogada(jogador_atual, tamanho_tabuleiro):

    print(f"Jogador {jogador_atual}, é sua vez.")
    while True:
        """como se fosse um try-cath do js, mas em python"""
        try:
            linha = int(input(f"Digite a linha da sua jogada (0-{tamanho_tabuleiro - 1}): "))
            coluna = int(input(f"Digite a coluna da sua jogada (0-{tamanho_tabuleiro - 1}): "))
            if 0 <= linha < tamanho_tabuleiro and 0 <= coluna < tamanho_tabuleiro:
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
    tamanho_tabuleiro = len(tabuleiro)
    if 0 <= linha < tamanho_tabuleiro and 0 <= coluna < tamanho_tabuleiro:
        return tabuleiro[linha][coluna] == 0
    return False
"""
    Verifica se há um vencedor.
    Retorna True se há um vencedor, False caso contrário.
"""
def verificar_vencedor(tabuleiro):

    tamanho_tabuleiro = len(tabuleiro)

    """Verificação linhas e colunas"""
    for i in range(tamanho_tabuleiro):
        linha = tabuleiro[i]
        coluna = [tabuleiro[j][i] for j in range(tamanho_tabuleiro)]
        if all(x == linha[0] and x != 0 for x in linha) or all(x == coluna[0] and x != 0 for x in coluna):
            return True

    """Verificação diagonais"""
    diagonal_principal = [tabuleiro[i][i] for i in range(tamanho_tabuleiro)]
    diagonal_secundaria = [tabuleiro[i][tamanho_tabuleiro - i - 1] for i in range(tamanho_tabuleiro)]
    
    if all(x == diagonal_principal[0] and x != 0 for x in diagonal_principal) or all(x == diagonal_secundaria[0] and x != 0 for x in diagonal_secundaria):
        return True

    return False

"""chamada dafunção principal que chama as outras funções para o perfeito funcionamento da main """
jogo_da_velha()
