import re
import os
import time  # Para generar un timestamp

# Definir una función para analizar cada línea del registro
def parse_log_line(line):
    # Patrón principal de expresión regular para los logs
    pattern = r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - \[(?P<date>[\w:/]+)\s[+-]\d{4}\] "(?P<method>\w+) (?P<url>\S+) HTTP/\d+\.\d+" (?P<status>\d{3}) (?P<size>\S+) "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"'
    match = re.match(pattern, line)

    if match:
        return match.groupdict()

# Ruta del archivo de log
log_file_path = 'C:\\Bootcamp-Python24\\Bootcamp-Python24\\Practicas 3\\http_access_200304.log'  # Cambiar la ruta por la que coincida con el trabajo/proyecto

# Verificar si el archivo existe antes de intentar abrirlo
if not os.path.exists(log_file_path):
    print(f"El archivo de log no se encontró en la ruta: {log_file_path}")
else:
    log_data = []
    with open(log_file_path, 'r') as file:
        for line in file:
            parsed_line = parse_log_line(line)
            if parsed_line:
                log_data.append(parsed_line)

        # Definir filtros
        os_filter = 'Mac OS'  # Cambia este valor o déjalo como None si no quieres filtrar por Sistema Operativo
        code_filter = '200'  # Cambia este valor o déjalo como None si no quieres filtrar por código
        ip_filter = None  # Cambia este valor o déjalo como None si no quieres filtrar por IP
        date_filter = None  # Cambia este valor o déjalo como None si no quieres filtrar por fecha
        method_filter = None  # Cambia este valor o déjalo como None si no quieres filtrar por método
        url_filter = None  # Cambia este valor o déjalo como None si no quieres filtrar por URL
        size_filter = None  # Cambia este valor o déjalo como None si no quieres filtrar por tamaño
        referrer_filter = None  # Cambia este valor o déjalo como None si no quieres filtrar por referer
        user_agent_filter = None  # Cambia este valor o déjalo como None si no quieres filtrar por user agent

        # Filtrar los datos
        filtered_data = []
        for entry in log_data:
            if (os_filter.lower() in entry['user_agent'].lower() and entry['status'] == code_filter):
                if (ip_filter is None or entry['ip'] == ip_filter) and \
                   (date_filter is None or entry['date'] == date_filter) and \
                   (method_filter is None or entry['method'] == method_filter) and \
                   (url_filter is None or entry['url'] == url_filter) and \
                   (size_filter is None or entry['size'] == size_filter) and \
                   (referrer_filter is None or entry['referrer'] == referrer_filter) and \
                   (user_agent_filter is None or user_agent_filter.lower() in entry['user_agent'].lower()):
                    filtered_data.append(entry)

        # Función para generar un nombre de archivo único
        def generar_nombre_archivo():
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            return f"resultados_filtrados_{timestamp}.csv"

        # Guardar los resultados filtrados en un CSV con nombre único
        if filtered_data:
            nombre_archivo = generar_nombre_archivo()
            with open(nombre_archivo, 'w') as csvfile:
                # Escribir encabezados
                csvfile.write("ip,date,method,url,status,size,referrer,user_agent\n")
                # Escribir cada entrada filtrada
                for entry in filtered_data:
                    csvfile.write(f"{entry['ip']},{entry['date']},{entry['method']},{entry['url']},{entry['status']},{entry['size']},{entry['referrer']},{entry['user_agent']}\n")
            print(f"Los resultados filtrados han sido guardados en '{nombre_archivo}'.")
        else:
            print("No se encontraron resultados con los filtros aplicados.")