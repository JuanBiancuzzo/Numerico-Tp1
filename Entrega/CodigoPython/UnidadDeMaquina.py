
def UnidadDeMaquina(base : int, precision) -> int:
    division = 1              #definimos div=1
    valor = 1 + division      #definimos valor=1+div
    unidad = 0                #unidad =0

    #itera hasta que no se cumpla que la precision en valor sea igual a la precision en valor=1
    while not precision(valor) == precision(1):    
        division /= base       #div=div/base(10)
        valor = 1 + division   
        unidad += 1            #unidad=unidad+1

    #devolvemos unidad que fue sumandose de a uno hasta que dio(un contador)
    return unidad       
