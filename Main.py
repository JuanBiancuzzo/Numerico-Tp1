from distutils.log import error
from numpy import float32, float64

from UnidadDeMaquina import UnidadDeMaquina
from Serie import FuncionSerie, CantidadIteraciones
from CalculoExperimentales import CalcularCPExperimental, CalcularTEExperimental
from ErrorTotal import ErrorTotal

valorPrueba = (105859 + 106005) / 10 ** 6
errorMinimo = 10 ** (-14)
precisionesUsadas = [float32, float64]
precisionDeCalculo = float64
basesUsadas = [2, 10]
baseDeCalculo = 10

# iteracion para las bases y precisiones
def UnidadDeMaquicaSegunBasesYPrecisiones(bases, precisiones):
    for base in bases:
        print(f"Con la base {base}, tenemos las unidades de maquina: ")

        for precision in precisiones:
            unidad = UnidadDeMaquina(base, precision)
            #__name__ para que no apresca el nombre de la clase(+ bonito)
            print(f"\tCon precision {precision.__name__}: {unidad}")
        
        print()

# imprime los resultados de la serie segun la precision (32 o 64 bits en los floats)
def ResultadosSegunPrecisiones(valor : float, iteracion : int, precisiones):
    for precision in precisiones:
        print(f"Con una cantidad de iteraciones {iteracion}\n\tSe logra con {precision.__name__} de precision: ", end = "")
        resultado = FuncionSerie(valor, iteracion, precision)
        print("{0:.55f}\n".format(float64(resultado)))


def CalculoDeCPYTEPorBases(valor : float, iteracion : int, presicionMayor, presicionMenor, bases):
    # El calculo del cp solo varia segun la precision
    for precision in [presicionMayor]:
        print(f"Con la precision {precision.__name__}:")        

        cp = CalcularCPExperimental(FuncionSerie, valor, iteracion, precision)
        print(f"\tLa Condicion del problema: {cp}")
    
    # el calculo experimental del te es |y_d - y_s|/ mu_s |y_d|
    for base in bases:
        print(f"Con la base {base}: ")
        te = CalcularTEExperimental(FuncionSerie, valor, iteracion, presicionMayor, presicionMenor, base)
        print(f"\tEl termino de estabilidad: {te}")

def MostrarCalculoErrorTotal(valor , errorInherente, iteracion, bases):
    for base in bases:
        print(f"Con base {base}")
        print(f"\t El error inherente relativo es : {errorInherente} ")
        error = ErrorTotal(FuncionSerie, valor, iteracion, float64, float32, base, errorMinimo, errorInherente)
        print(f"\t El error total es : {error}\n")

def Main():

    UnidadDeMaquicaSegunBasesYPrecisiones(basesUsadas, precisionesUsadas)

    for valor in [valorPrueba, valorPrueba * 15]:
        
        print(f"Con valor: {valor}")

        iteracionesNecesarias = CantidadIteraciones(valor, errorMinimo, precisionDeCalculo)
        ResultadosSegunPrecisiones(valor, iteracionesNecesarias, precisionesUsadas)

        CalculoDeCPYTEPorBases(valor, iteracionesNecesarias, float64, float32, basesUsadas)  
        MostrarCalculoErrorTotal(valor, 0, iteracionesNecesarias, basesUsadas)      #item c
        MostrarCalculoErrorTotal(valor, 0.0001, iteracionesNecesarias, basesUsadas)   #item d
        

if __name__ == "__main__":
    Main()
