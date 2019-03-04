import random

def jogar_forca():
    print("Bem vindo ao jogo de forca!")

    palavra_secreta = carrega_palavra()

    letras_acertadas = ininializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual letra? ")  # Retira os espaços
        chute = chute.strip().upper()  # unper retorna sempre em maisculas, para minusculas utilizar o lower

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
    if (acertou):
        print("Parabéns você ganhou!")
    else:
        print("Você perdeu, a palavra secreta era",format(palavra_secreta))
    print("Fim de jogo")

def carrega_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def ininializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


if (__name__ == "__main__"):
    jogar_forca()
