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

