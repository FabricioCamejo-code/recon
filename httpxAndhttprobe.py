import subprocess
import json

# Rutas completas de los ejecutables de httpx
ruta_httpx = "/Users/fabri/Documents/h1/recon/httpx"

# Nombre del archivo de subdominios
archivo_subdominios = "resultados_subdominios.txt"

# Nombre del archivo de resultados
archivo_resultados = "resultadohttpx.txt"

# Comando para ejecutar httpx y guardar los resultados en un archivo JSON
comando_httpx = f"type {archivo_subdominios} | {ruta_httpx} -threads 50 -status-code -title -content-length -json -o {archivo_resultados}"

# Ejecutar el comando en una shell de Windows
subprocess.run(comando_httpx, shell=True)

# Leer el archivo de resultados línea por línea
with open(archivo_resultados, "r", encoding='utf-8') as f:
    for linea in f:
        # Cargar cada línea como un objeto JSON
        try:
            resultado_json = json.loads(linea)
        except json.JSONDecodeError as e:
            print(f"Error al decodificar la salida JSON: {e}")
            print("Línea JSON inválida:")
            print(linea)
            continue

        # Extraer la URL del resultado y escribirla en el archivo de resultados final
        url = resultado_json.get('url')
        if url:
            with open("resultadohttpx_clean.txt", "a") as resultado_final:
                resultado_final.write(url + '\n')

print("Prueba HTTP completada. Los resultados limpios se han guardado en resultadohttpx_clean.txt")

