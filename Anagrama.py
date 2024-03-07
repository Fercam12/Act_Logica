def es_anagrama(palabra1, palabra2):
    # Convertir las palabras a minúsculas para que la comparación sea insensible a mayúsculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    # Verificar si ambas palabras tienen la misma longitud
    if len(palabra1) != len(palabra2):
        return False

    # Ordenar las letras de ambas palabras y comparar
    return sorted(palabra1) == sorted(palabra2)

# Ejemplos de uso
print(es_anagrama("Roma", "Mora"))  # Debería imprimir True
print(es_anagrama("Lacteo", "Coleta"))  # Debería imprimir True
print(es_anagrama("Cara", "Arca"))  # Debería imprimir True
print(es_anagrama("Hola", "Mundo"))  # Debería imprimir False
