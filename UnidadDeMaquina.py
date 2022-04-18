import numpy 

def ComparacionSimple(valor1 : float, valor2 : float) -> bool:
    return numpy.float32(valor1) == numpy.float32(valor2)

def ComparacionDoble(valor1 : float, valor2 : float) -> bool:
    return numpy.float64(valor1) == numpy.float64(valor2)

def UnidadDeMaquina(base : int, funcionComparacion) -> int:
    division = 1
    valor = 1 + division
    unidad = 0

    while not funcionComparacion(valor, 1):
        division /= base
        valor = 1 + division
        unidad += 1

    return unidad

