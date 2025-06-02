import os
import shutil

# Ruta de la imagen descargada (cambia esto a la ruta donde se encuentra la imagen)
original_file_path = r'C:\Users\CompuAula 03\Downloads\Request\Fred_wierum_Velociraptor.png'  # Cambia esto a la ruta de tu imagen
# Solicitar al usuario que ingrese el nuevo nombre del archivo
new_file_name = input("123.png")

# Ruta de destino donde se guardará la imagen renombrada
download_path = r'C:\Users\CompuAula 03\Downloads'
new_file_path = os.path.join(download_path, new_file_name)

# Renombrar y mover el archivo
try:
    shutil.move(original_file_path, new_file_path)
    print(f'Imagen renombrada y guardada correctamente como {new_file_name} en {download_path}')
except FileNotFoundError:
    print('El archivo original no se encontró. Asegúrate de que la ruta sea correcta.')
except Exception as e:
    print(f'Ocurrió un error: {e}')





