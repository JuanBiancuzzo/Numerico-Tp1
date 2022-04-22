from UnidadDeMaquina import UnidadDeMaquina

def CPExperimentalSegunDeltaX(serieIterable, valor : float, iteraciones : int, precision, deltaX : float) -> float:
    valorIteracion = serieIterable(valor, iteraciones, precision)
    valorCorrida = serieIterable(valor * (1 + deltaX), iteraciones, precision)

    return abs(valorCorrida - valorIteracion) / (abs(valorIteracion) * abs(deltaX))

def CalcularCPExperimental(serieIterable, valor : float, iteraciones : int, precision) -> float:    
    deltaValor = 10 ** -13 # un numero suficientemente a la derecha del valor del cp
    decrecimiento = 10 ** -14

    calculoCP = lambda delta : CPExperimentalSegunDeltaX(serieIterable, valor, iteraciones, precision, delta)

    CPInicial = calculoCP(deltaValor)
    
    deltaValor -= decrecimiento
    CPSiguiente = calculoCP(deltaValor)

    while CPInicial > CPSiguiente:
        CPInicial = CPSiguiente

        deltaValor -= decrecimiento
        CPSiguiente = calculoCP(deltaValor)
    
    return CPInicial

# el calculo experimental del te es |y_d - y_s|/ mu_s |y_d|
def CalcularTEExperimental(serieIterable, valor : float, iteracion : int, precisionMayor, precisionMenor, base : int) -> float:
    valorMayor = serieIterable(valor, iteracion, precisionMayor)
    valorMenor = serieIterable(valor, iteracion, precisionMenor)
    unidad = UnidadDeMaquina(base, precisionMenor)

    return abs(valorMayor - valorMenor) / ((0.5 * (base ** -unidad)) * abs(valorMayor))