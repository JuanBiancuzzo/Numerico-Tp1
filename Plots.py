from matplotlib import pyplot
from numpy import arange, float32, float64

from CalculoExperimentales import CalcularCPExperimental, CalcularTEExperimental
from UnidadDeMaquina import UnidadDeMaquina

from CalculoExperimentales import CPExperimentalSegunDeltaX
from Serie import CotaDeErrorEnIteraccion, CantidadMinimaIteracciones
from ErrorTotal import ErrorTotal, CalculoDeError
from Main import valorPrueba, errorMinimo, precisionDeCalculo, baseDeCalculo
from Serie import FuncionSerie, CantidadIteraciones

def MostrarTableDeValoresDeIteracion(valor : float, errorMinimo : float, precision):
    iteracionMasBaja = 1
    iteracionMasAlta = 10
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
    pyplot.ylabel("Valor de la cota de error") 
    pyplot.plot(rango, resultados)
    pyplot.grid(True)
    pyplot.show()

def MotrarTablaDeCacluloDeCP(serieIterable, valor : float, iteraciones : int, precision):
    deltaMasAlto = 10**-8

    rango = [deltaMasAlto]
    for i in range(50):
        rango.append(rango[i] / 1.2)

    resultados = []
    for i in rango:
        resultado = CPExperimentalSegunDeltaX(serieIterable, valor, iteraciones, precision, i)
        resultados.append(resultado)

    fig = pyplot.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xscale('log')
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
    rango = arange(0, 0.01, 0.000001)

    cp = CalcularCPExperimental(serieIterable, valor, iteraciones, precisionMayor)
    te = CalcularTEExperimental(serieIterable, valor, iteraciones, precisionMayor, precisionMenor, base)
    
    unidad = UnidadDeMaquina(base, precisionMayor)
    mu = 0.5* (base**-unidad)

    for i in rango:
        resultado = CalculoDeError(cp, te, mu, i, errorTruncamiento)
        resultados.append(resultado)

    fig = pyplot.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_yscale('log')
    ax.set_xscale('log')
    pyplot.axvline(x=0, color='r', linestyle='-')
    pyplot.axvline(x=0.01 / 100, color='r', linestyle='-')
    pyplot.title("Error total variando el error inherente") 
    pyplot.xlabel("Error inherente") 
    pyplot.ylabel("Error total") 
    pyplot.plot(rango, resultados)
    pyplot.grid(True)
    pyplot.show()

def MostrarTablaDeCantidadIteracionesSegunValor():
    resultados = []
    valorMinimo = 10 ** -4
    valorMaximo = 5
    valorSalto = 10 ** -2
    rango = arange(valorMinimo, valorMaximo, valorSalto)
    for i in rango:
        resultado = CantidadIteraciones(i, errorMinimo, precisionDeCalculo)  
        resultados.append(resultado)

    pyplot.axvline(x=valorPrueba, color='r', linestyle='-')
    pyplot.axvline(x=valorPrueba * 15, color='g', linestyle='-')
    pyplot.title("Calculo de cantidad de iteraciones dependiendo el valor") 
    pyplot.xlabel("Valor de x en la serie") 
    pyplot.ylabel("Cantidad de iteraciones") 
    pyplot.plot(rango, resultados)
    pyplot.grid(True)
    pyplot.show()  

def MostrarTablaDeCantidadIteracionesMinimasSegunValor():
    resultados = []
    valorMinimo = 0.1
    rango = [valorMinimo]
    for i in range(83):
        rango.append(rango[i] * 1.05)

    for i in rango:
        resultado = CantidadMinimaIteracciones(i, precisionDeCalculo)  
        resultados.append(resultado)

    fig = pyplot.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xscale('log')
    pyplot.axvline(x=valorPrueba, color='r', linestyle='-')
    pyplot.axvline(x=valorPrueba * 15, color='g', linestyle='-')
    pyplot.title("Calculo de cantidad de iteraciones\n minima para cumplir el criterio de Leibniz") 
    pyplot.xlabel("Valor de x en la serie") 
    pyplot.ylabel("Cantidad de iteraciones minima") 
    pyplot.plot(rango, resultados)
    pyplot.grid(True)
    pyplot.show()  

def MostrarTablaDeCacluloDeTE(serieIterable, valor : float, iteraciones : int, precisionMayor, precisionMenor, base):
    resultados = []
    rango = arange(0.01, 5, 0.05)

    for i in rango:
        resultado = CalcularTEExperimental(serieIterable, i, iteraciones, precisionMayor, precisionMenor, base)
        resultados.append(resultado)

    pyplot.axvline(x=valorPrueba, color='r', linestyle='-')
    pyplot.axvline(x=valorPrueba * 15, color='r', linestyle='-')
    pyplot.title("Error total variando el error inherente") 
    pyplot.xlabel("Error inherente") 
    pyplot.ylabel("Error total") 
    pyplot.plot(rango, resultados)
    pyplot.grid(True)
    pyplot.show()

def main():

    #MostrarTableDeValoresDeIteracion(valorPrueba, errorMinimo, precisionDeCalculo)
    #MostrarTablaDeCantidadIteracionesSegunValor()
    iteracionesNecesarias = CantidadIteraciones(valorPrueba, errorMinimo, precisionDeCalculo)
    MostrarTablaDeErrorTotal(FuncionSerie, valorPrueba, iteracionesNecesarias, float64, float32, baseDeCalculo, errorMinimo)
    #MotrarTablaDeCacluloDeCP(FuncionSerie, valorPrueba, iteracionesNecesarias, precisionDeCalculo)
    #MostrarTablaDeCantidadIteracionesMinimasSegunValor()
    MostrarTablaDeCacluloDeTE(FuncionSerie, valorPrueba, iteracionesNecesarias, float64, float32, baseDeCalculo)

if __name__ == "__main__":
    main()