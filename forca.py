def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    palavra_secreta = "banana" #declrando a palavra secreta

    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False #variavel caso o jogador erre a letra
    acertou = False #variavel caso o jogador acerte a letra

    print(letras_acertadas)

    while(not enforcou and not acertou): #enquanto não enforcou e não acertou
        chute = input("Qual a letra? ")
        chute = chute.strip() #O strip serve para caso exista um espaço em branco ele remove da esquerda e da direita.

        index = 0 #seria a posição da letra
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()): #caso chute com a letra maiuscula ele entende
                letras_acertadas[index] = letra #ira guardar a letra na posição certa
            index = index + 1 #incrementa a letra

        print(letras_acertadas)



    print("Fim do Jogo!")
    if(__name__=="__main__"):
        jogar()
