import os
import re

def create_yaml(species_data, output_folder):
    # Función para limpiar espacios adicionales y manejar caracteres en 'Fuente'
    def clean_value(value):
        return value.strip() if value else ""

    # Función especial para manejar 'Fuente' y evitar problemas de formato YAML
    def clean_source(source_value):
        source_value = clean_value(source_value)
        # Escapar comillas dobles y envolver la fuente en comillas
        source_value = source_value.replace('"', '\\"')
        return f'"{source_value}"'

    # Crear nombre de archivo basado en la especie
    species_name = clean_value(species_data['Especie']).replace(" ", "_")
    file_name = f"{species_name}.md"  # Guardar como archivo .md
    
    # Contenido del archivo YAML con limpieza de valores, incluyendo 'Fuente'
    content = f"""---
Clase: {clean_value(species_data['Clase'])}
Orden: {clean_value(species_data['Orden'])}
Familia: {clean_value(species_data['Familia'])}
Género: {clean_value(species_data['Género'])}
Especie: {clean_value(species_data['Especie'])}
NombreComún: {clean_value(species_data['NombreComún'])}
CategoríaUICN: {clean_value(species_data['CategoríaUICN'])}
EstadoConservaciónNacional: {clean_value(species_data['EstadoConservaciónNacional'])}
SectorenlaRBHH: {clean_value(species_data['SectorenlaRBHH'])}
Presencia: {clean_value(species_data['Presencia'])}
TipoDeDato: {clean_value(species_data['TipoDeDato'])}
Fuente: {clean_source(species_data['Fuente'])}
---
"""

    # Guardar el archivo YAML en formato markdown (.md) en la carpeta correspondiente
    with open(os.path.join(output_folder, file_name), 'w') as md_file:
        md_file.write(content)

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

    # Crear archivos YAML en formato markdown (.md)
    for row in data_rows:
        create_yaml(row, output_folder)

# Unificar carpetas por clase de organismos
output_folders = {
    'Aves': 'Aves',
    'Peces': 'Peces',
    'Reptiles': 'Reptiles',
    'Anfibios': 'Anfibios',
    'Mamiferos': 'Mamiferos',
    'Insectos': 'Insectos',
    'Fungi': 'Fungi',
    'Flora': 'Flora'
}

# Asegurarse de que las carpetas existen
for folder in output_folders.values():
    os.makedirs(folder, exist_ok=True)

# Leer cada archivo markdown y convertirlo en archivos .md con formato YAML
read_markdown_and_convert_to_yaml('csv/Aves.md', output_folders['Aves'])
read_markdown_and_convert_to_yaml('csv/Peces.md', output_folders['Peces'])
read_markdown_and_convert_to_yaml('csv/Reptiles.md', output_folders['Reptiles'])
read_markdown_and_convert_to_yaml('csv/Anfibios.md', output_folders['Anfibios'])
read_markdown_and_convert_to_yaml('csv/Mamiferos.md', output_folders['Mamiferos'])
read_markdown_and_convert_to_yaml('csv/Insectos.md', output_folders['Insectos'])
read_markdown_and_convert_to_yaml('csv/Fungi.md', output_folders['Fungi'])
read_markdown_and_convert_to_yaml('csv/Flora.md', output_folders['Flora'])

