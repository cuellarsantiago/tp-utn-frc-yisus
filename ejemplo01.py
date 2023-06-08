def es_patente(pat):
    if len(pat) >= 7:
        return True
    else:
        return False


def es_chilena(pate):
    if len(pate) <= 6:
        return True
    else:
        return False


carg = cbol = cbra = cpar = cchi = curu = cotr = 0
imp_acu_total = 0
primera = cpp = 0
mayimp = 0
maypat = None
porc = 0
prom = 0
# Variables propias:

# _______________________
fd = "peaje25.txt" # --> se debe retornar a "peajes" para la entrega
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

        elif patente[0] in letras and patente[1] in letras and patente[2] in numeros and patente[3] in numeros and \
                patente[4] in numeros and patente[5] in numeros and patente[6] in numeros: \
                cbol += 1

        elif patente[0] in letras and patente[1] in letras and patente[2] in letras and patente[3] in numeros and \
                patente[4] in letras and patente[5] in numeros and patente[6] in numeros:
            cbra += 1

        elif patente[0] in letras and patente[1] in letras and patente[2] in letras and patente[3] in letras and \
                patente[4] in numeros and patente[5] in numeros and patente[6] in numeros:
            cpar += 1

        elif patente[0] in letras and patente[1] in letras and patente[2] in letras and patente[3] in numeros and \
                patente[4] in numeros and patente[5] in numeros and patente[6] in numeros:
            curu += 1

        else:
            cotr += 1


    if es_chilena(patente):
        if patente[0] in letras and patente[1] in letras and patente[2] in letras and patente[3] in letras and \
                patente[4] in numeros and patente[5] in numeros:
            cchi += 1

        else:
            cotr += 1

    # Siguiente proceso

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