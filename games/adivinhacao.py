print("Bem vindo ao jogo de adivinhação!")

num_secreto = 42
total_tentativas = 1

while (total_tentativas <= 3):
    print("\nTentativa",total_tentativas," de 3")
    chute = int(input("Digite o seu numero: "))
    print("Você digitou ", chute)

    if (num_secreto == chute):
        print("Você acertou!")
    else:
        if (chute > num_secreto):
            print("Você errou! O chute foi maior.")
        elif (chute < num_secreto):
            print("Você errou! O chute foi menor.")
    total_tentativas = total_tentativas + 1
print("Fim de jogo!")
