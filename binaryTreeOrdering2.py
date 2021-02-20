arbol = [None] * 31

print(arbol)

raiz = int(input("Escriba un número de 1 a 4: "))

arbol[0] = raiz

print(arbol)

def ubicar(padre, entrada):
    if entrada < arbol[padre]:
        if arbol[2*padre + 1] == None:
            arbol[2*padre + 1] = entrada
            
        else:
            ubicar(2*padre +1, entrada)
    else:
        if arbol[2*padre + 2] == None:
            arbol[2*padre + 2] = entrada
        else:
            ubicar(2*padre +2, entrada)

for i in range(3):
    entrada = int(input("Escriba un número de 1 a 4: "))
    ubicar(0, entrada)
    print(arbol)

def en_orden(padre, arbol):
    if arbol[2*padre + 1] != None:
        en_orden(2*padre + 1, arbol)

    print(arbol[padre])

    if arbol[2*padre + 2] != None:
        en_orden(2*padre + 2, arbol)
        
en_orden(0, arbol)    
