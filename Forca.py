from random import randrange


def jogar_foca():

    imprimir_mensagem_abertura()

    palavra_secreta = carrega_palavrasecreta()

    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print("  _______     ")
    print(" |/      |    ")
    print(" |            ")
    print("_|___         ")
    print(letras_acertadas)
    while not enforcou and not acertou:

        chute = pergunta_chute()

        if chute in palavra_secreta:
            verifica_acertou_chute(chute, palavra_secreta, letras_acertadas)
            desenha_forca(erros)
        else:
            erros += 1
            desenha_forca(erros)
            enforcou = verfica_enforcou(erros)

        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")


def imprimir_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")


def carrega_palavrasecreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    palavras = palavras[randrange(0, len(palavras))]

    palavra_secreta = palavras.upper()
    return palavra_secreta


def pergunta_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def verifica_acertou_chute(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def verfica_enforcou(erros):
    enforcou = erros == 7
    return enforcou


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")


if __name__ == "__main__":
    jogar_foca()