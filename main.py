import random
from registros import *
from archivos import *
from datetime import *

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
        favorito = False
        publicacion = Publicacion(codigo, precio, ubicacion, estado, cantidad, puntuacion, favorito)
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
#--------------------funciones punto 1----------------------------------------------------------------------------------
def validarConfirmacion(msj, min, max):
    conf = int(input(msj))
    while conf < min or conf > max:
        print("Error!")
        conf = int(input("Ingrese una opcion valida: "))
    return conf

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
                    precio = round(vec[c].precio * cant, 2)
                    final = round(precio + (precio*0.10), 2)
                    fecha = date.today()
                    compra = Compra(codig, cant, precio, entrega, final, fecha)
            else:
                return 2
            return compra
        elif x < vec[c].codigo:
            der = c - 1
        else:
            izq = c + 1
    return -1

#-------------------------------------------funciones punto 3-----------------------------------------------------------
def rango_precios(v):
    b = False
    for i in range(len(v)):
        if not b:
            pmin = v[i].precio
            pmax = 0
        b = True
        if v[i].precio < pmin:
            pmin = v[i].precio
        if v[i].precio > pmax:
            pmax = v[i].precio
    print()
    print("El mayor precio que se encontro es de: $", pmax)
    print("El mayor precio que se encontro es de: $", pmin)
    print("Ingrese los precios dentro de ese rango")
    print()
    min = validarEntre(pmin, pmax, "Ingrese el precio minimo que quiere gastar: ")
    max = validarEntre(pmin, pmax, "Ingrese el precio maximo que quiere gastar: ")
    for j in range(len(v)):
        if v[j].precio > min:
            if v[j].precio < max:
                write(v[j])


#-------------------------------------------funciones punto 4-----------------------------------------------------------
def agregarFavoritos(vec, x, vf):
    ban = False
    n = len(vec)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq+der)//2
        if x == vec[c].codigo:
            ban = True
            if len(vf) is not None:
                for i in range(len(vf)):
                    if x == vf[i].codigo:
                        print("Ya existe una publicacion con ese codigo")
                        return vf
            pos = c
            break
        if x < vec[c].codigo:
            der = c - 1
        else:
            izq = c + 1
    if ban == False:
        print("Publicacion no encontrada")
        return vf
    else:
        if izq > der:
            pos = izq
        vf[pos:pos] = [vec[c]]
        return vf

#-----------------------------------------------------------------------------------------------------------------------

def test():
    banarc = False
    vf = [ ]
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
        print()
        print(TGREEN + "Sitio de compra/venta 2.0 " + ENDC)
        menu()
        op = validarEntre(1, 6, "Ingrese una opcion: ")
        if op == 1:
            cod = validarMayorQue(0, "Ingrese el codigo de la publicacion a buscar: ")
            reg = binarySearch(sorted, cod)
            if reg == -1:
                print("Publicacion no encontrada")
            elif reg == 2:
                pass
            else:
                grabarVector(reg, FD)
                generarArchivoTexto(reg)
                leerArchivo(FD)
        if op == 2:
            if os.path.exists(FD):
                y1= validarMayorQue(0, "ingrese el año de la primera fecha: ")
                m1= validarEntre(1, 12, "ingrese el mes de la primera fecha: ")
                d1= validarEntre(1, 31, "ingrese el dia de la primera fecha: ")

                y2= validarMayorQue(0, "ingrese el año de la segunda fecha: ")
                m2= validarEntre(1, 12, "ingrese el mes de la segunda fecha: ")
                d2= validarEntre(1, 31, "ingrese el dia de la segunda fecha: ")

                mostrar_archivo_fechas(FD, y1, m1, d1, y2, m2, d2)
            else:
                print("Archivo no creado")
        if op == 3:
           if os.path.exists(FD):
                rango_precios(vec)
            else:
                print("Archivo no creado")
        if op == 4:
            x = validarMayorQue(0, "Ingrese el codigo de la publicacion a buscar: ")
            vf = agregarFavoritos(sorted, x, vf)
            if vf is not None:
                mostrarVector(vf)
        if op == 5:
            if len(vf) == 0:
                print("El vector favoritos esta vacio")
            else:
                crearFavoritos(vf, FD2)
                leerArchivoFav('favoritos.dat')
       

if __name__ == "__main__":
    test()

#----------------------------------------------------------------------------

