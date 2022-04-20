from UnidadDeMaquina import UnidadDeMaquina, ComparacionSimple, ComparacionDoble
from Serie import FuncionSerie
import numpy

padron1 = 105859
padron2 = 106005
divisor = 10 ** 6

valorPrueba = (padron1 + padron2) / divisor

def UnidadDeMaquicaSegunBases(bases):
    for base in bases:
        print(f"Con la base {base}, tenemos las unidades de maquina: ")

        unidadSimple = UnidadDeMaquina(base, ComparacionSimple)
        unidadDoble = UnidadDeMaquina(base, ComparacionDoble)

        print(f"\tSimple: {unidadSimple} \n\tDoble: {unidadDoble}\n")

def ResultadosSegunPrecisiones(valor : float, iteracion : int, precisiones):
    for precision in precisiones:
        print(f"Con una cantidad de iteraciones {iteracion}\n\tSe logra la precision: ", end = "")
        resultado = FuncionSerie(valor, iteracion, precision)
        print("{0:.55f}\n".format(numpy.float64(resultado)))

def Main():
    UnidadDeMaquicaSegunBases([2, 10])
    iteracionesNecesarias = 10 # hacer el calculo de iteraciones
    ResultadosSegunPrecisiones(valorPrueba, iteracionesNecesarias, [numpy.float32, numpy.float64])    

if __name__ == "__main__":
    Main()
