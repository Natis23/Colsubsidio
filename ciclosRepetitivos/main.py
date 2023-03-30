""" 1. Crear un bucle que cuente todos los números pares hasta
el 100 ciclo for """
for Index in range (0, 100, 2):
    print(Index)

""" 2. Haz una tabla de multiplicar utilizando el ciclo for
ciclo for """
num = int(input("Digite el número de la tyabla de multiplicar: "))
for i in range(11):
  print(i, " x ", num , " = ", i * num)

""" 3. Escribir un programa que pregunte al usuario su edad y
muestre por pantalla todos los años que ha cumplido
(desde 1 hasta su edad). ciclo for """
edad = int(input("Cuantos anos tiene? "))
for e in range(1, edad, 1):
    print(e)

""" 4. Escribir un programa que pida al usuario un número entero
positivo y muestre por pantalla todos los números
impares desde 1 hasta ese número separados por comas. """
num = int(input("Escriba un numero entero? "))
for j in range(1, num):
    if j % 2 != 0:
        print(j, end= ", " )


""" 5. Encuentra la suma de todos los números pares del 1 al
100 ciclo for """
accumulator = 0
for h in range(0, 100, 1):
    accumulator = accumulator + h
print(f"\n La Suma de todos los números pares del 1 al 100 {accumulator}")