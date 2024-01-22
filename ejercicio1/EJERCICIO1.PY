# se inicia la funcion llamada calculadora
def calculadora():
    # se nombran las variables numero y operacion , las variables num llevan un input y en prefijo
    # int q convierte el string en numero entero y permite la operacion
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")

    # de la linea 10 a la 21 se hacen los condicionales para las diferentes operaciones
    # que se haran con las variables anteriores 
    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = num1 / num2
    else:
        resultado = "Operación no válida"

    # linea 23 imprime el codigo del resultado de las operaciones de los condicionales
    print("Resultado: ", resultado)
    
# se llama la funcion calculadora
calculadora()

# se hcieron cambios en las lineas 5 y 6 donde se nombran las variables num1 y num 1 
# se cambio el float por el int para definir el tipo de dato a ingresar
# cambios en las lineas 12 y 18 la variable num1 estaba mal escrita 
# cambio en la linea 26 la palabra calculadora estaba mal escrita 

