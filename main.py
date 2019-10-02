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

def validarMayorQue(min):
    n = int(input("Ingrese la cantidad de publicaciones a buscar: "))
    while n <= min:
        print("Error!")
        n = int(input("Ingrese una cantidad valida: "))
    return n

def crearVector(n):
    vec = [None] * n
    for i in range(len(vec)):
        codigo = random.randint(1, 100000)
        precio = round(random.uniform(1, 100000), 2)
        ubicacion = random.randint(1, 23)
        estado = random.randint(0, 1)
        cantidad = random.randint(0, 1000)
        puntuacion = random.randint(1, 5)
        publicacion = Publicacion(codigo, precio, ubicacion, estado, cantidad, puntuacion)
        vec[i] = publicacion
    return vec

def mostrarVector(vec):
    for pub in vec:
        write(pub)

def ordenarPorCodigo(vec):
    n = len(vec)
    for i in range(n-1):
        for j in range(i+1, n):
            if vec[i].codigo > vec[j].codigo:
                vec[i], vec[j] = vec[j], vec[i]

    return vec

def test():
    ban = False
    op = 0
    while op != 6:
        n = validarMayorQue(0)
        vec = crearVector(n)
        sorted = ordenarPorCodigo(vec)
        mostrarVector(sorted)
        print()
        TGREEN =  '\033[32m' # TEXTO VERDE
        ENDC = '\033[m' # TEXTO DEFAULT
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
