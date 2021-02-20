# Python3 Implementación de un árbol binario para ordenar números
# La numeración va de 0 a 3
arbol = [None] * 15

print(arbol)

def raiz(entrada):
	if arbol[0] != None:
		print("El árbol ya tiene raiz")
	else:
		arbol[0] = entrada


def hijo_izq(entrada, padre):
	if arbol[padre] == None:
		print("No se puede asignar hijo en", (padre * 2) + 1, ", no hay padre")
	else:
		arbol[(padre * 2) + 1] = entrada


def hijo_der(entrada, padre):
	if arbol[padre] == None:
		print("No se puede asignar hijo en", (padre * 2) + 2, ", no hay padre")
	else:
		arbol[(padre * 2) + 2] = entrada


def arbol():
	for i in range(15):
		if arbol[i] != None:
			print(arbol[i], end="")
		else:
			print("-", end="")
	print()


lista_entrada = []

for i in range(4):
	lista_entrada.append(input("Digite un número de 1 a 4"))

raiz(lista_entrada[0])

