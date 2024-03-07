# Función para generar los primeros 50 números de la sucesión de Fibonacci
def fibonacci(n):
    fibo_sequence = [0, 1]
    
    for i in range(2, n):
        next_number = fibo_sequence[-1] + fibo_sequence[-2]
        fibo_sequence.append(next_number)
    
    return fibo_sequence

# Imprimir los primeros 50 números de Fibonacci
primeros_50_fibonacci = fibonacci(50)
print(primeros_50_fibonacci)
