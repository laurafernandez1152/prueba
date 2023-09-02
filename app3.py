x = 10

def imprimir_x():
    x = 5  # Esta variable x es local a la función
    print("x dentro de la función:", x)

imprimir_x()
print("x fuera de la función:", x)