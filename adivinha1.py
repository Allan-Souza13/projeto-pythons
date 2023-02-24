# Jogo de Adivinhação
print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
chute_str  = input("Digite o seu numero: ")

print("Voce digitou ", chute_str)

chute = int(chute_str)#chute_str se transformou em int
acertou= chute == numero_secreto
maior =  chute > numero_secreto
menor =  chute < numero_secreto

if (acertou):
    print("Você acertou!")
else:
    if(maior):
        print("Você errou! O seu chute foi maior do que o que o número secreto. ")
    elif(menor):
        print("Você errou! O seu chute foi menor do que o que o número secreto. ")

print("Fim do Jogo!")