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

    '''valorPrueba = 1
    resultados = []
    for iteracion in range(20):
        resultado = FuncionSerie(valorPrueba, iteracion)
        resultados.append(resultado)
    
    resultadosNP = numpy.array(resultados)
    for resultado in resultados:
        print(resultado)
    print(resultadosNP)'''

if __name__ == "__main__":
    Main()
