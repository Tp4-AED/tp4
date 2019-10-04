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
    print("-" * 165)
    renglon = ""
    renglon += "Codigo: "'{:<10}'.format(compra.codigo)
    renglon += "Cantidad comprada: ""$" '{:<10}'.format(compra.Ccomprada)
    renglon += "Precio: "'{:<20}'.format(compra.precio)
    renglon += "Tipo de envio: "'{:<10}'.format(compra.tipo)
    renglon += "Monto total abonado: "'{:<20}'.format(compra.montoF)
    renglon += "Fecha: "'{:<10}'.format(compra.fecha)
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


def grabarVector(reg, arch):
    m = open(arch, 'ab')
    pickle.dump(reg, m)
    m.close()

def generarArchivoTexto(reg):
    m = open('miscompras.txt', 'at')
    m.write('\n-----------------------------------------------')
    m.write('\nCompra: {} - {} '.format(reg.codigo, reg.fecha))
    m.write('\nResumen de compra:')
    m.write('\nProducto: ${} ({} x ${})'.format(round(reg.precio, 2)* reg.Ccomprada, reg.Ccomprada, round(reg.precio, 2)))
    m.write('\nCargo de envio: ${}'.format(round(((reg.precio * reg.Ccomprada)*0.10), 2)))
    m.write('\nTu pago: ${}'.format(round(((reg.precio * reg.Ccomprada)*0.10) + reg.precio * reg.Ccomprada), 2))

