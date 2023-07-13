#Ejercicio 1 parcial

numeronumero = input("Ingrese un número de 4 dígitos: ")
if len(numero) != 4 or not numero.isdigit():
    print("El número no es válido.")
else:
    print("El número es válido.")
    semilla = int(numero)
    numeros_aleatorios = []
    for i in range(5):
        semilla = semilla ** 2
        divisor = int('1' + '0' * len(str(semilla)))
        numeros_aleatorios.append(semilla / divisor)
        semilla_str = str(semilla)
        mitad = len(semilla_str) // 2
        semilla = int(semilla_str[mitad - 2:mitad + 2])
    print("Números aleatorios generados por medio de la técnica del cuadrado medio:")
    print(numeros_aleatorios)