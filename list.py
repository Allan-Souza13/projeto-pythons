#Mariana montou o seguinte código Python para controlar se a sua barraca de frutas possui determinadas frutas solicitadas pelos seus clientes:

frutas = ['Banana', 'Maçã', 'Pera', 'Uva', 'Melancia', 'Jamelão']

fruta_pedida = input("Qual é a fruta que deseja consultar?")


if(fruta_pedida in frutas): #se fruta perdida tem em frutas
    print("Sim, temos a frutas.")
else:
    print("Não temos essa fruta.")

print("****************************")
print("--Descobrir o valor minimo--")
print("****************************")

precos = [1525,1120,1464,1200,1330,1356,1312,1531,1232,
          1234,1250,1114,1553,1147,1303,1296,1309,1404,1479,
          1376,1152,1440,1038,1018,1291,1388,1577,1115,1488,
          1494,1254,1230,1122,1396,1208,1356,1549,1116,1443,1075,
          1536,1542,1036,1015,1020,1217,1484,1032,1390,1026 ]
print(min(precos))#Desscobre o valor minimo


print("****************************")
print("--Descobrir a quantidade de funcionarios--")
print("****************************")


funcionarios = ['Astrid','Flavia','Talia',  'Allan' ,'Mauricio', 'Waldemar', 'Marina']
print(len(funcionarios))#verifica a quantidade de funcionarios


print("*****************")
print("--contando os 0--")
print("*****************")

valores = [ 0, 0, 0, 1, 2, 3, 4]
print(valores.count(0))#conta os 0


print("*****************")
print("--Quantas letras faltam preencher--")
print("*****************")

letras_acertadas = ["_","_","_","_","_","_"]
letras_faltando = str(letras_acertadas.count("_"))
print("Ainda faltam acertar {} letras".format(letras_faltando))


print("*****************")
print("--função index retorna o primeiro elemento--")
print("*****************")

frutas = ["Banana", "Morango", "UVA", "MAÇÃ"]
print(frutas.index("UVA"))#POSIÇÃO DA UVA FICA EM 2 NA LISTA


print("*****************")
print("--Caso a fruta não esteja na lista--")
print("*****************")

frutas = ["Banana","Maçã","Uva","Melão","Amora"]

fruta_buscada= "Melancia"
if fruta_buscada in frutas:#se fruta buscada esta em frutas
    print(frutas.index(fruta_buscada))
else:
    print("Desculpe, a {} não está na lista frutas".format(fruta_buscada))
