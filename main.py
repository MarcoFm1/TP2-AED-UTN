'''
pais = None
provincia = None
precio_inicial = None
precio_final = None
Descuenos = None
recargo = None

cp = input("Ingrese el código postal del lugar de destino: ")
if cont_cp_final == 8 and lista_cp[0] in "abcdefghjklmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ":
    pais = "Argentina"
    recargo = 1
    if lista_cp[0] in "aA":
        provincia = "salta"
    elif lista_cp[0] in "bB":
        provincia = "Provincia de BsAs"
    elif lista_cp[0] in "cC":
        provincia = "Ciudad Autónoma de Buenos Aires"
    elif lista_cp[0] in "dD":
        provincia = "San Luis"
    elif lista_cp[0] in "eE":
        provincia = "Entre Ríos"
    elif lista_cp[0] in "fF":
        provincia = "La Rioja"
    elif lista_cp[0] in "gG":
        provincia = "Santiago del Estero"
    elif lista_cp[0] in "hH":
        provincia = "Chaco"
    elif lista_cp[0] in "jJ":
        provincia = "San Juan"
    elif lista_cp[0] in "kK":
        provincia = "Catamarca"
    elif lista_cp[0] in "lL":
        provincia = "La Pampa"
    elif lista_cp[0] in "Mm":
        provincia = "Mendoza"
    elif lista_cp[0] in "Nn":
        provincia = "Misiones"
    elif lista_cp[0] in "Pp":
        provincia = "Formosa"
    elif lista_cp[0] in "Qq":
        provincia = "Neuquén"
    elif lista_cp[0] in "Rr":
        provincia = "Rio Negro"
    elif lista_cp[0] in "Ss":
        provincia = "Santa Fe"
    elif lista_cp[0] in "Tt":
        provincia = "Tucuman"
    elif lista_cp[0] in "Uu":
        provincia = "Chubut"
    elif lista_cp[0] in "Vv":
        provincia = "Tierra del Fuego"
    elif lista_cp[0] in "Ww":
        provincia = "Corrientes"
    elif lista_cp[0] in "Xx":
        provincia = "Cordoba"
    elif lista_cp[0] in "Yy":
        provincia = "Jujuy"
    elif lista_cp[0] in "Zz":
        provincia = "Santa Cruz"
    else:
        provincia = "No aplica"
elif cont_cp_final == 4 and lista_cp[0] in "1234567890":
    pais = "Bolivia"
    provincia = "No aplica"
    recargo = 1.2
elif cont_cp_final == 9 and lista_cp[0] in "1234567890" and cp[5] == "-":
    pais = "Brasil"
    if lista_cp[0] in ("0123"):
        recargo = 1.25
        provincia = "No aplica"
    elif lista_cp[0] in ("89"):
        recargo = 1.2
        provincia = "No aplica"
    elif lista_cp[0] in ("4567"):
        recargo = 1.3
        provincia = "No aplica"
elif cont_cp_final == 7 and lista_cp[0] in "1234567890":
    pais = "Chile"
    provincia = "No aplica"
    recargo = 1.25
elif cont_cp_final == 5 and lista_cp[0] in "1234567890":
    pais = "Uruguay"
    if lista_cp[0] == "1":
        pais = "Uruguay"
        provincia = "No aplica"
        recargo = 1.2
    else:
        pais = "Uruguay"
        provincia = "No aplica"
        recargo = 1.25
elif cont_cp_final == 6 and lista_cp[0] in "1234567890":
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

envios = open("envios100SC.txt", "r", encoding="utf-8").readlines()
#1
def control():
    for line in envios:
        if "HC" in line.upper():  
            return "Hard Control"
        if "SC" in line.upper():  
            return "Soft Control"


#2
def validation(envio: str):
    # print("-------")
    # print(f"viendo: {envio[8:29].strip()}")
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
    # print(f"{result}")
    
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
    importe_acumulado = 0
    
    if control() == "Soft Control":
        for linea in envios[1:]:
            lista_cp = []
            cont_cp = 0
            # print("-----------")
            for letra in linea[:9]:
                cp = letra
                lista_cp.append(cp)
                # print(cp)
                cont_cp += 1
            cont_cp_final = cont_cp
            # print("letras: ", cont_cp_final)
            # print(lista_cp)
            
            # Determinar país y recargo
            if cont_cp_final == 8 and lista_cp[0] in "abcdefghjklmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ":
                pais = "Argentina"
                recargo = 1
            elif cont_cp_final == 4 and lista_cp[0] in "1234567890":
                pais = "Bolivia"
                provincia = "No aplica"
                recargo = 1.2
            elif cont_cp_final == 9 and lista_cp[0] in "1234567890" and lista_cp[5] == "-":
                pais = "Brasil"
                if lista_cp[0] in ("0123"):
                    recargo = 1.25
                    provincia = "No aplica"
                elif lista_cp[0] in ("89"):
                    recargo = 1.2
                    provincia = "No aplica"
                elif lista_cp[0] in ("4567"):
                    recargo = 1.3
                    provincia = "No aplica"
            elif cont_cp_final == 7 and lista_cp[0] in "1234567890":
                pais = "Chile"
                provincia = "No aplica"
                recargo = 1.25
            elif cont_cp_final == 5 and lista_cp[0] in "1234567890":
                pais = "Uruguay"
                if lista_cp[0] == "1":
                    provincia = "No aplica"
                    recargo = 1.2
                else:
                    provincia = "No aplica"
                    recargo = 1.25
            elif cont_cp_final == 6 and lista_cp[0] in "1234567890":
                pais = "Paraguay"
                provincia = "No aplica"
                recargo = 1.2
            else:
                pais = "Otro"
                provincia = "No aplica"
                recargo = 1.5 

            # Calcular el monto basado en tipo de envio
            tipo = linea[29]
            precio_inicial = 0
            if tipo == '0':
                precio_inicial = 1100
            elif tipo == '1':
                precio_inicial = 1800
            elif tipo == '2':
                precio_inicial = 2450
            elif tipo == '3':
                precio_inicial = 8300
            elif tipo == '4':
                precio_inicial = 10900
            elif tipo == '5':
                precio_inicial = 14300
            elif tipo == '6':
                precio_inicial = 17900
            monto_final = precio_inicial * recargo

            # print("Tipo de envio: ", tipo)
            # print("Monto: ", monto_final)
            
            importe_acumulado += monto_final

    elif control() == "Hard Control":
        for linea in envios[1:]:
            result = validation(linea)
            if result == True:
                lista_cp = []
                cont_cp = 0
                # print("-----------")
                for letra in linea[:9]:
                    cp = letra
                    lista_cp.append(cp)
                    # print(cp)
                    cont_cp += 1
                cont_cp_final = cont_cp
                # print("letras: ", cont_cp_final)
                # print(lista_cp)
                
                # Determinar país y recargo
                if cont_cp_final == 8 and lista_cp[0] in "abcdefghjklmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ":
                    pais = "Argentina"
                    recargo = 1
                elif cont_cp_final == 4 and lista_cp[0] in "1234567890":
                    pais = "Bolivia"
                    provincia = "No aplica"
                    recargo = 1.2
                elif cont_cp_final == 9 and lista_cp[0] in "1234567890" and lista_cp[5] == "-":
                    pais = "Brasil"
                    if lista_cp[0] in ("0123"):
                        recargo = 1.25
                        provincia = "No aplica"
                    elif lista_cp[0] in ("89"):
                        recargo = 1.2
                        provincia = "No aplica"
                    elif lista_cp[0] in ("4567"):
                        recargo = 1.3
                        provincia = "No aplica"
                elif cont_cp_final == 7 and lista_cp[0] in "1234567890":
                    pais = "Chile"
                    provincia = "No aplica"
                    recargo = 1.25
                elif cont_cp_final == 5 and lista_cp[0] in "1234567890":
                    pais = "Uruguay"
                    if lista_cp[0] == "1":
                        provincia = "No aplica"
                        recargo = 1.2
                    else:
                        provincia = "No aplica"
                        recargo = 1.25
                elif cont_cp_final == 6 and lista_cp[0] in "1234567890":
                    pais = "Paraguay"
                    provincia = "No aplica"
                    recargo = 1.2
                else:
                    pais = "Otro"
                    provincia = "No aplica"
                    recargo = 1.5 

                # Calcular el monto basado en tipo de envio
                tipo = linea[29]
                precio_inicial = 0
                if tipo == '0':
                    precio_inicial = 1100
                elif tipo == '1':
                    precio_inicial = 1800
                elif tipo == '2':
                    precio_inicial = 2450
                elif tipo == '3':
                    precio_inicial = 8300
                elif tipo == '4':
                    precio_inicial = 10900
                elif tipo == '5':
                    precio_inicial = 14300
                elif tipo == '6':
                    precio_inicial = 17900
                monto_final = precio_inicial * recargo

                # print("Tipo de envio: ", tipo)
                # print("Monto: ", monto_final)
                
                importe_acumulado += monto_final


    return importe_acumulado

    # print("Importe acumulado final: ", importe_acumulado)


def tipo_carta():
    carta_simple = 0
    carta_certificada = 0
    carta_expresa = 0
    
    if control() == "Soft Control":
        for linea in envios[1:]:
            tipo = linea[29]
            if tipo == '0' or tipo == '1' or tipo == '2':
                carta_simple += 1                
            elif tipo == '3' or tipo == '4':
                carta_certificada += 1
            elif tipo == '5' or tipo == '6':
                carta_expresa += 1
                
    elif control() == "Hard Control":
        for linea in envios[1:]:
            result = validation(linea)
            if result == True:
                tipo = linea[29]
                if tipo == '0' or tipo == '1' or tipo == '2':
                    carta_simple += 1                
                elif tipo == '3' or tipo == '4':
                    carta_certificada += 1
                elif tipo == '5' or tipo == '6':
                    carta_expresa += 1

    return carta_simple, carta_certificada, carta_expresa

def ccs():
    simple, certificada, expresa = tipo_carta()
    return simple

def ccc():
    simple, certificada, expresa = tipo_carta()
    return certificada

def cce():
    simple, certificada, expresa = tipo_carta()
    return expresa


def tipo_mayor():
    mayor = ccs()
    nombre_mayor = "Carta Simple"
    if ccc() > mayor:
        mayor = ccc()
        nombre_mayor = "Carta Verificada"
    if cce() > mayor:
        mayor = cce()
        nombre_mayor = "Carta Expresa"
    
    return nombre_mayor
    

def primer_cp():
    linea = envios[1]
    code = linea[:9].strip()
    return code


def cant_primer_cp():
    contador = 0
    cp = primer_cp()
    for linea in envios[1:]: 
        # print("chequeado")
        if cp in linea.strip(): 
            contador += 1
    return contador

def menimp():
    menor_importe = None
    cp_menor_importe = None
    
    for linea in envios[1:]:
        cp = linea[:9].strip()
        
        if len(cp) == 9:
            primer_digito = int(cp[0])
            if primer_digito in [0, 1, 2, 3]:
                recargo = 1.25
            elif primer_digito in [8, 9]:
                recargo = 1.2
            elif primer_digito in [4, 5, 6, 7]:
                recargo = 1.3
            
            tipo = int(linea[29]) 
            if tipo == 0:
                precio_inicial = 1100
            elif tipo == 1:
                precio_inicial = 1800
            elif tipo == 2:
                precio_inicial = 2450
            elif tipo == 3:
                precio_inicial = 8300
            elif tipo == 4:
                precio_inicial = 10900
            elif tipo == 5:
                precio_inicial = 14300
            elif tipo == 6:
                precio_inicial = 17900
            monto_final = precio_inicial * recargo
            
            if menor_importe is None or monto_final < menor_importe:
                menor_importe = monto_final
                cp_menor_importe = cp
    
    return menor_importe, cp_menor_importe

menor_importe, cp_menor_importe = menimp()


def porc():
    total = 0
    cont = 0

    for linea in envios[1:]:
        total += 1
        cp = linea[:9].strip()
        if len(cp) != 8:
            cont += 1
    
    if total > 0:
        porce = (cont / total) * 100
    else:
        porce = 0
    
    return porce


def prom():
    importe_envio = 0
    
    for linea in envios[1:]:
        cp = linea[:9].strip()
        
        if len(cp) == 8:
            primer_digito = int(cp[0])
            if primer_digito in [0, 1, 2, 3]:
                recargo = 1.25
            elif primer_digito in [8, 9]:
                recargo = 1.2
            elif primer_digito in [4, 5, 6, 7]:
                recargo = 1.3
            
            tipo = int(linea[29]) 
            if tipo == 0:
                precio_inicial = 1100
            elif tipo == 1:
                precio_inicial = 1800
            elif tipo == 2:
                precio_inicial = 2450
            elif tipo == 3:
                precio_inicial = 8300
            elif tipo == 4:
                precio_inicial = 10900
            elif tipo == 5:
                precio_inicial = 14300
            elif tipo == 6:
                precio_inicial = 17900
            monto_final = precio_inicial * recargo
                
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

print('(r11) - Importe menor pagado por envíos a Brasil:', menor_importe)
print('(r12) - Código postal del envío a Brasil con importe menor:', cp_menor_importe)
print('(r13) - Porcentaje de envios al exterior sobre el total:', porc())

print('(r14) - Importe final promedio de los envios a Buenos Aires:', prom())




