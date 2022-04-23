
def FuncionFactorial(valor:int, precision)->float:
    resultado = 1
    for i in range(1,valor):
        resultado = precision(resultado * i)

    return precision(resultado)

# la variable iteracion seria la "k" en la serie
def ValorEnIteracion(valor : float, iteracion : int, precision) -> float:
    signo = (-1) ** iteracion
    dividendo = precision( signo * ( valor ** ( 2 * iteracion + 1 ) ) )
    divisor = precision( ( 2 ** iteracion ) * FuncionFactorial(iteracion,precision) * ( 2 * iteracion + 1 ) )

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

    iteracion = 0
    while CotaDeErrorEnIteraccion(valor, iteracion, precision) > errorMinimo:
        iteracion += 1
    
    return iteracion

def CondicionMinima(valor : float, iteracion : int, precision) -> bool:
    valorConNIteraciones = abs(ValorEnIteracion(valor, iteracion, precision))
    valorConNMas1Iteraciones = abs(ValorEnIteracion(valor, iteracion + 1, precision))

    #print(f"valor n: {valorConNIteraciones} y valor n+1: {valorConNMas1Iteraciones}")
    return valorConNMas1Iteraciones < valorConNIteraciones

def CantidadMinimaIteracciones(valor : float, precision) -> int:
    
    iteracion = 0

    while not CondicionMinima(valor, iteracion, precision):
        iteracion += 1

    return iteracion