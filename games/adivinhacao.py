print("Bem vindo ao jogo de adivinhação!")

num_secreto=42

chute = int(input("Digite o seu numero: "))

print("Você digitou ", chute)

if (num_secreto==chute):
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim de jogo!")