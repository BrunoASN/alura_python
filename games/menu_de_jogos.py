import forca
import adivinhacao

print("Bem vindo, escolha seu jogo!")
print("(1) Forca\n(2) Adivinhação")
jogo=int(input("Escolha seu jogo: "))

if(jogo==1):
    print("Jogando forca!")
    forca.jogar_forca()
elif (jogo == 2):
    print("Jogando adivinhação!")
    adivinhacao.jogar_adivinhacao()