def jogar_adivinhacao():
    import random

    print("Bem vindo ao jogo de adivinhação!")
    pontos = 1000;
    print("Qual nível de dificuldade?")
    print("(1) Fácil\n(2) Médio\n(3) Dificil")
    nivel = int(input("Defina o nivel: "))
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    elif (nivel == 3):
        total_tentativas = 5
    num_secreto = random.randrange(1, 101)

    for rodada in range(1, total_tentativas + 1):
        print("\nTentativa", rodada, " de ", total_tentativas)
        chute = int(input("Digite o seu numero entre 0 e 100: "))
        if (chute < 1 or chute > 100):
            print("Você digitou um valor invalido.")
            continue
        print("Você digitou ", chute)

        if (num_secreto == chute):
            print("Você acertou! E fez ", pontos, " pontos!")
            break
        else:
            pontos = pontos - abs(chute - num_secreto)  # ABS numero absoluto
            if (chute > num_secreto):
                print("Você errou! O chute foi maior.")
            elif (chute < num_secreto):
                print("Você errou! O chute foi menor.")
    print("Fim de jogo! O numero era ", num_secreto)

if (__name__ == "__main__"):
    jogar_adivinhacao()
