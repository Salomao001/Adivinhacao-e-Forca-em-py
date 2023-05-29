from random import randint


def jogar_adivinhacao():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = randint(1, 100)
    total_de_tentativas = 3
    rodada = 1
    pontos = 1000

    print('Qual nivel de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')
    while True:
        nivel = int(input('Defina o nível: '))
        if nivel < 1 or nivel > 3:
            print("Opção invalida!")
        else:
            break

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5

    for rodada in range(rodada, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou {}".format(chute))

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você Acertou e fez {} pontos!!!".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior que o numero secreto.")
            elif menor:
                print("Você errou! O seu chute foi menor que o numero secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim do jogo")


if __name__ == "__main__":
    jogar_adivinhacao()