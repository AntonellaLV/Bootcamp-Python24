import pandas as pd
import re
import matplotlib.pyplot as plt

# Definir una función para analizar cada línea del registro
def parse_log_line(line):
    # Actualiza el patrón de expresión regular para incluir varios formatos
    pattern = r'(?P<ip>[\d\.]+) - - \[(?P<date>.*?)\] "(?P<method>\w+) (?P<url>.*?) HTTP/[\d\.]+" (?P<status>\d{3}) (?P<size>\d+) "(?P<referrer>.*?)" "(?P<user_agent>.*?)"'
    match = re.match(pattern, line)
    
    # Si no coincide, intenta con un patrón alternativo que ignore el tamaño
    if not match:
        pattern_alternativo = r'(?P<ip>[\d\.]+) - - \[(?P<date>.*?)\] "(?P<method>\w+) (?P<url>.*?) HTTP/[\d\.]+" (?P<status>\d{3}) (?P<size>\d+)? "(?P<referrer>.*?)" "(?P<user_agent>.*?)"'
        match = re.match(pattern_alternativo, line)
    
    if match:
        return match.groupdict()
    else:
        print(f"No match: {line}")  # Imprimir líneas que no coinciden

# Leer el archivo y aplicar la función de análisis
log_data = []
with open('http_access_200304.log', 'r') as file:
    for line in file:
        parsed_line = parse_log_line(line)
        if parsed_line:
            log_data.append(parsed_line)

# Convertir a DataFrame
df = pd.DataFrame(log_data)

# Imprimir el DataFrame para verificar que se creó correctamente
print("Contenido del DataFrame:")
print(df.head())

# Imprimir las columnas del DataFrame
print("Columnas en el DataFrame:")
print(df.columns)

# Filtrar las solicitudes con estado 200
if not df.empty:
    status_200 = df[df['status'] == '200']
    print("\nSolicitudes con estado 200:")
    print(status_200)

    # Contar las IPs
    ip_counts = df['ip'].value_counts()
    print("\nConteo de IPs:")
    print(ip_counts)

    # Contar las URLs
    url_counts = df['url'].value_counts()
    print("\nConteo de URLs:")
    print(url_counts)

    # Gráfico de las solicitudes por IP
    ip_counts.plot(kind='bar', title='Número de Solicitudes por IP')
    plt.xlabel('IP')
    plt.ylabel('Número de Solicitudes')
    plt.show()

# Suponiendo que 'df' es tu DataFrame que contiene los resultados del análisis
if not df.empty:  # Verifica que el DataFrame no esté vacío
    # Guardar resultados en un archivo CSV
    df.to_csv('resultados_analisis.csv', index=False)
    print("Los resultados han sido guardados en 'resultados_analisis.csv'.")
else:
    print("No se encontraron entradas válidas en el archivo de log.")