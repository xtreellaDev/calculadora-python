import funciones


funciones.mostrar_menu()  #llama a la función para mostrar el menu

numero_seleccionado = int(input()) #asocia un numero a una de las operaciones, para luego ser utilizado en el case

while True: #while que engloba el case, para poder repetir solo la operación de nuevo (suma, resta, multiplicación, división)

    match numero_seleccionado: #case que determina que operación eligio el usuario
        case 1:
            operacion = "suma" #variable que sera utilizada mas adelante por el while para poder realizar una suma ed nuevo
            funciones.funcion_suma()

        case 2:
            operacion = "resta" #variable que sera utilizada mas adelante por el while para poder realizar una suma de nuevo
            funciones.funcion_resta()

        case 3:
            operacion = "multiplicación" #variable que sera utilizada mas adelante por el while para poder realizar una resta de nuevo
            funciones.funcion_multiplicacion()

        case 4:
            operacion = "división" #variable que sera utilizada mas adelante por el while para poder realizar una division de nuevo
            funciones.funcion_division()

        case 5:
            operacion = "potenciación" #variable que sera utilizada mas adelante por el while para poder realizar una potenciación de nuevo
            funciones.funcion_potenciacion()

            
        case _: #case por si el usuario ingresa un numero no valido en el menu
            print("Número desconocido, por favor, ingrese un numero válido")
            print("¿Qué operación deseas realizar?")
            numero_seleccionado = int(input()) #solicita al usuario que ingrese un numero valido
            continue #vuelve al inicio del while para repetir el case

    
    print(f"¿Desea realizar otra {operacion}? si/no ") 
    respuesta_usuario = input().lower() #pregunta al usuario si desea realizar la misma operación de nuevo, lower para evitar errores de mayusculas

    if respuesta_usuario == "si": #if para saber si se realizara la misma operacion de nuevo
        continue #repite el while para realizar la misma operacion   

    print("¿deseas realizar una operación distinta?")
    respuesta_usuario = input().lower() #pregunta al usuario si desea realizar una operación distinta, lower para evitar errores de mayusculas
    if respuesta_usuario == "si":
        funciones.mostrar_menu()
        numero_seleccionado = int(input()) #asocia un numero a una de las operaciones, para luego ser utilizado en el case
        continue  #repite el while principal para volver al menu #rompe el while principal para finalizar el programa
    break
print("Gracias por utilizar la calculadora, hasta luego!") #mensaje de despedida al finalizar el programa



