# se inicia una funcion para contar palabras con los parametros texto y palabra 
def contar_palabra(texto, palabra):
# el return devolvera la cantidad de veces que se repute una palabra en el texto
# lower hace quetodas las letras sean minisculas en la cadena de texto de los parametros texto y
#  palabra , split divide los caracteres de la cadena de texto 
# y count devuelve la cantidad de veces que se repita una palabra segun el parametro dado    
    return texto.lower().split().count(palabra.lower())

# se crean las variables texto  para crear un ejemplo y de palabra buscada qur llevara la palabra 
# que queremos saber la veces que se repite
texto = "Este es un ejemplo de texto . Este texto tiene palabras repetidas."
palabra_buscada = "texto"

# se hace el prin y se cierra la funcion con los parametros que queremos que queremos ver 
# en este caso la cantidad de veces que se repite la palabra texto en una frase
# print(f"La palabra {palabra_buscada, "aparece", contar_palabra(texto, palabra_buscada)} veces.")


def contar_palabra(texto, palabra):
    return texto.lower().split().count(palabra.lower())

texto = "Este es un ejemplo de texto. Este texto tiene palabras repetidas."
palabra_buscada = "texto"

print(f"La palabra {palabra_buscada ," aparece", contar_palabra(texto, palabra_buscada)} veces.")