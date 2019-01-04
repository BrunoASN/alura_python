def jogar_forca():
    print("Bem vindo ao jogo de forca!")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input("Qual letra? ")
        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1


if (__name__ == "__main__"):
    jogar_forca()
