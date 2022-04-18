import numpy

def comparacion_simple(valor1 : float, valor2 : float) -> bool :
    return numpy.float32(valor1) == numpy.float32(valor2)

def comparacion_doble(valor1 : float, valor2 : float) -> bool :
    return numpy.float64(valor1) == numpy.float64(valor2)

def unidad_de_maquina(base : int, funcion_comparacion) -> int :
    division = 1
    valor = 1 + division
    unidad = 0

    while not funcion_comparacion(valor, 1):
        division /= base
        valor = 1 + division
        unidad += 1

    return unidad

def main():
    unidad = unidad_de_maquina(10, comparacion_simple)
    print(unidad)

if __name__ == "__main__":
    main()
