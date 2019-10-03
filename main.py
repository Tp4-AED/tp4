#------------------------codigo Feli-----------------------------------------
import random
from registros import *
from archivos import *
import time

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

def validarMayorQue(min, msj):
    n = int(input(msj))
    while n <= min:
        print("Error!")
        n = int(input(msj))
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

def validarConfirmacion(msj, min, max):
    conf = int(input(msj))
    while conf < min or conf > max:
        print("Error!")
        conf = int(input("Ingrese una opcion valida: "))
    return conf

#feli
def binarySearch(vec, x):
    ban = False
    n = len(vec)
    izq, der = 0, n-1
    while izq <= der:
        c = (izq+der)//2
        if x == vec[c].codigo:
            ban = True
            print("Stock del producto: {0}".format(vec[c].cantidad))
            cant = int(input("Ingrese la cantidad que desea comprar: "))
            while vec[c].cantidad < cant:
                print("No hay stock suficiente")
                cant = int(input("Ingrese la cantidad que desea comprar: "))
            conf = validarConfirmacion("¿Desea realizar la compra?(1=si, 2=no)", 1, 2)
            if conf == 1:
                    vec[c].cantidad -= cant
                    print("Stock actualizado del producto: {0} ".format(vec[c].cantidad))
                    entrega = validarConfirmacion("¿Como desea que se realize la entrega(1: por envio, 2: retiro en sucursal)", 1, 2)
                    codig = vec[c].codigo
                    precio = vec[c].precio * cant
                    final = round(precio + (precio*0.10), 2)
                    fecha = time.strftime('%Y%m%d')
                    compra = Compra(codig, cant, precio, entrega, final, fecha)
            return compra
        elif x < vec[c].codigo:
            der = c - 1
        else:
            izq = c + 1
    return -1
    #842091,6

#belu-----------------------------------------------------------------------------------------------------
def buscador_cod(v):
    cod = False
    reg = None
    busqueda_codigo = int(input("ingrese el codigo de la publicacion a buscar: "))
    for i in range(len(v)):
        if v[i].codigo == busqueda_codigo:
            cod = True
            cant = int(input("ingrese la cantidad a comprar: "))
            if cant < v[i].cantidad:
                print("si hay disponibilidad, compra confirmada")
                v[i].cantidad = v[i].cantidad - cant
                envio = int(input("1-(desea envio a domicilio) o 2-(retirar por sucursal)"))
                precio = v[i].precio * cant
                if envio == 1:
                    monto_total = round(10 * precio / 100, 2) + precio
                else:
                    monto_total = precio

                reg = Compra(v[i].codigo, cant, precio, envio, monto_total)

            else:
                print("no hay disponibilidad, compra rechazada")
    if not cod:
        print("el codigo ingresado no existe")

    return reg
#------------------------------------------------------------------------------------------------------------------

def test():
    FD = 'miscompras.dat'
    #ban = False
    n = validarMayorQue(0, "Ingrese la cantidad de publicaciones a buscar: ")
    vec = crearVector(n)
    sorted = ordenarPorCodigo(vec)
    mostrarVector(sorted)
    op = 0
    while op != 6:
        TGREEN =  '\033[32m' # TEXTO VERDE
        ENDC = '\033[m' # TEXTO DEFAULT
        print(TGREEN + "Sitio de compra/venta 2.0 " + ENDC)
        menu()
        op = validarEntre(1, 6, "Ingrese una opcion: ")
        if op == 1:
            cod = validarMayorQue(0, "Ingrese un codigo a buscar: ")
            reg = binarySearch(sorted, cod)
            if reg == -1:
                print("Publicacion no encontrada")
            else:
                grabarVector(vec, reg, FD)
                leerArchivo(FD)
            #belu------------------------
            reg = buscador_cod(vec)
            cargar_archivo(reg)
            mostrar_archivo()
            #-------------------------------
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

#----------------------------------------------------------------------------
