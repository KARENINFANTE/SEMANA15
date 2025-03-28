# Crear un diccionario llamado informacion_personal para almacenar datos de una persona
informacion_personal = {
    "nombre": "KAREN ANABEL",  # Clave "nombre" con el valor del nombre de la persona
    "edad": 18,             # Clave "edad" con el valor de la edad de la persona
    "ciudad": "Guayaquil"   # Clave "ciudad" con el valor de la ciudad de la persona
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Quito"  # Ahora la persona vive en Quito

# Agregar una nueva clave-valor para representar la "profesion"
informacion_personal["profesion"] = "Ingeniera de Software"  # Se añade la profesión de la persona

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    # Si la clave "telefono" no existe, se agrega con un número ficticio
    informacion_personal["telefono"] = "099-123-4567"

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]  # La información de la edad ya no es necesaria

# Imprimir el diccionario resultante después de todas las operaciones
print(informacion_personal)
