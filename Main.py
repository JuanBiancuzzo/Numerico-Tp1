import numpy

from UnidadDeMaquina import UnidadDeMaquina
from Serie import FuncionSerie, CantidadIteraciones
from CalculoExperimentales import CaclularCPExperimental, CalcularTEExperimental
from Plots import MostrarTableDeValoresDeIteracion

valorPrueba = (105859 + 106005) / 10 ** 6
errorMinimo = 10 ** (-14)
precisionesUsadas = [numpy.float32, numpy.float64]
basesUsadas = [2, 10]

def UnidadDeMaquicaSegunBases(bases, precisiones):
    for base in bases:
        print(f"Con la base {base}, tenemos las unidades de maquina: ")

        for precision in precisiones:
            unidad = UnidadDeMaquina(base, precision)
            print(f"\tCon precision {precision.__name__}: {unidad}")#__N__ para que no apresca el nombre de la clase(+ bonito)
        
        print()

def ResultadosSegunPrecisiones(valor : float, iteracion : int, precisiones):
    for precision in precisiones:
        print(f"Con una cantidad de iteraciones {iteracion}\n\tSe logra la precision: ", end = "")
        resultado = FuncionSerie(valor, iteracion, precision)
        print("{0:.55f}\n".format(numpy.float64(resultado)))

def CalculoDeCPYTEPorBases(valor : float, iteracion : int, presicionMayor, presicionMenor, bases):
    for precision in [presicionMayor, presicionMenor]:
        print(f"Con la precision {precision.__name__}:")        

        cp = CaclularCPExperimental(FuncionSerie, valor, iteracion, precision)
        print(f"\tLa Condicion del problema: {cp}")
    
    for base in bases:
        print(f"Con la base {base}: ")
        te = CalcularTEExperimental(FuncionSerie, valor, iteracion, presicionMayor, presicionMenor, base)
        print(f"\tEl termino de estabilidad: {te}")


def Main():
    valor = valorPrueba * 1
    UnidadDeMaquicaSegunBases(basesUsadas, precisionesUsadas)

    MostrarTableDeValoresDeIteracion(valor, errorMinimo)

    iteracionesNecesarias = CantidadIteraciones(valor, errorMinimo)
    ResultadosSegunPrecisiones(valor, iteracionesNecesarias, precisionesUsadas)
    CalculoDeCPYTEPorBases(valor, iteracionesNecesarias, numpy.float64, numpy.float32, basesUsadas)    

if __name__ == "__main__":
    Main()
