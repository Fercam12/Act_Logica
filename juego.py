import random

def jugar_piedra_papel_tijera(opcion_usuario):
    opciones = ['piedra', 'papel', 'tijera']
    opcion_maquina = random.choice(opciones)
    
    print("La opción de la máquina es:", opcion_maquina)
    print("Tu opción es:", opcion_usuario)
    
    if opcion_usuario == opcion_maquina:
        print("¡Empate!")
    elif (opcion_usuario == 'piedra' and opcion_maquina == 'tijera') or \
         (opcion_usuario == 'papel' and opcion_maquina == 'piedra') or \
         (opcion_usuario == 'tijera' and opcion_maquina == 'papel'):
        print("¡Ganaste!")
    else:
        print("¡La máquina gana!")

# Solicitar la opción al usuario
opcion_usuario = input("Elige piedra, papel o tijera: ").lower()

# Verificar que la opción del usuario sea válida
while opcion_usuario not in ['piedra', 'papel', 'tijera']:
    print("Opción no válida. Por favor, elige piedra, papel o tijera.")
    opcion_usuario = input("Elige piedra, papel o tijera: ").lower()

# Jugar piedra, papel, tijera
jugar_piedra_papel_tijera(opcion_usuario)
