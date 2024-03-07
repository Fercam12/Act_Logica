import datetime


def generar_correo_electronico(nombre, apellido, fecha_nacimiento, dominio="domino.com"):
    # Obtener las primeras dos letras del nombre y las últimas dos del apellido
    usuario = nombre[:2].lower() + apellido[-2:].lower()

    # Obtener el día de nacimiento y formatearlo con ceros a la izquierda si es necesario
    dia_nacimiento = str(fecha_nacimiento.day).zfill(2)

    # Construir el correo electrónico con el usuario, día de nacimiento y dominio
    correo_electronico = f"{usuario}{dia_nacimiento}@{dominio}"

    return correo_electronico

# Ejemplo de uso
nombre = "Gerardo"
apellido = "Garrido"
fecha_nacimiento = datetime.date(1999, 10, 5)  # Suponiendo formato YYYY, MM, DD

correo = generar_correo_electronico(nombre, apellido, fecha_nacimiento)
print(correo)
