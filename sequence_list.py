pontos = (3,5)
p1 = (3,5)
p2 = (4,6)
p3 = (5,7)
line = [p1,p2,p3]
print(line)

p1 = ("Nicodemos", 34,32)
p2 = ("Jesus",33)
instrutores = [p1,p2]



print(instrutores[0][1])
print("********************")

print("Tuple")
#utilizando o tuple para guardar as palavras
palavras = []
palavras.append("banana")
palavras.append("abacaxi")
nova = tuple(palavras)
print(nova)

print("Transforma tuple em list")
#sequencia que recebe o tuple/ transforma tuple em uma lista
outra = list(nova)
print(outra)