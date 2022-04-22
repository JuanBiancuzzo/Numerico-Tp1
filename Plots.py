from matplotlib import pyplot
from numpy import arange, exp, log

from CalculoExperimentales import CPExperimentalSegunDeltaX
from Serie import CotaDeErrorEnIteraccion
from ErrorTotal import ErrorTotal

iteracionMasBaja = 1
iteracionMasAlta = 10

deltaMasBajo = 10**-10
deltaMasAlto = 10**-9
deltaSalto = 10 ** (-11)

def MostrarTableDeValoresDeIteracion(valor : float, errorMinimo : float, precision):
    resultados = []
    rango = range(iteracionMasBaja, iteracionMasAlta + 1)
    for i in rango:
        resultado = CotaDeErrorEnIteraccion(valor, i, precision)
        resultados.append(resultado)

    fig = pyplot.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_yscale('log')
    pyplot.axhline(y=errorMinimo, color='r', linestyle='-')
    pyplot.title("Calculo de cantidad de iteraciones analitico") 
    pyplot.xlabel("Cantidad de iteraciones") 
    pyplot.ylabel("Valor por iteracion") 
    pyplot.plot(rango, resultados)
    pyplot.grid(True)
    pyplot.show()

def MotrarTablaDeCacluloDeCP(serieIterable, valor : float, iteraciones : int, precision):
    resultados = []
    rango = arange(deltaMasBajo, deltaMasAlto, deltaSalto)
    for i in rango:
        resultado = CPExperimentalSegunDeltaX(serieIterable, valor, iteraciones, precision, i)
        resultados.append(resultado)

    pyplot.title("Calculo de CP Experimental") 
    pyplot.xlabel("Valores de dx/x") 
    pyplot.ylabel("Valores de CP experimental") 
    pyplot.plot(rango, resultados)
    pyplot.grid(True)
    pyplot.show()

# por ahora no pude hacer el plot bien
def MostrarTablaDeValoresDeFuncion(serieIterable, valor : float, iteraciones : int, precision):
    resultados = []
    rango = range(0, iteraciones)
    for i in rango:
        resultado = serieIterable(valor, i, precision)
        resultados.append(resultado)

    for resultado in resultados:
        print(resultado)

    pyplot.title("Valores de la serie") 
    pyplot.xlabel("Numero de iteraciones") 
    pyplot.ylabel("Valor de la serie") 
    pyplot.plot(rango, resultados)
    pyplot.grid(True)
    pyplot.show()

def MostrarTablaDeErrorTotal():
    pass