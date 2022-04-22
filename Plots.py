from matplotlib import pyplot
from numpy import arange, float32, float64

from CalculoExperimentales import CPExperimentalSegunDeltaX
from Serie import CotaDeErrorEnIteraccion
from ErrorTotal import ErrorTotal, CalculoDeError
from Main import valorPrueba, errorMinimo, precisionDeCalculo, baseDeCalculo
from Serie import FuncionSerie, CantidadIteraciones

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

    pyplot.title("Valores de la serie") 
    pyplot.xlabel("Numero de iteraciones") 
    pyplot.ylabel("Valor de la serie") 
    pyplot.plot(rango, resultados)
    pyplot.grid(True)
    pyplot.show()

def MostrarTablaDeErrorTotal(serieIterable, valor : float, iteraciones : int, precisionMayor, precisionMenor, base, errorTruncamiento):
    resultados = []
    rango = arange(0, 0.1, 0.001)

    cp = CalcularCPExperimental(serieIterable, valor, iteracion, precisionMayor)
    te = CalcularTEExperimental(serieIterable, valor, iteracion, precisionMayor, precisionMenor, base)
    
    unidad = UnidadDeMaquina(base, precisionMayor)
    mu = 0.5* (base**-unidad)

    for i in rango:
        resultado = CalculoDeError(cp, te, mu, errorInherente, i)
        resultados.append(resultado)

    pyplot.title("Error total variando el error inherente") 
    pyplot.xlabel("Error inherente") 
    pyplot.ylabel("Error total") 
    pyplot.plot(rango, resultados)
    pyplot.grid(True)
    pyplot.show()
    

def main():
    iteracionesNecesarias = CantidadIteraciones(valorPrueba, errorMinimo, precisionDeCalculo)
    MostrarTablaDeErrorTotal(FuncionSerie, valorPrueba, iteracionesNecesarias, float64, float32, baseDeCalculo, errorMinimo)

if __name__ == "__main__":
    main()