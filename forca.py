import random




def jogar(): #def é a definição de uma função

    iniciar()
    palavra_secreta = carrega_palavra_secreta()



    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    #-----------------------------------------------------------------#
    print(letras_acertadas)
    enforcou = False #variavel caso o jogador erre a letra
    acertou = False #variavel caso o jogador acerte a letra
    erros = 0 #varialvel erros




    while(not enforcou and not acertou): #enquanto não enforcou e não acertou

        chute =  pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute,letras_acertadas,palavra_secreta)

        else:
            erros = erros + 1
            desenha_forca(erros)

        enforcou = erros == 6 #se a pessoa errar 6 vezes ela perde
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()




    if(__name__=="__main__"):
        jogar()


#-------------------Funções definidas-------------------#


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
                print("Parabéns, você ganhou!")
                print("       ___________      ")
                print("      '._==_==_=_.'     ")
                print("      .-\\:      /-.    ")
                print("     | (|:.     |) |    ")
                print("      '-|:.     |-'     ")
                print("        \\::.    /      ")
                print("         '::. .'        ")
                print("           ) (          ")
                print("         _.' '._        ")
                print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")


def marca_chute_correto(chute,letras_acertadas,palavra_secreta):
    index = 0  # seria a posição da letra
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):  # caso chute com a letra maiuscula ele entende
            letras_acertadas[index] = letra  # ira guardar a letra na posição certa
        index = index + 1  # incrementa a letra

def pede_chute():
    chute =  input("Qual a letra? ")
    chute = chute.strip().upper()  # O strip serve para caso exista um espaço em branco ele remove da esquerda e da direita.
    return chute

def inicializa_letras_acertadas(palavra):
    return["_" for letra in palavra]  # usa o caracter "_"  para cada letra dentro da palavra/ list Comprehensions

def iniciar():
    print("*********************************")
    print("Bem vindo ao jogo da forca!")
    print("*********************************")


def carrega_palavra_secreta():
    # Escolhendo a palavra
    arquivo = open("palavras.txt", "r")  # r seria read
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta #como esta fora da função ela puxa a palavra secreta
