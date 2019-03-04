def jogar_forca():
    print("Bem vindo ao jogo de forca!")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual letra? ")  # Retira os espaços
        chute = chute.strip()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (
                        chute.upper() == letra.upper()):  # unper retorna sempre em maisculas, para minusculas utilizar o lower
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6  # limita o numero de tentativas em 6
        print(letras_acertadas)

    print("Fim de jogo")


if (__name__ == "__main__"):
    jogar_forca()
