
def mostrar_menu():

    #imprime el menu de la calculadora
    print("----- Menú calculadora -----")
    print("¿Qué operación deseas realizar?")
    print("""
        1.- Suma       
        2.- Resta
        3.- Multiplicación
        4.- División
        5.- Potenciación  
        """)


def funcion_suma():

    resultado = 0 #igualar valor a 0 por si se realizara una operación a cero y no afecte el resultado anterior
    print("Ha seleccionado, realizar una operación de suma")
    print("¿Cuántos números deseas sumar?")
    cantidad_operacion = int(input())

    for i in range(cantidad_operacion): #for que sirve para poder sumar varios valores ingresados por el usuario
        if i <= cantidad_operacion:
            print(f"ingresa el valor {i+1}")
            numero_ingresado = int(input()) #variable para lso valores ingresados por el usuario
            resultado += numero_ingresado #operación de suma
    
    print(f"El resultado de la suma es: {resultado}")


def funcion_resta():

    print("Ha seleccionado, realizar una operación de resta")
    print("¿Cuántos números deseas restar?")
    cantidad_operacion = int(input())
    print("ingresa el valor 1")
    resultado = int(input())

    for i in range(cantidad_operacion - 1): #for que sirve para poder restar varios valores ingresados por el usuario
        if i <=cantidad_operacion:
            print(f"ingresa el valor {i+2}")
            numero_ingresado = int(input())
            resultado -= numero_ingresado #operación de resta
    
    print(f"El resultado de la resta es: {resultado}")  


def funcion_multiplicacion():

    print("Ha seleccionado, realizar una operación de multiplicación")
    print("¿Cuántos números desea multiplicar?")
    cantidad_operacion = int(input())
    print("ingresa el valor 1")
    resultado = int(input())

    for i in range(cantidad_operacion - 1): #for que sirve para poder multiplicar varios valores ingresados por el usuario
            print(f"ingresa el valor {i+2}")
            numero_ingresado = int(input())
            resultado *= numero_ingresado #operación de multiplicacion
    
    print(f"El resultado de la multiplicación es: {resultado}")


def funcion_division():

    print("Ha seleccionado, realizar una operación de división")
    print("¿Cuál es número dividendo?")
    dividendo = int(input())
    print("¿Cuáles el número divisor?")
    divisor = int(input())
    resultado = dividendo / divisor
    print(f"El resultado de la división es: {resultado}")


def funcion_potenciacion():

    print("Ha seleccionado, realizar una operación de potenciación")
    print("Ingrese el número a potenciar")
    numero_potenciar = int(input())
    print("Ingresa el número potenciador")
    numero_potenciador = int(input())
    resultado = numero_potenciar ** numero_potenciador #operación de potenciación
    print(f"El resultado de la potenciación es: {resultado}")


