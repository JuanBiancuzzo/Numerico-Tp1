
def UnidadDeMaquina(base : int, precision) -> int:
    division = 1
    valor = 1 + division
    unidad = 0

    while not precision(valor) == precision(1):
        division /= base
        valor = 1 + division
        unidad += 1

    return unidad
