def es_patente(pat):
    if len(pat) >= 7:
        return True
    else:
        return False
def es_importe(cabina):
    if cabina == 0:  # Argentina
        return  300
    elif cabina == 1:  # Bolivia
        return  200
    elif cabina == 2:  # Brasil
        return 400
    elif cabina == 3:  # Paraguay
        return 300
    elif cabina == 4:  # Uruguay
        return 300
    importe_basico = calcular_importe_basico(tipo, importe_base)
def calcular_importe_basico(tipo, importe_base):
    if tipo == 0:  # Motocicleta
        return 0.5 * importe_base
    elif tipo == 2:  # Camión
        return importe_base + 0.6 * importe_base
    else:  # Automóvil
        return importe_base

def calcular_importe_final(pago, importe_basico):
    if pago == 2:  # Telepeaje
        return 0.9 * importe_basico
    else:  # Manual
        return importe_basico
def es_mayor(importe_mayor,pais_patente):
    if importe_final_arg>importe_final_bolivia and importe_final_arg> importe_final_brasil and importe_final_arg>importe_final_uru and importe_final_arg> importe_final_para and importe_final_arg>importe_total_des and importe_final_arg>importe_final_chile:
        return (importe_final_arg,"ARGENTINA")
    elif  importe_final_bolivia > importe_final_arg and importe_final_bolivia> importe_final_brasil and importe_final_bolivia>importe_final_uru and importe_final_bolivia> importe_final_para and importe_final_bolivia>importe_total_des and importe_final_bolivia>importe_final_chile:
        return (importe_final_bolivia,"BOLIVIA")
    elif  importe_final_brasil > importe_final_arg and importe_final_bolivia< importe_final_brasil and importe_final_brasil>importe_final_uru and importe_final_brasil> importe_final_para and importe_final_brasil>importe_total_des and importe_final_brasil>importe_final_chile:
        return (importe_final_brasil,"BRASIL")
    elif  importe_final_uru > importe_final_arg and importe_final_uru> importe_final_brasil and importe_final_brasil<importe_final_uru and importe_final_uru> importe_final_para and importe_final_uru>importe_total_des and importe_final_uru>importe_final_chile:
        return (importe_final_uru,"URUGUAY")
    elif  importe_final_para > importe_final_arg and importe_final_para> importe_final_brasil and importe_final_para>importe_final_uru and importe_final_uru< importe_final_para and importe_final_para>importe_total_des and importe_final_para>importe_final_chile:
        return (importe_final_para,"PARAGUAY")
    elif  importe_final_chile > importe_final_arg and importe_final_chile> importe_final_brasil and importe_final_chile>importe_final_uru and importe_final_chile> importe_final_para and importe_final_chile>importe_total_des and importe_final_para<importe_final_chile:
        return (importe_final_chile,"CHILE")
    else:
        return (importe_total_des,"DESCONOCIDA")



# Código anterior...

importe_base = 0


def es_chilena(pate):
    if len(pate) <= 6:
        return True
    else:
        return False


carg = cbol = cbra = cpar = cchi = curu = cotr = 0

primera = cpp = 0
mayimp = 0
maypat = None
porc = 0
prom = 0
importe_basico=0
importe_final_arg =importe_final_bolivia =importe_final_brasil =importe_final_para \
    =importe_final_uru =importe_final_desconocida_patente=importe_final_dec2=importe_final_chile=0
# Variables propias:

# _______________________
fd = "peaje100.txt" # --> se debe retornar a "peajes" para la entrega
m = open(fd)
line = m.readline()
idioma = "Español"
if "PT" in line:
    idioma = "Portugués"

while True:
    line = m.readline()
    if line == "":
        break

    # datos de cada línea...
    patente = line[0:7].lstrip()
    tipo = int(line[7])
    pago = int(line[8])
    cabina = int(line[9])
    distancia = int(line[10:13])

    # Patentes
    numeros = "1234567890"
    letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÉ"

    if es_patente(patente):
        if patente[0] in letras and patente[1] in letras and patente[2] in numeros and patente[3] in numeros and \
                patente[4] in numeros and patente[5] in letras and patente[6] in letras:
            carg += 1

            importe_base=es_importe(cabina)

            importe_basico = calcular_importe_basico(tipo, importe_base)

            # Calcula el importe final
            importe_final_arg = calcular_importe_final(pago, importe_basico)



        elif patente[0] in letras and patente[1] in letras and patente[2] in numeros and patente[3] in numeros and \
                patente[4] in numeros and patente[5] in numeros and patente[6] in numeros:
                cbol += 1
                importe_base = es_importe(cabina)

                importe_basico = calcular_importe_basico(tipo, importe_base)

                # Calcula el importe final
                importe_final_bolivia = calcular_importe_final(pago, importe_basico)

        elif patente[0] in letras and patente[1] in letras and patente[2] in letras and patente[3] in numeros and \
                patente[4] in letras and patente[5] in numeros and patente[6] in numeros:
            cbra += 1
            importe_base = es_importe(cabina)

            importe_basico = calcular_importe_basico(tipo, importe_base)

            # Calcula el importe final
            importe_final_brasil = calcular_importe_final(pago, importe_basico)

        elif patente[0] in letras and patente[1] in letras and patente[2] in letras and patente[3] in letras and \
                patente[4] in numeros and patente[5] in numeros and patente[6] in numeros:
            cpar += 1
            importe_base = es_importe(cabina)

            importe_basico = calcular_importe_basico(tipo, importe_base)

            # Calcula el importe final
            importe_final_para = calcular_importe_final(pago, importe_basico)

        elif patente[0] in letras and patente[1] in letras and patente[2] in letras and patente[3] in numeros and \
                patente[4] in numeros and patente[5] in numeros and patente[6] in numeros:
            curu += 1
            importe_base = es_importe(cabina)

            importe_basico = calcular_importe_basico(tipo, importe_base)

            # Calcula el importe final
            importe_final_uru = calcular_importe_final(pago, importe_basico)

        else:
            cotr += 1
            importe_base = es_importe(cabina)

            importe_basico = calcular_importe_basico(tipo, importe_base)

            # Calcula el importe final
            importe_final_desconocida_patente = calcular_importe_final(pago, importe_basico)


    if es_chilena(patente):
        if patente[0] in letras and patente[1] in letras and patente[2] in letras and patente[3] in letras and \
                patente[4] in numeros and patente[5] in numeros:
            cchi += 1
            importe_base = es_importe(cabina)

            importe_basico = calcular_importe_basico(tipo, importe_base)

            # Calcula el importe final
            importe_final_chile = calcular_importe_final(pago, importe_basico)

        else:
            cotr += 1
            importe_base = es_importe(cabina)

            importe_basico = calcular_importe_basico(tipo, importe_base)

            # Calcula el importe final
            importe_final_dec2 = calcular_importe_final(pago, importe_basico)

importe_total_des=importe_final_desconocida_patente+importe_final_dec2
    # Siguiente proceso
mayimp,maypat=es_mayor(mayimp,maypat)
imp_acu_total=importe_final_arg +importe_final_bolivia +importe_final_brasil +importe_final_para \
    +importe_final_uru +importe_final_desconocida_patente+importe_final_dec2+importe_final_chile

# No toquen esto! todos los procesos que quieran hacer se hacen arriba de esta ternurita o el programa se clava.
m.close()

# Visualización de resultados...
print('(r1) - Idioma a usar en los informes:', idioma)

print()
print('(r2) - Cantidad de patentes de Argentina:', carg)
print('(r2) - Cantidad de patentes de Bolivia:', cbol)
print('(r2) - Cantidad de patentes de Brasil:', cbra)
print('(r2) - Cantidad de patentes de Chile:', cchi)
print('(r2) - Cantidad de patentes de Paraguay:', cpar)
print('(r2) - Cantidad de patentes de Uruguay:', curu)
print('(r2) - Cantidad de patentes de otro país:', cotr)

print()
print('(r3) - Importe acumulado total de importes finales:', imp_acu_total)

print()
print('(r4) - Primera patente del archivo:', primera, '- Frecuencia de aparición:', cpp)

print()
print('(r5) - Mayor importe final cobrado:', mayimp, '- Patente a la que se cobró ese importe:', maypat)

print()
print('(r6) - Porcentaje de patentes de otros países:', porc, '\b%')

print()
print('(r7) - Distancia promedio recorrida por vehículos argentinos pasando por cabinas brasileñas:', prom, '\bkm')
