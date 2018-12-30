print("Bem vindo ao jogo de adivinhação!")

num_secreto=42

chute = int(input("Digite o seu numero: "))

print("Você digitou ", chute)

if (num_secreto==chute):
    print("Você acertou!")
else:
    if(chute>num_secreto):
        print("Você errou! O chute foi maior.")
    elif (chute < num_secreto):
        print("Você errou! O chute foi menor.")

print("Fim de jogo!")