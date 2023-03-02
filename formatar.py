#-----------------Float------------------------#
print("R$ {:f}".format(1.59))  # {:f} tipo float

print("R$ {:.2f}".format(1.59)) #ira imprimir 1.59

print("R$ {:7.2f}".format(1.59)) #deixara um espaço pois esta sendo informado 7 de float

print("R$ {:07.2f}".format(1.59)) #ira imprimir "0" no espaço antes do valor "1.59"

print("R$ {:7.2f}".format(11.6))

print("Meu nome é{1}{0}".format("Souza", "Allan"))#puxará o Allan primeiro

idade = 14

nome = "Allan Souza"
mes = 12
dia = 4
ano = 1998

print("Me chamo {}, a data do meu nacimento é: {}/{}/{}".format(nome,dia,mes,ano))

#-----------------Inteiro------------------------#

print("Data {:02d}/{:02d}".format(9,4))#irá imprimir o inteiro de data, usa-se "d" de digito


#Digamos que ele queira exibir a seguinte mensagem: "Ola Sr. Leonardo Cordeiro", como ele pode formatar a string para obter o resultado desejado?

print("Olá Sr.{1} {0}".format("Cordeiro", "Leandro")) #A posição de Leandro é 1 e a de Cordeiro é 0.

