import subprocess
import os

# Paso 1: Abrir el archivo "domains.txt" para leer los dominios
with open("domains.txt", "r") as f:
    domains = f.readlines()

# Paso 2: Crear el archivo "resultados_subdominios.txt"
with open("resultados_subdominios.txt", "w", encoding="utf-8") as f:
    # Iterar sobre cada dominio
    for domain in domains:
        # Eliminar espacios en blanco y saltos de línea al final de cada dominio
        domain = domain.strip()
        
        #1 Ejecutar subfinder para buscar subdominios del dominio actual
        subfinder_result = subprocess.run(["/Users/fabri/Documents/h1/recon/subfinder", "-d", domain], capture_output=True, text=True, encoding="utf-8")
        
        #1 Escribir los resultados de subfinder en el archivo resultados_subdominios.txt
        f.write(f"Resultados de subfinder para el dominio {domain}:\n")
        f.write(subfinder_result.stdout)
        f.write("\n\n")
        
        #2 Ejecutar findomain para buscar subdominios del dominio actual
        findomain_result = subprocess.run(["/Users/fabri/Documents/h1/recon/findomain", "-t", domain], capture_output=True, text=True, encoding="utf-8")
        
        #2 Escribir los resultados de findomain en el archivo resultados_subdominios.txt
        f.write(f"Resultados de findomain para el dominio {domain}:\n")
        if findomain_result.stdout is not None:
            f.write(findomain_result.stdout)
        else:
            f.write("No se encontraron subdominios para este dominio.\n")
        f.write("\n\n")

        #3 Ejecutar sublist3r.py para buscar subdominios del dominio actual
        sublist3r_result = subprocess.run(["python", "/Users/fabri/Documents/h1/recon/sublist3r", "-d", domain], capture_output=True, text=True, encoding="utf-8")
        
        #3 Escribir los resultados de sublist3r en el archivo resultados_subdominios.txt
        f.write(f"Resultados de sublist3r para el dominio {domain}:\n")
        if sublist3r_result.stdout is not None:
            f.write(sublist3r_result.stdout)
        else:
            f.write("No se encontraron subdominios para este dominio usando sublist3r.\n")
        f.write("\n\n")

        #4 Ejecutar findomain para buscar subdominios del dominio actual
        amass_result = subprocess.run(["/Users/fabri/Documents/h1/recon/amass", "enum", "-d", "-silent", domain], capture_output=True, text=True, encoding="utf-8")
                
        #4 Escribir los resultados de amass en el archivo resultados_subdominios.txt
        f.write(f"Resultados de findomain para el dominio {domain}:\n")
        if amass_result.stdout is not None:
            f.write(amass_result.stdout)
        else:
            f.write("No se encontraron subdominios para este dominio.\n")
        f.write("\n\n")


        #5 Ejecutar ctfr para buscar subdominios del dominio actual
        ctfr_result = subprocess.run(["python", "/Users/fabri/Documents/h1/recon/ctfr/ctfr", "-d", domain], capture_output=True, text=True, encoding="utf-8")
        
        #5 Escribir los resultados de ctfr en el archivo resultados_subdominios.txt
        f.write(f"Resultados de ctfr para el dominio {domain}:\n")
        if ctfr_result.stdout is not None:
            f.write(ctfr_result.stdout)
        else:
            f.write("No se encontraron subdominios para este dominio usando ctfr.\n")
        f.write("\n\n")        

print("Se han guardado los resultados en resultados_subdominios.txt")
