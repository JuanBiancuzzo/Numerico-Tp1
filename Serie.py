from scipy.special import factorial

def FuncionSerie(valor : float, iteraciones : int) -> float: 
    resultado = 0
    for iteracion in range(iteraciones + 1):
        resultado += ( ( (-1) ** iteracion ) * ( valor ** ( 2 * iteracion ) ) ) / ( ( 2 ** iteracion ) * factorial(iteracion) * ( 2 * iteracion + 1 ) )
    return resultado * valor

def CaclularCPExperimental(serieIterable, valor : float, iteraciones : int) -> float:    
    deltaValor = 0.1
    valorIteracion = serieIterable(valor, iteraciones)
    calculoCP = lambda delta : abs(serieIterable(valor * (1 + delta), iteraciones) - valorIteracion) / (abs(valorIteracion) * abs(delta))

    CPInicial = calculoCP(deltaValor)
    CPSiguiente = calculoCP(deltaValor / 10)
    while CPInicial > CPSiguiente:
        CPInicial = CPSiguiente
        CPSiguiente = calculoCP(deltaValor / 10)
    
    return CPInicial