# Solicitar al usuario los valores de N y M
N = int(input("Ingrese el valor de N: "))
M = int(input("Ingrese el valor de M: "))

# Generar y mostrar la matriz de zig-zag
matriz = []
numero = 1
direccion = int(input("Seleccione de que manera quiere rellenar la matriz: \n de izquierda a derecha coloque 1, \n de derecha a izquierda coloque -1: "))   # 1 para ir hacia la derecha, -1 para ir hacia la izquierda

for fila in range(N):
    fila_matriz = []
    for columna in range(M):
        fila_matriz.append(numero)
        numero += 1
    if direccion == -1:
        fila_matriz.reverse()
    matriz.append(fila_matriz)
    direccion *= -1

for fila in matriz:
    print(fila)