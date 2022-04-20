from UnidadDeMaquina import UnidadDeMaquina
from Serie import FuncionSerie, CantidadIteraciones
from CalculoExperimentales import CaclularCPExperimental, CalcularTEExperimental
import numpy

valorPrueba = (105859 + 106005) / 10 ** 6
errorMinimo = 10 ** (-14)
precisionesUsadas = [numpy.float32, numpy.float64]

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

def Main():
    valor = valorPrueba * 15
    UnidadDeMaquicaSegunBases([2, 10], precisionesUsadas)
    iteracionesNecesarias = CantidadIteraciones(valor, errorMinimo)
    ResultadosSegunPrecisiones(valor, iteracionesNecesarias, precisionesUsadas)

    cp = CaclularCPExperimental(FuncionSerie, valor, iteracionesNecesarias, numpy.float64)
    te = CalcularTEExperimental(FuncionSerie, valor, iteracionesNecesarias, numpy.float32, numpy.float64, 10)
    print(f"cp: {cp}, te: {te}")

if __name__ == "__main__":
    Main()
