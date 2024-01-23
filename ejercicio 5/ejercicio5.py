# se inicia la funcion para indentificar si un numero es primo 
def es_primo(numero):
 
# se abre condicional que devolvera falso si el  umero ingresado es menor a 2    
    if numero < 2 :
        return False
# bucle que hara una lista de numeros primos de 2 hasta el numero dado , se multiplica por 0.5 
# para que el resultado sea mas acertado
# el condicional devolvera  false si al dividir cada numero numero  por si mismo es 0 , de resto devuleve true 
# y el ciclo continuara con cada numero desde 2 hasta el limite      
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
# variable limite con el input para ingresar los datos y  int para que el dato sea identificado como
# entero y nos devuelva un numero entero 
limite = int(input("Ingrese el límite superior para encontrar números primos: "))

# variable crea el rango de la lista que mostrara los numeros primos hasta el limite dado si este numero es primo 
primos = [num for num in range(2, limite + 1) if es_primo(num)]

# este print nos imprimira la lista de numeros primos 
print("Números primos:", primos)