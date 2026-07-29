#Este código corresponde a los ejercicios 17 y 18 de la tarea 1 del propedéutico de Siafi.    ^u^
#Ejercicio 17 (Polinomio):
from funciones_polinomios import *
def ejercicio17():
    n = None
    while True:
        try:
            n = (int(input("Ingrese el número de puntos en el polinomio interpolante del Don Ramón (Mínimo: 1, Máximo: 5): ")))
            if n < 1 or n > 5:
                print("Número de puntos no válido, lee las instrucciones caray... Por favor, ingresa un número entre 1 y 5.")
                continue
            break
        except ValueError:
            print("Eso ni es número entero, no inventes compadre. Pareces del TEC. >:c\nPor favor, ingresa un número entre 1 y 5.")
            continue

    puntitos = [[None for j in range(2)] for i in range(n)]
    
    # for p in puntitos:
    #     print(p)
    
    x_lista = [None] * n
    y_lista = [None] * n  
    print("\n***************************************************************************************************************************")
    print("Vamos a ingresar los valores de x y y de los puntos. El valor de x no puede repetirse, así que ten cuidado con eso. >:c\n")
    for i in range(n):
        while True:
            try:
                print("Punto {}:".format(i+1))
                x_lista [i] =   (int(input("Ingrese el valor de x para el punto {}: ".format(i+1))))
                if x_lista[i] in x_lista[:i]:
                    print("\nTE DIJE QUE NO LOS REPITIERAS!!!!. >:c\nPor favor, ingresa un número entre 1 y 5. :3")
                    continue
                y_lista [i] =   (int(input("Ingrese el valor de y para el punto {}: ".format(i+1))))
                break
            except ValueError:
                print("Eso ni es número entero, no inventes compadre. Pareces del TEC. >:c\nPor favor, ingresa un número entre 1 y 5.\n")
                continue
    
    for i in range(n):
        puntitos[i][0] = x_lista[i]
        puntitos[i][1] = y_lista[i]
    
    for p in puntitos:
        print(p)

    t = int(input("Ahora pon el valor donde quieres evaluar el polinomio:"))
    tablita_Pij = [[None for j in range(n)] for i in range(n)]
    for i in range(n):
        tablita_Pij[i][i] = y_lista[i]
    for tablita in tablita_Pij:
        print(tablita)

    #Formulita del pdf de Ramón: p_i,j(t) = [(t-x_j)p_i,j-1(t) - (t-x_i)p_i+1,j(t)] / (x_i-x_j)
    for distancia in range(1, n):
        for i in range(n - distancia):
            j = i + distancia
            tablita_Pij[i][j] = ((t - x_lista[j]) * tablita_Pij[i][j-1] - (t - x_lista[i]) * tablita_Pij[i+1][j]) / (x_lista[i] - x_lista[j])

    print("\n*** SIAFI *** SIAFI *** SIAFI *** SIAFI *** SIAFI *** SIAFI *** SIAFI *** SIAFI *** \n\nTabla p_ij:")
    for tablita in tablita_Pij:
        print(tablita)
    print("El resultado es: ", tablita_Pij[0][n-1])
    
    ########SIAFI####### Aquí ya es ejercicio 18: Generar el polinomio que describe a la función. #######SIAFI########
    tablita_polinomitos = [[None for j in range(n)] for i in range(n)]
    for i in range(n):
        tablita_polinomitos[i][i] = [y_lista[i]]
    
    #Formulita del pdf de Ramón: p_i,j(x) = [(x-x_j)p_i,j-1(x) - (x-x_i)p_i+1,j(x)] / (x_i-x_j)
    for distancia_polis in range(1, n):
        for i in range(n - distancia_polis):
            j = i + distancia_polis

            parte1 = multiplicar_xMenos_valor(tablita_polinomitos[i][j - 1], x_lista[j])
            parte2 = multiplicar_xMenos_valor(tablita_polinomitos[i + 1][j], x_lista[i])

            numerador = restaPolinomios(parte1, parte2)
            denominador = x_lista[i] - x_lista[j]

            tablita_polinomitos[i][j] = multiplicacionConst(numerador, 1 / denominador)
    
    print("\n*** SIAFI *** SIAFI *** SIAFI *** SIAFI *** SIAFI *** SIAFI *** SIAFI *** SIAFI *** \n\nTabla de polinomios:")
    for tablita_poli in tablita_polinomitos:
        print(tablita_poli)
    print("El resultado es: ", imprimirPolinomio(tablita_polinomitos[0][n-1]))

ejercicio17()
