# import ,random y string se usan para importar una libreria de letras o numeros 
# segun tengamos la necesidad
import random 
import string

# se incicia una funcion para genrar una contraseña aleatoria con un parametro de 8 caracteres
def generar_contraseña(longitud=8):
# se crean las variables contraseña y caracteres que utilizaran las librerias y se designa
# la posicion en que iran los caracteres de las contraseñas aleatoreas     
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
# return utilizado para definir que se devolvera la contraseña que crearan las 
# lineas anteriores    
    return contraseña
# se cierra la funcion y se hace el print  que nos devolvera la contraseña 
print(generar_contraseña())
# habia un error al llamar la libreria random , estaba mal escrita
# en la linea 14 el return estaba mal escrito y se cambio
# al cerrar la funcion de generar contraseña hubo un error en la palabra 
# contraseña 