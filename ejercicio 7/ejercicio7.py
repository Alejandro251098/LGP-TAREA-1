# se inicia la funcion factorial con parametro "n" que sera el dato que sera ingresado
def factorial(n):

# condicional verificara si el numero ingresado es igual a 0 o 1 deviolvera el 1  
# de lo contrario devolvera el resultado del factorial de numero ingresado      
    if n == 0 or n == 1 :
        return 1
    else:
        return n * factorial(n - 1)

# se crea la variable numero contiene un input para ingresar el numero entero positvo para ver su factorial
numero = int(input("Ingrese un número para calcular su factorial: "))
# el print nos devolvera mostrara el resultado de factorial del numero ingresado
print(f"El factorial de {numero} es {factorial(numero)}")

# en la linea 2 al iniciar la funcion factorial faltaban los dos puntos al final de la linea de codigo 
# en la linea 6  del condicional  faltaban un signo igual que identificara que "n" debia ser igual a 1 ,
# ademas faltaban los dos puntos al final de la linea de codigo
# en  la linea 14 dentro del print al llamar la funcion factorial faltaba el parametro "numero" een los parentesis
