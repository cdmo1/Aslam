import random
import colorama  # Importar a biblioteca para estilização de cores
from colorama import Fore

colorama.init(autoreset=True)  # Inicializar a biblioteca de estilização de cores

""" 
    Carregar lista de palavras de um arquivo de texto de maneira formatada
"""
def carregar_palavras():
    with open('lista_palavras.txt', 'r', encoding='utf-8') as arquivo:
        palavras = arquivo.read().splitlines()
    return palavras


""" aqui escolhemos uma palavra aleatória da lista de palavras"""
def selecionar_palavra(palavras):
    return random.choice(palavras)

""" encapsulamento de função necessária para a inicialização do game"""
def inicializar_jogo():
    palavras = carregar_palavras()
    palavra_secreta = selecionar_palavra(palavras)
    letras_adivinhadas = []
    letras_erradas = []
    tentativas = 6
    return palavra_secreta, letras_adivinhadas, letras_erradas, tentativas

""" exibição de estado atual do jogo assim como no game para o usuário """
def exibir_jogo(palavra, letras_adivinhadas, letras_erradas, tentativas):
    palavra_oculta = ''.join([letra if letra in letras_adivinhadas else '_' for letra in palavra])
    
    print(f"Palavra: {palavra_oculta}")
    print(f"Tentativas restantes: {tentativas}")
    letras_erradas_estilizadas = ', '.join([Fore.RED + letra + Fore.RESET for letra in letras_erradas])
    print(f"Letras erradas: {letras_erradas_estilizadas}")

    # Estilização das letras erradas em vermelho
    letras_erradas_estilizadas = ', '.join([Fore.RED + letra + Fore.RESET for letra in letras_erradas])
    print(f"Letras erradas: {letras_erradas_estilizadas}")

"""exibição do terclado solicitado no exercício proposto pelo professor na última segunda-feira 04/09/2023"""
def exibir_teclado(letras_adivinhadas, letras_erradas):
    letras_disponiveis = [chr(ord('a') + i) for i in range(26)]
    
    teclado = ""
    for letra in letras_disponiveis:
        if letra in letras_adivinhadas:
            teclado += f"{Fore.GREEN}{letra}{Fore.RESET} "
        elif letra in letras_erradas:
            teclado += f"{Fore.RED}{letra}{Fore.RESET} "
        else:
            teclado += f"{letra} "
    
    print("\nTeclado:")
    print(teclado)

""" a função principal do game, chamada de funções necessárias """
def jogo_da_forca():
    print("Bem-vindo ao Jogo da Forca!")
    aux = True
    while aux:
        palavra, letras_adivinhadas, letras_erradas, tentativas = inicializar_jogo()
        
        while tentativas > 0:
            exibir_jogo(palavra, letras_adivinhadas, letras_erradas, tentativas)
            exibir_teclado(letras_adivinhadas, letras_erradas)
            letra = input("Escolha uma letra: ").lower()
            
            if letra in letras_adivinhadas or letra in letras_erradas:
                print("Você já tentou essa letra. Tente outra.")
                continue
            
            if letra in palavra:
                letras_adivinhadas.append(letra)
                if set(letras_adivinhadas) == set(palavra):
                    exibir_jogo(palavra, letras_adivinhadas, letras_erradas, tentativas)
                    print("Parabéns! Você venceu!")
                    break
            else:
                letras_erradas.append(letra)
                tentativas -= 1
        
        if tentativas == 0:
            exibir_jogo(palavra, letras_adivinhadas, letras_erradas, tentativas)
            print(f"Você perdeu! A palavra era '{palavra}'.")
        
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            break

if __name__ == "__main__":
    jogo_da_forca()
