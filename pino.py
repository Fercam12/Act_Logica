def imprimir_pino_navidad(tamano):
    if tamano < 6:
        print("El tamaño del pino debe ser 6 o mayor.")
        return

    for i in range(1, tamano + 1):
        espacio = tamano - i
        asteriscos = i * 2 - 1
        print(" " * espacio + "*" * asteriscos)

    # Tronco del pino
    tronco_altura = tamano // 3
    tronco_ancho = tamano // 5
    tronco_inicio = tamano // 2 - tronco_ancho // 2

    for i in range(tronco_altura):
        print(" " * tronco_inicio + "*" * tronco_ancho)

# Solicitar al usuario el tamaño del pino
tamano_pino = int(input("Ingrese el tamaño deseado para el pino de Navidad (debe ser 6 o mayor): "))

# Imprimir el pino de Navidad
imprimir_pino_navidad(tamano_pino)
