# Pede ao usuario que digite o primeiro numero

num1 = float(input("Digite o primeiro numero: "))


#Pede pára o usuario digitar o segundo numero

num2 = float(input("Digite o segundo numero: "))

#pede para o usuario digite a operação desejada

operacao = input("Digite a operação desejada (+, -, * ,/): ")


#verifica qual operação foi escolhida e realizada a operação correspondente

if operacao =='+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2
else:
    print("Essa operação é invalida")


#imprime o resultado
print("O resultado é: ", resultado)
