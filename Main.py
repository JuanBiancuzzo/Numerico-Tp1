import numpy

def comparacion_simple(valor1 : float, valor2 : float) -> bool :
    return numpy.float32(valor1) == numpy.float32(valor2)

def comparacion_doble(valor1 : float, valor2 : float) -> bool :
    return numpy.float64(valor1) == numpy.float64(valor2)

def unidad_de_maquina(base : int, funcion_comparacion) -> int :
    valor = 1
    unidad = 0
    while not funcion_comparacion(valor, valor/10):
        valor /= base
        unidad += 1
    return unidad

def main():
    unidad = unidad_de_maquina(10, comparacion_doble)
    print(unidad)

if __name__ == "__main__":
    main()
