#Caja registradora :c

productos = []
venta_realizada = False

while not venta_realizada:
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Ver productos")
    print("4. Realizar venta")
    print("5. Salir")


    opcion = input("Ingrese una opción: ")

    if opcion.isdigit():


      if opcion == "1":
          # Agregar producto
          while True:
            nombre_producto = input("Ingrese el nombre del producto: ")
            if not nombre_producto.isdigit():
              break
            else:
              print("Nombre inválido")
          while True:
            try:
              precio_producto = float(input("Ingrese el precio del producto: "))
              break
            except ValueError:
              print("Precio inválido")
          while True:
            try:
              cantidad_producto = int(input("Ingrese la cantidad del producto: "))
              break
            except ValueError:
              print("Cantidad invalida")
          productos.append({"nombre_producto": nombre_producto, "precio_producto": precio_producto, "cantidad_producto": cantidad_producto})
      elif opcion == "2":
          # Eliminar producto
          nombre_producto_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
          for i, producto in enumerate(productos):
              if producto['nombre_producto'] == nombre_producto_eliminar:
                  productos.pop(i)
                  print(f"El producto {nombre_producto_eliminar} ha sido eliminado")
                  break
          else:
              print(f"No se encontró el producto {nombre_producto_eliminar}")
      elif opcion == "3":
          # Ver productos
          for i, producto in enumerate(productos):
              print(f"{i + 1}. {producto['nombre_producto']} - ${producto['precio_producto']} - {producto['cantidad_producto']} unidades disponibles")
      elif opcion == "4":
          # Realizar venta
          total = 0
          while True:
              print("Productos disponibles:")
              for i, producto in enumerate(productos):
                  print(f"{i + 1}. {producto['nombre_producto']} - ${producto['precio_producto']} - {producto['cantidad_producto']} unidades disponibles")
              opcion_producto = input("Ingrese el número del producto que desea comprar (0 para salir): ")
              if opcion_producto == "0":
                  break
              else:
                  try:
                      opcion_producto = int(opcion_producto)
                      if opcion_producto < 1 or opcion_producto > len(productos):
                          raise ValueError()
                      else:
                          producto_seleccionado = productos[opcion_producto - 1]
                          cantidad_comprar = int(input(f"Ingrese la cantidad de {producto_seleccionado['nombre_producto']} que desea comprar: "))
                          if cantidad_comprar > producto_seleccionado['cantidad_producto']:
                              print(f"No hay suficientes unidades de {producto_seleccionado['nombre_producto']}")
                          else:
                              total += cantidad_comprar * producto_seleccionado['precio_producto']
                              producto_seleccionado['cantidad_producto'] -= cantidad_comprar
                              print(f"Se han comprado {cantidad_comprar} unidades de {producto_seleccionado['nombre_producto']}")
                  except ValueError:
                      print("Opción inválida")
          print(f"El total de la venta es ${total}")
          venta_realizada = True
      elif opcion == "5":
          # Salir
          break
      else:
          print("Opción inválida")
    else:
      print("Opción inválida")