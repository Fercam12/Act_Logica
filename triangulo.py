def triangulo_de_pascal(filas):
    triangulo = [[1] * (i + 1) for i in range(filas)]

    for i in range(2, filas):
        for j in range(1, i):
            triangulo[i][j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]

    return triangulo

def imprimir_triangulo(triangulo):
    for fila in triangulo:
        print(" ".join(map(str, fila)))

# Solicitar al usuario la cantidad de filas
cantidad_filas = int(input("Ingrese la cantidad de filas para el Triángulo de Pascal: "))

# Calcular y mostrar el Triángulo de Pascal
triangulo_resultante = triangulo_de_pascal(cantidad_filas)
imprimir_triangulo(triangulo_resultante)
