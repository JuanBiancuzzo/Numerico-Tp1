from matplotlib import pyplot

from Serie import ErrorEnIteraccion

iteracionMasBaja = 1
iteracionMasAlta = 10

def MostrarTableDeValoresDeIteracion(valor : float, errorMinimo : float):
    resultados = []
    rango = range(iteracionMasBaja, iteracionMasAlta + 1)
    for i in rango:
        resultado = ErrorEnIteraccion(valor, i)
        resultados.append(resultado)

    print(resultados)

    fig = pyplot.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_yscale('log')
    pyplot.axhline(y=errorMinimo, color='r', linestyle='-')
    pyplot.title("Calculo de cantidad de iteraciones analitico") 
    pyplot.xlabel("Cantidad de iteraciones") 
    pyplot.ylabel("Valor por iteracion") 
    pyplot.plot(rango, resultados)
    pyplot.show()