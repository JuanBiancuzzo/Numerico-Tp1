from scipy.special import factorial

def FuncionSerie(valor : float, iteraciones : int) -> float: 
    resultado = 0
    for iteracion in range(iteraciones + 1):
        resultado += ( ( (-1) ** iteracion ) * ( valor ** ( 2 * iteracion ) ) ) / ( ( 2 ** iteracion ) * factorial(iteracion) * ( 2 * iteracion + 1 ) )
    return resultado * valor