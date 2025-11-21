while True: #while que engloba todo el programa para su repetición, a partir del menu

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

    numero_seleccionado = int(input()) #asocia un numero a una de las operaciones, para luego ser utilizado en el case

    while True: #while que engloba el case, para poder repetir solo la operación de nuevo (suma, resta, multiplicación, división)

        match numero_seleccionado: #case que determina que operación eligio el usuario
            case 1:
                operacion = "suma" #variable que sera utilizada mas adelante por el while para poder realizar una suma ed nuevo
                resultado = 0 #igualar valor a 0 por si se realizara una operación a cero y no afecte el resultado anterior
                print("Ha seleccionado, realizar una operación de suma")
                print("¿Cuántos números deseas sumar?")
                cantidad_operacion = int(input())

                for i in range(cantidad_operacion): #for que sirve para poder sumar varios valores ingresados por el usuario
                    if i <= cantidad_operacion:
                        print(f"ingresa el valor {i+1}")
                        numero_ingresado = int(input()) #variable para lso valores ingresados por el usuario
                        resultado += numero_ingresado #operación de suma

            case 2:
                operacion = "resta" #variable que sera utilizada mas adelante por el while para poder realizar una suma de nuevo
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

            case 3:
                operacion = "multiplicación" #variable que sera utilizada mas adelante por el while para poder realizar una resta de nuevo
                print("Ha seleccionado, realizar una operación de multiplicación")
                print("¿Cuántos números desea multiplicar?")
                cantidad_operacion = int(input())
                print("ingresa el valor 1")
                resultado = int(input())

                for i in range(cantidad_operacion - 1): #for que sirve para poder multiplicar varios valores ingresados por el usuario
                    if i <= cantidad_operacion:
                        print(f"ingresa el valor {i+2}")
                        numero_ingresado = int(input())
                        resultado *= numero_ingresado #operación de multiplicacion

            case 4:
                operacion = "división" #variable que sera utilizada mas adelante por el while para poder realizar una division de nuevo
                print("Ha seleccionado, realizar una operación de división")
                print("¿Cuál es número dividendo?")
                dividendo = int(input())
                print("¿Cuáles el número divisor?")
                divisor = int(input())
                resultado = dividendo / divisor

            case 5:
                operacion = "potenciación" #variable que sera utilizada mas adelante por el while para poder realizar una potenciación de nuevo
                print("Ha seleccionado, realizar una operación de potenciación")
                print("Ingrese el número a potenciar")
                numero_potenciar = int(input())
                print("Ingresa el número potenciador")
                numero_potenciador = int(input())
                resultado = numero_potenciar ** numero_potenciador #operación de potenciación
            
            case _: #case por si el usuario ingresa un numero no valido en el menu
                print("Número desconocido, por favor, ingrese un numero válido")
                print("¿Qué operación deseas realizar?")
                numero_seleccionado = int(input()) #solicita al usuario que ingrese un numero valido
                continue #vuelve al inicio del while para repetir el case

        print(f"El resultado de la operación realizada es: {resultado}")
        print(f"¿Desea realizar otra {operacion}? si/no ") 
        respuesta_usuario = input().lower() #pregunta al usuario si desea realizar la misma operación de nuevo, lower para evitar errores de mayusculas

        if respuesta_usuario == "si": #if para saber si se realizara la misma operacion de nuevo
            continue #repite el while para realizar la misma operacion
        break #rompe el while para salir del case y volver al menu principal
    print("¿deseas realizar una operación distinta?")
    respuesta_usuario = input().lower() #pregunta al usuario si desea realizar una operación distinta, lower para evitar errores de mayusculas

    if respuesta_usuario == "si":
        continue  #repite el while principal para volver al menu
    break #rompe el while principal para finalizar el programa
print("Gracias por utilizar la calculadora, hasta luego!") #mensaje de despedida al finalizar el programa



