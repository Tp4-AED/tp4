#-----------------------------codigo Feli-------------------------------------
import os.path
import io
import pickle
from main import *

class Compra:
    def __init__(self, codigo, Ccomprada, precio, tipo, montoF, fecha):
        self.codigo = codigo
        self.Ccomprada = Ccomprada
        self.precio = precio
        self.tipo = tipo
        self.montoF = montoF
        self.fecha = fecha

def display(compra):
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    renglon = ""
    renglon += "Codigo: "'{:<10}'.format(compra.codigo)
    renglon += "antidad comprada: ""$" '{:<20}'.format(compra.Ccomprada)
    renglon += "Precio: "'{:<20}'.format(compra.precio)
    renglon += "Tipo de envio: "'{:<20}'.format(compra.tipo)
    renglon += "Monto total abonado: "'{:<20}'.format(compra.montoF)
    renglon += "Fecha: "'{:<20}'.format(compra.fecha)
    print(renglon)

def leerArchivo(FD):
    if not os.path.exists(FD):
        print("El archivo no existe")
    m = open(FD, 'rb')
    size = os.path.getsize(FD)
    while m.tell() < size:
        pub = pickle.load(m)
        display(pub)
    m.close()

def grabarVector(v, reg, arch):
    m = open(arch, 'wb')
    pickle.dump(reg, m)
    m.close()

#-----------------------------------------------------------------------------
