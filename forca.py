import random
def jogar(): #def é a definição de uma função
    print("*********************************")
    print("Bem vindo ao jogo da forca!")
    print("*********************************")

    #Escolhendo a palavra
    arquivo = open("palavras.txt", "r")#r seria read
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]#usa o caracter "_"  para cada letra dentro da palavra/ list Comprehensions
    #-----------------------------------------------------------------#

    enforcou = False #variavel caso o jogador erre a letra
    acertou = False #variavel caso o jogador acerte a letra
    erros = 0 #varialvel erros


    print(letras_acertadas)

    while(not enforcou and not acertou): #enquanto não enforcou e não acertou
        chute = input("Qual a letra? ")
        chute = chute.strip().upper() #O strip serve para caso exista um espaço em branco ele remove da esquerda e da direita.

        if(chute in palavra_secreta):

            index = 0 #seria a posição da letra
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()): #caso chute com a letra maiuscula ele entende
                    letras_acertadas[index] = letra #ira guardar a letra na posição certa
                index = index + 1 #incrementa a letra
        else:
            erros = erros + 1

        enforcou = erros == 6 #se a pessoa errar 6 vezes ela perde
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")



    print("Fim do Jogo!")
    if(__name__=="__main__"):
        jogar()
