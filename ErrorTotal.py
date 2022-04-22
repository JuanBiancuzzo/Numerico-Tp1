#(cp * r)+(te*U)+10^-14
from CalculoExperimentales import CalcularCPExperimental,CalcularTEExperimental
from UnidadDeMaquina import UnidadDeMaquina

def CalculoDeError(cp : float, te : float, mu : float, errorInherente : float, errorTruncamiento : float) -> float:
    return (cp * errorInherente) + (te * mu) + errorTruncamiento 

def ErrorTotal(serieIterable, valor, iteracion, precisionMayor, precisionMenor, base, errorTruncamiento, errorInherente):
    cp = CalcularCPExperimental(serieIterable, valor, iteracion, precisionMayor)
    te = CalcularTEExperimental(serieIterable, valor, iteracion, precisionMayor, precisionMenor, base)
    
    unidad = UnidadDeMaquina(base, precisionMayor)
    mu = 0.5* (base**-unidad)

    return CalculoDeError(cp, te, mu, errorInherente, errorTruncamiento)