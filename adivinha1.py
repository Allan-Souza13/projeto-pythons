# Jogo de Adivinhação
print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
#rodada = 0  define no while

#------- Laço de repetição em while --------#
#enquanto ainda há tentativas:
#while (rodada < total_de_tentativas ):#laço de repetição com while
 #   print("Tentativas {} de {}".format( rodada, total_de_tentativas))#.format Strin Interpulation, substitui o {} de {}
  #  chute_str  = input("Digite o seu numero: ")
   # print("Voce digitou ", chute_str)
    #chute = int(chute_str)#chute_str se transformou em int


#------- Laço de repetição em for --------#
for rodada in range(1, total_de_tentativas + 1 ):
    print("tentativas {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o numero entre 1 e 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if(chute < 1 | chute > 100): #utilizei o ou para saber se o usuario digitou menor que 1 ou maior que 100'
        print("Você deve digitar um numero entre 1 e 100!")
        continue#continua a rodada



    acertou= chute == numero_secreto
    maior =  chute > numero_secreto
    menor =  chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break #finaliza o laço da rodada quando acerta o numero.
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o que o número secreto. ")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o que o número secreto. ")

    #rodada = rodada +1  encrenta no while

print("Fim do Jogo!")