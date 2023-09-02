def ejercicio():
    print("ejecucion del ejercicio 4")
    print("Bienvenido a la calculadora y evaluadora de masa corporal, a continuación ingresa la siguiente información")
    kilos = float (input("Tu peso en kilogramos: "))
    estatura = float(input("Tu estatura en metro: "))
    indice = kilos / estatura ** 2
    print("tu indice de masa corporal es de: ", indice)
    rta = int(input("¿quieres que te interprete los resultado? 1 para SÍ, cualquier otra tecla para NO "))
    if (rta == 1):
        if (indice <= 18.5):
            print ("el era paco el flaco... estas considerado como de 'bajo peso', toca darte complejo B")
        elif (indice <= 24.9):
            print ("ni fu ni fa, buen trabajo eres considerado de 'peso normal'")
        elif (indice <= 29.9):
            print ("Estamos comiendonos toda la sopita ehhh, ojo que ya eres considerado con 'sobrepeso'")
        else:
            print("ajá compadre, bajale a la cuchara que la cosa ya es sería, ya eres considerado 'obeso'")
    else:
        print("hay cosas que es mejor no saber, gracias por utilizar nuestros servicios")
        
ejercicio()
#cambio 2

