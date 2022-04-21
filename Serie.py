from scipy.special import factorial

# la variable iteracion seria la "k" en la serie
def ValorEnIteracion(valor : float, iteracion : int, precision) -> float:
    signo = (-1) ** iteracion
    dividendo = precision( signo * ( valor ** ( 2 * iteracion + 1 ) ) )
    divisor = precision( ( 2 ** iteracion ) * factorial(iteracion) * ( 2 * iteracion + 1 ) )

    return precision( dividendo / divisor )

# La funcion serie itera el calculo en ValorEnIteracion (sumatoria)
def FuncionSerie(valor : float, iteraciones : int, precision) -> float: 
    resultado = 0
    for iteracion in range(iteraciones + 1):
        resultado += ValorEnIteracion(valor, iteracion, precision)
    return precision(resultado)

# Segun el criterio de Leibniz (a_(n+1)) = Cota de error
def CotaDeErrorEnIteraccion(valor : float, n : int, precision) -> float:
    return abs(ValorEnIteracion(valor, n + 1, precision))

def CantidadIteraciones(valor : float, errorMinimo : float, precision) -> int: 

    iteracion = 1
    while CotaDeErrorEnIteraccion(valor, iteracion, precision) > errorMinimo:
        iteracion += 1
    
    return iteracion