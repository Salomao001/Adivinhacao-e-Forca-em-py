import adivinhacao
import Forca


def escolhe_jogo():
    print("********************************")
    print("*******Escolha o seu jogo*******")
    print("********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o jogo: "))

    if jogo == 1:
        Forca.jogar_foca()
    elif jogo == 2:
        adivinhacao.jogar_adivinhacao()


if __name__ == "__main__":
    escolhe_jogo()