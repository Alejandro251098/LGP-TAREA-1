# el import y random impportan una libreria de nhmeros aleatorea que se podra usar 
import random

# se inicia una funcion para simular el resultado de lanzamientos de dados  con los parametros de 
# la cantidad de dados y la cantidad de  caras de los dados 
def simular_lanzamiento_dados(cantidad_dados, caras_por_dado):
 
#  se crea la variable resultados que contendra la llamada a la libreria ramdom para el resultados de las caras de los cantidad_dados
#  y un rango para la cantidad de dados
# el return nos devolvera  el resultados de las caras de los dados     
    resultados = [random.randint(1, caras_por_dado) for _ in range(cantidad_dados)]
    return resultados

# variables "cantidad dados y caras por dados" que contienen los input con la clase int para indentificar que los datos
# ingresados sean numeros enteros
cantidad_dados = int(input("Ingrese la cantidad de dados a lanzar: "))
caras_por_dado = int(input("Ingrese la cantidad de caras por dado: "))

# variable "lanzamientos" que llama a la funcion "simular lanzamientos dados " con los parametros anteriores 
# para que sean devueltos los resultados 
lanzamientos = simular_lanzamiento_dados( cantidad_dados , caras_por_dado)
# imprime el resultado  aleatoreo de los lanzamientos  dependiendo de la cantidad de dados y las cantidad de caras 
print(f"Resultados del lanzamiento: {lanzamientos}")

# en la linea 2  estaba mal escrito el random para llamar la libreria 
# en la linea 6 al iniciar la funcion faltaban los dos puntos al final de la linea de codigo
# en la linea 12  estaba mal escrito el return que devuelve los resultados 
# en la linea 21  faltaba  el parametro "cantidad_dados" dentro del parentesis q llama la funcion 