# inicio de la funcion para contar las palabras q tiene un archivo de texto en el sistema
def contar_palabras_en_archivo(nombre_archivo):
# try es un bloque que se usa para manejar las sentencias que se le dan junto con el bloque except en la linea 15
# que se ejecutara si try falla    
    try:
        
# with es una sentencia que usa la funcion open para ingresar a un archivo ,'r' define que se abrira en modo lectura        
        with open(nombre_archivo, 'r') as archivo:
# el metodo read permite leer el contenido en este caso de archivo 
# la metodo split divide la cadena de texto una lista de subcadenas que permite el conteo de las palabras            
            contenido = archivo.read()
            palabras = contenido.split()
# return devolvera la cantidad de elementos gracias al metodo len             
            return len(palabras)
    except FileNotFoundError:
# este return devolvers una respuesta si no se cumplen las sentencias que de le dan a try en la linea 5        
        return (f"El archivo {nombre_archivo} no fue encontrado.")
# variablea que contiene el input para ingresar el nombre del archivo 
archivo_nombre = input("Ingrese el nombre del archivo de texto: ")

# este print llama la funcion y nos mostrara el resultado de la cantidad de palabras que tiene el archivo  
print(f"El archivo contiene {contar_palabras_en_archivo(archivo_nombre)} palabras.")

# en la linea 2 al iniciar la funcion faltaban los dos puntos al final de la linea de codigo
# return en la linea 17 estaba mal escrito 