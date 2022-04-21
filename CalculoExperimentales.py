from UnidadDeMaquina import UnidadDeMaquina

def CPExperimentalSegunDeltaX(serieIterable, valor : float, iteraciones : int, precision, deltaX : float) -> float:
    valorIteracion = serieIterable(valor, iteraciones, precision)
    valorCorrida = serieIterable(valor + deltaX, iteraciones, precision)

    return ((abs(valorCorrida - valorIteracion) * abs(valor)) / (abs(valorIteracion) * abs(deltaX)))    

def CaclularCPExperimental(serieIterable, valor : float, iteraciones : int, precision) -> float:    
    deltaValor = 3
    decrecimiento = 0.01

    calculoCP = lambda delta : CPExperimentalSegunDeltaX(serieIterable, valor, iteraciones, precision, delta)

    CPInicial = calculoCP(deltaValor)
    
    deltaValor -= decrecimiento
    CPSiguiente = calculoCP(deltaValor)

    while CPInicial > CPSiguiente:
        CPInicial = CPSiguiente

        deltaValor -= decrecimiento
        CPSiguiente = calculoCP(deltaValor)
    
    return CPInicial

def CalcularTEExperimental(serieIterable, valor : float, iteracion : int, precisionMayor, precisionMenor, base : int) -> float:
    valorMayor = serieIterable(valor, iteracion, precisionMayor)
    valorMenor = serieIterable(valor, iteracion, precisionMenor)
    unidad = UnidadDeMaquina(base, precisionMenor)

    return abs(valorMayor - valorMenor) / ((0.5 * (base ** -unidad)) * abs(valorMayor))