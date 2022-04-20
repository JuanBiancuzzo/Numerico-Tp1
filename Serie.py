from scipy.special import factorial
import numpy

def Float32(valor : float) -> float:
    return numpy.float32(valor)

def Float64(valor : float) -> float:
    return numpy.float64(valor)

def FuncionSerie(valor : float, iteraciones : int, precision) -> float: 
    resultado = 0
    for iteracion in range(iteraciones + 1):
        signo = (-1) ** iteracion 
        dividendo = precision( signo * ( valor ** ( 2 * iteracion + 1 ) ) )
        divisor = precision( ( 2 ** iteracion ) * factorial(iteracion) * ( 2 * iteracion + 1 ) )
        resultado += precision( dividendo / divisor)
    return resultado 

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