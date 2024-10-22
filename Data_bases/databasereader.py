import os

# Ruta donde se almacenarán las notas
output_dir = "notas_aves"

# Asegurarse de que el directorio existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Contenido de la tabla en formato markdown (el archivo que subiste)
input_file = "Aves.md"

# Función para generar el contenido de la nota
def generar_nota(row):
    contenido = f"""---
Clase: {row['Clase']}
Orden: {row['Orden']}
Familia: {row['Familia']}
Género: {row['Género']}
Especie: {row['Especie']}
Nombre_Común: {row['Nombre(s) Común(es)']}
Categoría_UICN: {row['Categoría UICN']}
Estado_Conservación_Nacional: {row['Estado de Conservación Nacional']}
Sector_RBHH: {row['Sector en la RBHH']}
Presencia: {row['Presencia']}
Tipo_de_Dato: {row['Tipo de dato']}
Fuente: {row['Fuente']}
---
"""
    return contenido

# Leer el archivo markdown y extraer las filas
with open(input_file, 'r') as f:
    lines = f.readlines()

# Convertir la tabla markdown en una lista de diccionarios
headers = ["N°", "Clase", "Orden", "Familia", "Género", "Especie", "Nombre(s) Común(es)", "Categoría UICN", "Estado de Conservación Nacional", "Sector en la RBHH", "Presencia", "Tipo de dato", "Fuente"]
rows = []

# Saltar las líneas de la tabla de markdown y crear un diccionario con cada fila
for line in lines:
    if '|' in line and not '----' in line:
        values = [x.strip() for x in line.split('|')[1:-1]]  # Tomar valores y quitar bordes
        if len(values) == len(headers):
            row = dict(zip(headers, values))
            rows.append(row)

# Generar las notas
for row in rows:
    # Crear nombre de archivo basado en el nombre común o número
    nombre_archivo = row['N°'] + "_" + row['Especie'] + ".md"
    nombre_archivo = os.path.join(output_dir, nombre_archivo)

    # Generar contenido de la nota
    contenido_nota = generar_nota(row)

    # Guardar el archivo
    with open(nombre_archivo, 'w') as nota_file:
        nota_file.write(contenido_nota)

print("Notas generadas con éxito.")
