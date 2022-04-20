from UnidadDeMaquina import UnidadDeMaquina, ComparacionSimple, ComparacionDoble
from Serie import FuncionSerie
import numpy

def UnidadDeMaquicaSegunBases(bases):
    for base in bases:
        print(f"Con la base {base}, tenemos las unidades de maquina: ")

        unidadSimple = UnidadDeMaquina(base, ComparacionSimple)
        unidadDoble = UnidadDeMaquina(base, ComparacionDoble)

        print(f"\tSimple: {unidadSimple} \n\tDoble: {unidadDoble}\n")

def Main():
    UnidadDeMaquicaSegunBases([2, 10])

    valorPrueba = (106005 + 105859) / (10 ** 6)
    resultados = []

    for iteracion in range(20):
        resultado = FuncionSerie(valorPrueba, iteracion, numpy.float32)
        resultados.append(resultado)
    
    for resultado in resultados:
        print("{0:.32f}".format(numpy.float64(resultado)))
    

if __name__ == "__main__":
    Main()
