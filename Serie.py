from scipy.special import factorial

def FuncionSerie(valor : float, iteraciones : int, precision) -> float: 
    resultado = 0
    for iteracion in range(iteraciones + 1):
        signo = (-1) ** iteracion 
        dividendo = precision( signo * ( valor ** ( 2 * iteracion + 1 ) ) )
        divisor = precision( ( 2 ** iteracion ) * factorial(iteracion) * ( 2 * iteracion + 1 ) )
        resultado += precision( dividendo / divisor)
    return precision(resultado)

def ErrorEnIteraccion(valor : float, n : int) -> float:
    return (valor ** (2 * n + 1)) / (((n + 1) ** n) * (2 * n + 1))


def CantidadIteraciones(valor : float, errorMinimo : float) -> int: 

    iteracion = 1
    while ErrorEnIteraccion(valor, iteracion) > errorMinimo:
        iteracion += 1
    
    return iteracion