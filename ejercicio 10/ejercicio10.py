# se inicia la funcion  que calculara un descuento segun los parametros dados en el parentesis 
def calcular_precio_con_descuento(precio_base, porcentaje_descuento):
 
# se crea la variable descuento que contendra la formula para el calculo segun el precio base y el porcentaje de descuento
# variable precio final restara al precio base el resultado del descuento 
# el retunr nos devolvera el precio final      
    descuento = precio_base * (porcentaje_descuento / 100)
    precio_final = precio_base - descuento
    return precio_final

# variables "precio base" y "porcentaje descuento" contien input para el ingreso de datos y la clase float que identificara 
# el tipo de dato ingresado que sea numero entero , decimal o negativo 
precio_base = float(input("Ingrese el precio base del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
# variable "precio final" llama la funcion  para que sea ejecutada segun los parametros y contenga el resultado 
precio_final = calcular_precio_con_descuento(precio_base, porcentaje_descuento)
# print nos mostrara el resultado de descuento final y el porcentaje que se le aplico 
print(f"El precio final con {porcentaje_descuento}% de descuento es: {precio_final}")

# en la linea 2 al iniciar la funcion faltaba  la palabra def para crearla , ademas en el nombre de la funcion 
# la palabra descuento estaba mal escrita no permitia volverla a llamar  , tambien se agregaron los dos puntos 
# al final de la linea de codigo
# en la linea 9  el return para devolver el resultado estaba mal escrito 
# en la linea 13  se agrego el input para el ingreso de datos