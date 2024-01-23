# se inicia la funcion que se uasara para convertir los grados celsius a grados
# fahrenheit 
def celsius_a_fahrenheit(celsius):
    
# return nos devolvera el resultado de la formula especifica para la conversion de los datos    
    return (celsius * 9/5) + 32

# se crean la variables para el ingreso de datos  con el float para que sean admitidos numeros 
# negativos y decimales para la funcion de conversion 
temperatura_celsius = float(input("Ingrese la temperatura en Celsius: "))
# variable para que los datos ingresados en el input pasen por la formula de la funcion y se haga
# la conversion 
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)

# imprime la conversion de celsius a fahrenheit mostrara el dato ingresado y el resultado 
print(f"{temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F")

# en la linea 3 faltaban los dos puntos al final  luego de escribir la funcion 
# en la formula de la linea 6 faltaba el signo sumar " + "  para que la formula estuviera correcta ,
# se debia sumar 32 al final  
# en la linea 10 faltaba crear  el input para el ingreso de datos 