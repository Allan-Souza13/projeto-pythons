import forca
import adivinha1
def escolhe_jogo():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    print("(1) Adivinha (2) Forca")

    jogo = int(input("Qual Jogo?"))
    if(jogo == 1):
        print("Jogar Adivinha")
        adivinha1.jogar()#chamando a função
    elif(jogo == 2):
        print("Jogar Forca")
        forca.jogar()


if(__name__=="__main__"):#Garante a execução como um programa principal
    escolhe_jogo()
