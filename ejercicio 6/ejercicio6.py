# se inicia la funcion llamada palindromo ,con el parametro texto que virificara si el texto 
# ingresado es palindromo 
def es_palindromo(texto):
 
#  se le da a la variable texto el metodo join convierte los elementos del texto  en una cadena
# el metodo lower  hara que cada caracter del texto ingresado sea en minuscula 
# el metodo isalnum verificara si el contenido del texto es alfanumerico
# el return  identificara que el texto ingresado sea igual de izquierda a derecha 
    texto = ''.join(caracter.lower() for caracter in texto if caracter.isalnum())
    return texto == texto[::-1]

# variable con el input para ingresar la cadena de texto
palabra_frase = input("Ingrese una palabra o frase: ")

# condicional que identificara si la palabra es un palindromo y nosdevolvera una respuesta afirmativa 
# si no lo es devolvera una respuesta identificando que no lo es 
if es_palindromo(palabra_frase):
    print(f"{palabra_frase} es un palíndromo.")
else:
    print(f"{palabra_frase} no es un palíndromo.")
    
# en la linea 9 que inicia la funcion faltaban los dos puntos al final del codigo
# en la linea 17 en el condicional faltaba escribir  el parametro  "palabra_frase " dentro de los parentesis    