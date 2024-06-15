envios = open("envios25.txt", encoding="utf-8")


def control():
    for i in envios:
        if "HC" in i:
            return "Hard Control"
        else:
            return "Soft Control"
        
def cedvalid():
    con = 0
    for i in envios:
        i = i.replace(' ','')
        i = i.replace('.','')
        if i.isdigit() and i.isalpha():
            con = con+1
    return con

def cedinvalid():
    return ""

def imp_acu_total():
    return ""

def ccs():
    return ""

def ccc():
    return ""

def cce():
    return ""

def tipo_mayor():
    return ""

def cce():
    return ""

def primer_cp():
    return ""

def cce():
    return ""

def cant_primer_cp():
    return ""

def menimp():
    return ""

def mencp():
    return ""

def porc():
    return ""

def prom():
    return ""


print(' (r1) - Tipo de control de direcciones:', control())
print(' (r2) - Cantidad de envios con direccion valida:', cedvalid())
print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid())
print(' (r4) - Total acumulado de importes finales:', imp_acu_total)
print(' (r5) - Cantidad de cartas simples:', ccs)
print(' (r6) - Cantidad de cartas certificadas:', ccc)
print(' (r7) - Cantidad de cartas expresas:', cce)
print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor)
print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp)
print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp)
print('(r11) - Importe menor pagado por envios a Brasil:', menimp)
print('(r12) - Codigo postal del envio a Brasil con importe menor:', mencp)
print('(r13) - Porcentaje de envios al exterior sobre el total:', porc)
print('(r14) - Importe final promedio de los envios a Buenos Aires:', prom)

