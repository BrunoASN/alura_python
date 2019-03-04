def jogar_forca():
    print("Bem vindo ao jogo de forca!")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual letra? ")  # Retira os espaços
        chute = chute.strip().upper() # unper retorna sempre em maisculas, para minusculas utilizar o lower

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6  # limita o numero de tentativas em 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        print("Parabéns você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim de jogo")


if (__name__ == "__main__"):
    jogar_forca()
