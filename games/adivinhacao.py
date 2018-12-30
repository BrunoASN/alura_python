print("Bem vindo ao jogo de adivinhação!")

num_secreto = 42
total_tentativas = 3

for rodada in range(1, total_tentativas + 1):
    print("\nTentativa", rodada, " de 3")
    chute = int(input("Digite o seu numero entre 0 e 100: "))
    if (chute < 1 or chute > 100):
        print("Você digitou um valor invalido.")
        continue
    print("Você digitou ", chute)

    if (num_secreto == chute):
        print("Você acertou!")
        break
    else:
        if (chute > num_secreto):
            print("Você errou! O chute foi maior.")
        elif (chute < num_secreto):
            print("Você errou! O chute foi menor.")
print("Fim de jogo!")
