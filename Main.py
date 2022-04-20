from UnidadDeMaquina import UnidadDeMaquina
from Serie import FuncionSerie
import numpy

padron1 = 105859
padron2 = 106005
divisor = 10 ** 6

valorPrueba = (padron1 + padron2) / divisor
precisionesUsadas = [numpy.float32, numpy.float64]

def UnidadDeMaquicaSegunBases(bases, precisiones):
    for base in bases:
        print(f"Con la base {base}, tenemos las unidades de maquina: ")

        for precision in precisiones:
            unidad = UnidadDeMaquina(base, precision)
            print(f"\tCon precision {precision.__name__}: {unidad}")
        
        print()

def ResultadosSegunPrecisiones(valor : float, iteracion : int, precisiones):
    for precision in precisiones:
        print(f"Con una cantidad de iteraciones {iteracion}\n\tSe logra la precision: ", end = "")
        resultado = FuncionSerie(valor, iteracion, precision)
        print("{0:.55f}\n".format(numpy.float64(resultado)))

def Main():
    UnidadDeMaquicaSegunBases([2, 10], precisionesUsadas)
    iteracionesNecesarias = 10 # hacer el calculo de iteraciones
    ResultadosSegunPrecisiones(valorPrueba, iteracionesNecesarias, precisionesUsadas)    

if __name__ == "__main__":
    Main()
