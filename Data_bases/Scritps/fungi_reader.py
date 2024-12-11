import os

# Función para crear el archivo YAML por cada especie
def create_yaml(species_data, output_folder):
    # Crear nombre de archivo basado en la especie
    species_name = species_data['Especie'].replace(" ", "_")
    file_name = f"{species_name}.md"
    
    # Contenido del archivo YAML
    content = f"""---
Orden: {species_data['Orden']}
Familia: {species_data['Familia']}
Especie: {species_data['Especie']}
Autor: {species_data['Autor']}
---
"""
    
    # Guardar el archivo YAML en la carpeta correspondiente
    with open(os.path.join(output_folder, file_name), 'w') as yaml_file:
        yaml_file.write(content)

# Función para leer el archivo markdown y convertirlo a YAML
def read_markdown_and_convert_to_yaml(markdown_file, output_folder):
    with open(markdown_file, 'r') as file:
        lines = file.readlines()
    
    # Leer el contenido de la tabla markdown
    table_started = False
    headers = []
    data_rows = []
    
    for line in lines:
        if line.startswith('|'):
            if not table_started:
                headers = [header.strip() for header in line.split('|') if header]
                table_started = True
            else:
                row_data = [data.strip() for data in line.split('|') if data]
                if len(row_data) == len(headers):
                    data_dict = dict(zip(headers, row_data))
                    data_rows.append(data_dict)
    
    # Crear archivos YAML
    for row in data_rows:
        create_yaml(row, output_folder)

# Crear la carpeta de salida
output_folder = 'Hongos_YAML'
os.makedirs(output_folder, exist_ok=True)

# Leer el archivo markdown y convertir cada entrada a YAML
read_markdown_and_convert_to_yaml('Fungi.md', output_folder)

print(f"Archivos YAML generados en la carpeta {output_folder}")
