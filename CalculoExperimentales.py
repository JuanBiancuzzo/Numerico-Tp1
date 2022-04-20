from UnidadDeMaquina import UnidadDeMaquina

def CaclularCPExperimental(serieIterable, valor : float, iteraciones : int, precision) -> float:    
    deltaValor = 0.1
    valorIteracion = serieIterable(valor, iteraciones, precision)
    calculoCP = lambda delta : abs(serieIterable(valor * (1 + delta), iteraciones, precision) - valorIteracion) / (abs(valorIteracion) * abs(delta))

    CPInicial = calculoCP(deltaValor)
    CPSiguiente = calculoCP(deltaValor / 10)
    while CPInicial > CPSiguiente:
        CPInicial = CPSiguiente
        CPSiguiente = calculoCP(deltaValor / 10)
    
    return CPInicial

def CalcularTEExperimental(serieIterable, valor : float, iteracion : int, precisionMayor, precisionMenor, base : int) -> float:
    valorMayor = serieIterable(valor, iteracion, precisionMayor)
    valorMenor = serieIterable(valor, iteracion, precisionMenor)
    unidad = UnidadDeMaquina(base, precisionMenor)

    return abs(valorMayor - valorMenor) / ((0.5 * (10 ** -unidad)) * abs(valorMayor))