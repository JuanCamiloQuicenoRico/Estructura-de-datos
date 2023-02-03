"""
Nombre: Juan Camilo Quiceno
Código: 1029292
"""

#1er punto
#se ingresa la matriz
mat = [[11, 23, 76, 34, 11],
[14, 30, 92, 30, 101],
[12, 45, 58, 92, 22],
[74, 56, 49, 56, 100],
[99, 5, 28, 47, 99]]

def verificarDiagonales(mat):
    #se ingresa el bool que nos dirá si los elementos de las diagonales 
    # coinciden 
    x = True
    y = -1  
    #iniciamos ciclo para que recorra la diagonal
    for i in range (len (mat)):
        if mat [i] [i] != mat [i] [y]:
            x = False 
        y -=1 

    return x
print(verificarDiagonales(mat))   

#2do punto
#
def esCapicua (listaNumeros):
    #damos una lista vacia llamada recorridoizqAder
    recorridoizqAder = "" 
    #iniciamos un ciclo para que haga el recorrido de izquierda a derecha 
    for i in range (0, len(listaNumeros), 1):
        recorridoizqAder = recorridoizqAder + str(listaNumeros[i]) 
    #imprimimos el recorrido
    print(recorridoizqAder)
    #iniciamos el recorrido de derecha a izquierda
    recorridoderAizq = "" 
    #hacemos siclo para que haga el recorrido de la lista de derecha a izquierda
    for i in range (len(listaNumeros) - 1, -1, -1):
        recorridoderAizq = recorridoderAizq + str(listaNumeros[i]) 
    #imrimimos el recorrido de derecha a izquierda 
    print(recorridoderAizq)
    #comparamos las 2 listas y retornamos 
    return recorridoderAizq == recorridoizqAder
#imprimimos la lista 
print(esCapicua([1,2,1]))
# 3er punto 
#a)
def diferenciaListas(listaA,listaB):
    #se pone lista vacia para añadir los resultados
    resultado = []
    #rango para que recorra la lista A
    for i in range (len(listaA)):
        loEncontre = False
        #rango para que recorra la lista B
        for j in range (len(listaB)): 
            #compara si algún caracter de la lista A esta en la lista B        
            if listaB[j] == listaA[i]:
                listaB.pop(j)
                loEncontre = True
                #rompe el ciclo
                break
        #si lo encontre sigue siendo falso lo que hara es añadir el resultao
        #a la lista A
    
        if loEncontre == False:
            resultado.append(listaA[i])
            #retornamos el resultado luego de haberlo añadido
    return resultado
listaA = [40, 10, 22, 12, 33, 33, 33]
listaB = [41, 22, 31, 15, 13, 12, 33, 19]
#imprimimos las listas   
print(diferenciaListas(listaA,listaB))
   

#b)
def diferenciaListasConInput():
    #asignamos  en "n" el imput
    n = int(input())
    #dejamos lista vacia para almacenar los datos de los resultados
    resultado = []
    #iniciamos ciclo en el cual separe caracteres con .split
    for x in range (n):
        cadenaA = input(8, 41 ,22 ,31 ,15, 13 ,12, 33 ,19)
        listaA = cadenaA.split()
        cadenaB = input(7, 40, 10, 22, 12, 33, 33,33)
        listaB = cadenaB.split()

      
        resultado.append(diferenciaListas(listaA[1:len(listaA)],listaB[1:len(listaB)]))
        # listaA.pop(0)
        # listaB.pop(0)
        # resultado.append(diferenciaListas(listaA,listaB))

    for i in resultado:
        print(*i)
        #imprimimos la diferencia de las listas
    print(diferenciaListasConInput()) 



#4) punto
def decirSiEsPrimo(n):
    #comparamos n con uno
    if n == 1:
        #si n es igual a uno restornamos false
        return False
    #si n no es uno retorna True
    esPrimo = True
    #iniciamos ciclos para definir si es primo o no
    for i in range (1,n):
        if n%i == 0 and i < n and i != 1:
            esPrimo = False

    return esPrimo

def decirSiSumListaEsPrimo(n):
    
    lista = [int(a) for a in str(n)]
    sum = 0
    # iniciamos un ciclo donde la ubicación en lista le sume 1
    for i in lista:
        sum += i

    sumListaEsPrimo = decirSiEsPrimo(sum)
    #retornamos si la lista es primo
    return sumListaEsPrimo
    

def mostrarPrimos(n):
    #creamos lista  vacia donde swe guarden los resultados
    resultado = []
    resultadoSuma = []
    # iniciamos ciclo para que si es primo lo adjunte a resultado
    for i in range (1,n):
        if decirSiEsPrimo(i):
            resultado.append(i)
    #creamos ciclos para que el resultado de la suma lo adjunte a i
    for i in resultado:
        if decirSiSumListaEsPrimo(i):
            resultadoSuma.append(i)
    print("Números primos entre 1 y ", n, ":")
    for i in resultado: 
        #ponemos el str para qu los numero primos salgan con base a la fecla y las comas en manera de lista    
        print("-->", i,"," )
    print("Números entre 1 y", n, "con súma de dígitos con valor primo",  ":\n", resultadoSuma) 



#5) punto
def sumarValoresMatriz(disp, coords):
    #iniciamos con un contador en 0
    sum = 0
    #iniciamos ciclo para ubicar coordenadas en la matriz dispersa
    for coordenada in coords:
        #iniciamos condicional donde coordenqada es 0 en la matriz dispersa
        if coordenada[0] in disp:
            #ubicamos la fila en la posición 0
            fila = disp[coordenada[0]]
            #para tupla en la fila si es 0 compra la coordenada
            for tupla in fila:
                if tupla[0] == coordenada[1]:
                    #suma añade uno a tupla
                    sum += tupla[1]
    print(sum)
    disp = {0 : [(0, 1), (5, 4), (7, 5)],
1 : [(6, 4), (7, 7)],
2 : [(0, 2), (1, 2), (4, 9), (6, 1)],
4 : [(2, 8), (3, 1), (5, 7)],
6 : [(0, 3), (5, 6), (7, 2)],
7 : [(0, 4), (1, 4), (2, 7)],
8 : [(1, 9), (3, 8), (5, 7), (7, 6)]}
#llamamos a la varaible
    sumarValoresMatriz(disp, [(0, 0), (8, 3), (3, 5), (7, 2), (4, 3), (4,6)])

"""
 [[1, 0, 0, 0, 0, 4, 0, 5],
[0, 0, 0, 0, 0, 0, 4, 7],
[2, 2, 0, 0, 9, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 8, 1, 0, 7, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[3, 0, 0, 0, 0, 6, 0, 2],
[4, 4, 7, 0, 0, 0, 0, 0],
[0, 9, 0, 8, 0, 7, 0, 6]]

"""



