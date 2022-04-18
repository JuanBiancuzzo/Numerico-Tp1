from UnidadDeMaquina import UnidadDeMaquina, ComparacionSimple, ComparacionDoble

def UnidadDeMaquicaSegunBases(bases):
    for base in bases:
        print(f"Con la base {base}, tenemos las unidades de maquina: ")

        unidadSimple = UnidadDeMaquina(base, ComparacionSimple)
        unidadDoble = UnidadDeMaquina(base, ComparacionDoble)

        print(f"\tSimple: {unidadSimple} \n\tDoble: {unidadDoble}\n")

def Main():
    UnidadDeMaquicaSegunBases([2, 10])

if __name__ == "__main__":
    Main()
