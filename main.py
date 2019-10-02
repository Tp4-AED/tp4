import random
from registros import *
from archivos import *

def menu():
    print("1- Comprar")
    print("2- Mis compras")
    print("3- Rango de precios")
    print("4- Agregar favorito")
    print("5- Actualizar Favoritos")
    print("6- Salir")


def validarEntre(min, max, msj):
    val = int(input(msj))
    while val < min or val > max:
        print("Error!")
        val = int(input(msj))
    return val


def test():
    ban = False
    op = 0
    while op != 6:
        TGREEN =  '\033[32m' # TEXTO VERDE
        ENDC = '\033[m' # reset to the defaults
        print(TGREEN + "Sitio de compra/venta 2.0 " + ENDC)
        menu()
        op = validarEntre(1, 6, "Ingrese una opcion: ")
        if op == 1:
            pass
        if op == 2:
            pass
        if op == 3:
            pass
        if op == 4:
            pass
        if op == 5:
            pass
        if op == 6:
            pass


if __name__ == "__main__":
    test()

