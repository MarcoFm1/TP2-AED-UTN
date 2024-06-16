'''
pais = None
provincia = None
precio_inicial = None
precio_final = None
Descuenos = None
recargo = None

cp = input("Ingrese el código postal del lugar de destino: ")
if len(cp) == 8 and cp[0] in "abcdefghjklmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ":
    pais = "Argentina"
    recargo = 1
    if cp[0] in "aA":
        provincia = "salta"
    elif cp[0] in "bB":
        provincia = "Provincia de BsAs"
    elif cp[0] in "cC":
        provincia = "Ciudad Autónoma de Buenos Aires"
    elif cp[0] in "dD":
        provincia = "San Luis"
    elif cp[0] in "eE":
        provincia = "Entre Ríos"
    elif cp[0] in "fF":
        provincia = "La Rioja"
    elif cp[0] in "gG":
        provincia = "Santiago del Estero"
    elif cp[0] in "hH":
        provincia = "Chaco"
    elif cp[0] in "jJ":
        provincia = "San Juan"
    elif cp[0] in "kK":
        provincia = "Catamarca"
    elif cp[0] in "lL":
        provincia = "La Pampa"
    elif cp[0] in "Mm":
        provincia = "Mendoza"
    elif cp[0] in "Nn":
        provincia = "Misiones"
    elif cp[0] in "Pp":
        provincia = "Formosa"
    elif cp[0] in "Qq":
        provincia = "Neuquén"
    elif cp[0] in "Rr":
        provincia = "Rio Negro"
    elif cp[0] in "Ss":
        provincia = "Santa Fe"
    elif cp[0] in "Tt":
        provincia = "Tucuman"
    elif cp[0] in "Uu":
        provincia = "Chubut"
    elif cp[0] in "Vv":
        provincia = "Tierra del Fuego"
    elif cp[0] in "Ww":
        provincia = "Corrientes"
    elif cp[0] in "Xx":
        provincia = "Cordoba"
    elif cp[0] in "Yy":
        provincia = "Jujuy"
    elif cp[0] in "Zz":
        provincia = "Santa Cruz"
    else:
        provincia = "No aplica"
elif len(cp) == 4 and cp[0] in "1234567890":
    pais = "Bolivia"
    provincia = "No aplica"
    recargo = 1.2
elif len(cp) == 9 and cp[0] in "1234567890" and cp[5] == "-":
    pais = "Brasil"
    if cp[0] in ("0123"):
        recargo = 1.25
        provincia = "No aplica"
    elif cp[0] in ("89"):
        recargo = 1.2
        provincia = "No aplica"
    elif cp[0] in ("4567"):
        recargo = 1.3
        provincia = "No aplica"
elif len(cp) == 7 and cp[0] in "1234567890":
    pais = "Chile"
    provincia = "No aplica"
    recargo = 1.25
elif len(cp) == 5 and cp[0] in "1234567890":
    pais = "Uruguay"
    if cp[0] == "1":
        pais = "Uruguay"
        provincia = "No aplica"
        recargo = 1.2
    else:
        pais = "Uruguay"
        provincia = "No aplica"
        recargo = 1.25
elif len(cp) == 6 and cp[0] in "1234567890":
    pais = "Paraguay"
    provincia = "No aplica"
    recargo = 1.2
else:
    pais = "Otro"
    provincia = "No aplica"
    recargo = 1.5

direccion = input("Dirección del lugar de destino: ")

tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): "))

if tipo == 0:
    precio_inicial = 1100
if tipo == 1:
    precio_inicial = 1800
if tipo == 2:
    precio_inicial = 2450
if tipo == 3:
    precio_inicial = 8300
if tipo == 4:
    precio_inicial = 10900
if tipo == 5:
    precio_inicial = 14300
if tipo == 6:
    precio_inicial = 17900

pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))

if pago == 1:
    descuento = 0.9
else:
    true_count = len(envios) - 1 
    false_count = 0
'''

envios = open("envios100HC.txt", "r", encoding="utf-8").readlines()
#1
def control():
    for line in envios:
        if "HC" in line.upper():  
            return "Hard Control"
        if "SC" in line.upper():  
            return "Soft Control"


#2
def validation(envio: str):
    print("-------")
    print(f"viendo: {envio[8:29].strip()}")
    is_mayus = False
    some_word_is_numeric = False
    actual_word = ""

    for letter in envio[8:29].strip():
        if letter.isalpha() or letter.isnumeric() or letter == " " or letter == ".":
            pass
        else:
            return False

        if letter.isalpha():
            if letter.isupper():
                if is_mayus:
                    return False
                is_mayus = True
            else:
                is_mayus = False

        if not some_word_is_numeric:
            if letter.isalpha() or letter.isnumeric():
                actual_word += letter
            else:
                if actual_word.isnumeric():
                    some_word_is_numeric = True
                actual_word = ""
        
        if actual_word.isnumeric():
            some_word_is_numeric = True
        
    if some_word_is_numeric:
        return True
    return False

true_count = 0
false_count = 0

for envio in envios[1:]:
    result = validation(envio)
    print(f"{result}")
    
    if result:
        true_count += 1
    else:
        false_count += 1

if control() == "Hard Control":
    print(f"Total Valid: {true_count}")
    print(f"Total Invalid: {false_count}")
else:
    true_count = len(envios) - 1 
    false_count = 0



def imp_acu_total():
    if control() == "Soft Control":
        pass


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
print(' (r2) - Cantidad de envios con direccion valida:', true_count)
print(' (r3) - Cantidad de envios con direccion no valida:', false_count)

print(' (r4) - Total acumulado de importes finales:', imp_acu_total())
print(' (r5) - Cantidad de cartas simples:', ccs())
print(' (r6) - Cantidad de cartas certificadas:', ccc())
print(' (r7) - Cantidad de cartas expresas:', cce())
print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor())
print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp())
print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp())
print('(r11) - Importe menor pagado por envios a Brasil:', menimp())
print('(r12) - Codigo postal del envio a Brasil con importe menor:', mencp())
print('(r13) - Porcentaje de envios al exterior sobre el total:', porc())
print('(r14) - Importe final promedio de los envios a Buenos Aires:', prom())




