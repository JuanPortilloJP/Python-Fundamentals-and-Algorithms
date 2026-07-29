#Código realizado por: Juan Manuel Portillo López
from ast import While
#Ejercicio 4:
def ejercicio4():
    resultado_potencia = 2 ** 3
    resultado_modulo = 10 % 3
    print("El resultado de 2 elevado a la potencia de 3 es:", resultado_potencia)
    print("El resultado del módulo de 10 entre 3 es:", resultado_modulo)

#Ejercicio 5:
def ejercicio5():
    nombre = "Juan" 
    apellido = "Pérez"
    nombre_completo = nombre + " " + apellido
    print(nombre_completo)

#Ejercicio 6:
def ejercicio6():
    frutas = ["manzana", "banana", "cereza", "dátil"]
    return frutas

#Ejercicio 7:
def ejercicio7(): 
    frutas = ["manzana", "banana", "cereza"]
    frutas.append("kiwi")
    frutas[1] = "arándano"

    print(frutas)

#Ejercicio 8:
def ejercicio8():
    calificacion = 75
    if calificacion >= 90:
        print("Tienes una A.")
    elif calificacion >= 80:
        print("Tienes una B.")
    elif calificacion >= 70:
        print("Tienes una C.")
    else:
        print("Tienes una D o F.")    

#Ejercicio 10:
def ejercicio10():
    for i in range(5):
        print(i)

#Ejercicio 11:
def ejercicio11():
    frutas = ["manzana", "banana", "cereza"]
    for fruta in frutas:
        print(fruta)

#Ejercicio 12 (Bucle while):
def ejercicio12():
    contador = 0
    while contador < 3:
        print("El contador es:",contador)
        contador += 1

#Ejercicio 13 (Funciones:Definición y llamada):
def ejercicio13():
    def saludar(nombre):
        print("Hola, " + nombre + "!")
    saludar("Carlos")

#Ejercicio 14 (Funciones con retorno):
def ejercicio14():
    def sumar(a, b):
        return a * b
    resultado = sumar(10, 7)
    return resultado

#Ejercicio 15 (Números primos):
def ejercicio15():
 
    # Funciones para verificar si un número es primo
    def es_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def listar_primos(N):
        primos = []
        if N >= 2:
            for num in range(2, N + 1):
                if es_primo(num):
                    primos.append(num)
        return primos
    
    # Solicitar al usuario un número N
    while True:
        N = input("Ingrese un número entre 0 y 50: ")

        # Validación de entrada N
        try:
            N = int(N)
            if N < 0 or N > 50:
                print("Ese no es un número válido. >:c\nPor favor, ingresa uno entre 0 y 50.")
                continue
            break
    
        except ValueError:
            print("Eso ni es número entero, no inventes compadre. >:c\nPor favor, ingresa un número entre 0 y 50.")
            continue
    
    # Obtener y mostrar la lista de números primos
    listaPrimos = listar_primos(N)
    if len(listaPrimos) == 0:
        print("No hay números primos en ese rango. buuuuuu :(")
        return
    else:
        print("Los números primos entre 0 y", N, "son:", listaPrimos)

#Ejercicio 16 (Ordenamiento de una cola):
def ejercicio16():
    #
    class Cola:
        def __init__(self):
            self.elementos = []

        def push(self, posi_actual):
            self.elementos.append(posi_actual)

        def pop(self):
            if not self.empty():
                return self.elementos.pop(0)

        def front(self):
            if not self.empty():
                return self.elementos[0]

        def empty(self):
            return len(self.elementos) == 0

        def mostrar(self):
            lista = []

            for elemento in self.elementos:
                lista.append(elemento)

            print(lista, "Achis achis")
    
    def ordenamiento(cola, n):
        for ordenados in range(n):

            desordenados = n - ordenados

            menor = None
            posicionDelmenor = -1
            
    
            for i in range(n):
                posi_actual = cola.pop()

                if i < desordenados:
                    if menor is None or posi_actual < menor:
                        menor = posi_actual
                        posicionDelmenor = i

                cola.push(posi_actual)

            for i in range(n):
                posi_actual = cola.pop()

                if i != posicionDelmenor:
                    cola.push(posi_actual)


            cola.push(menor)
          # Creamos una cola nueva para que no sea la misma del ejemplo del pdf     :v         
    cola = Cola()
    cola.push(89)
    cola.push(0)
    cola.push(1)
    cola.push(-11)

    cola.push(25)
    cola.push(43)
    cola.push(2)
    cola.push(8)
    cola.push(3)
    cola.push(5)
    cola.push(-13)

    n = 11
    ordenamiento(cola, n)
    cola.mostrar()




    