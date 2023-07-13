# Ejercicio#2_Parcial

HH = float(input("Ingrese la altura del pozo: "))
Ld = float(input("Ingrese la distancia que sube en el dia: "))
Ln = float(input("Ingrese la distancia que baja en la noche: "))
d = 0
h = 0
if Ln < Ld :
    while h < H:
        h = h + Ld - Ln
        d = d + 1
    print("Tardo ", d, "dias en salir")
else:
    print("El caracol no sale del pozo")