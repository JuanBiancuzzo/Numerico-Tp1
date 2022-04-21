#(cp * r)+(te*U)+10^-14
from CalculoExperimentales import CalcularCPExperimental,CalcularTEExperimental
from UnidadDeMaquina import UnidadDeMaquina

def ErrorTotal(serieIterable, valor, iteracion, precisionMayor, precisionMenor, base, errorTruncamiento, errorIneherente):
    cp = CalcularCPExperimental(serieIterable, valor, iteracion, precisionMayor)
    te = CalcularTEExperimental(serieIterable, valor, iteracion, precisionMayor, precisionMenor, base)
    unidad = UnidadDeMaquina(base, precisionMayor)
    mu = 0.5* (base**-unidad)
    return ((cp * unidad)+(te * mu)+errorTruncamiento) 