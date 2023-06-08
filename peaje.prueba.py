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
importe_total_chile = importe_total_bolivia =importe_total_otro2 = importe_total_brasil = importe_arg = importe_total_otra_patente = importe_total_paraguay = importe_total_uru = 0
primera = cpp = 0
mayimp = 0
importe_mayor = 0
porc = 0
prom = 0
importe_total_patente_desconocidas=0

importe_camion=importe_camion_tele=importe_auto=importe_auto_tele=importe_moto=importe_moto_tele=0
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
            if tipo==0 and pago==1 and (cabina==0 or cabina==3 or cabina==4):
                importe_moto+=(300*0.50)
            elif tipo==0 and pago==2 and (cabina==0 or cabina==3 or cabina==4):
                importe_moto_tele+=(300*0.50)-(300*0.10)
            elif tipo == 1 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_auto+=300
            elif tipo == 1 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_auto_tele+=300-(300*0.10)
            elif tipo==2 and pago==1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_camion+=300+(300*0.60)
            elif tipo == 2 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_camion_tele+=300+(300*0.60)-(300*0.10)
        #brasil
            elif tipo==0 and pago==1 and cabina==2:
                importe_moto+=(400*0.50)
            elif tipo==0 and pago==2 and cabina==2:
                importe_moto_tele+=(400*0.50)-(400*0.10)
            elif tipo == 1 and pago == 1 and cabina == 2:
                importe_auto+=400
            elif tipo == 1 and pago == 2 and cabina == 2:
                importe_auto_tele+=400-(400*0.10)
            elif tipo==2 and pago==1 and cabina==2:
                importe_camion+=400+(400*0.60)
            elif tipo == 2 and pago == 2 and cabina==2:
                importe_camion_tele+=400+(400*0.60)-(400*0.10)
        #bolivia
            elif tipo==0 and pago==1 and cabina==1:
                importe_moto+=(200*0.50)
            elif tipo==0 and pago==2 and cabina==1:
                importe_moto_tele+=(200*0.50)-(200*0.10)
            elif tipo == 1 and pago == 1 and cabina == 1:
                importe_auto+=200
            elif tipo == 1 and pago == 2 and cabina == 1:
                importe_auto_tele+=200-(200*0.10)
            elif tipo==2 and pago==1 and cabina == 1 :
                importe_camion+=200+(200*0.60)
            elif tipo == 2 and pago == 2 and cabina == 1 :
                importe_camion_tele+=200+(200*0.60)-(200*0.10)
            importe_arg=importe_moto+importe_moto_tele+importe_auto+importe_auto_tele+importe_camion+importe_camion_tele





        elif patente[0] in letras and patente[1] in letras and patente[2] in numeros and patente[3] in numeros and \
                patente[4] in numeros and patente[5] in numeros and patente[6] in numeros:
                cbol += 1
                if tipo == 0 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                    importe_moto += (300 * 0.50)
                elif tipo == 0 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                    importe_moto_tele += (300 * 0.50) - (300 * 0.10)
                elif tipo == 1 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                    importe_auto += 300
                elif tipo == 1 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                    importe_auto_tele += 300 - (300 * 0.10)
                elif tipo == 2 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                    importe_camion += 300 + (300 * 0.60)
                elif tipo == 2 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                    importe_camion_tele += 300 + (300 * 0.60) - (300 * 0.10)
                # brasil
                elif tipo == 0 and pago == 1 and cabina == 2:
                    importe_moto += (400 * 0.50)
                elif tipo == 0 and pago == 2 and cabina == 2:
                    importe_moto_tele += (400 * 0.50) - (400 * 0.10)
                elif tipo == 1 and pago == 1 and cabina == 2:
                    importe_auto += 400
                elif tipo == 1 and pago == 2 and cabina == 2:
                    importe_auto_tele += 400 - (400 * 0.10)
                elif tipo == 2 and pago == 1 and cabina == 2:
                    importe_camion += 400 + (400 * 0.60)
                elif tipo == 2 and pago == 2 and cabina == 2:
                    importe_camion_tele += 400 + (400 * 0.60) - (400 * 0.10)
                # bolivia
                elif tipo == 0 and pago == 1 and cabina == 1:
                    importe_moto += (200 * 0.50)
                elif tipo == 0 and pago == 2 and cabina == 1:
                    importe_moto_tele += (200 * 0.50) - (200 * 0.10)
                elif tipo == 1 and pago == 1 and cabina == 1:
                    importe_auto += 200
                elif tipo == 1 and pago == 2 and cabina == 1:
                    importe_auto_tele += 200 - (200 * 0.10)
                elif tipo == 2 and pago == 1 and cabina == 1:
                    importe_camion += 200 + (200 * 0.60)
                elif tipo == 2 and pago == 2 and cabina == 1:
                    importe_camion_tele += 200 + (200 * 0.60) - (200 * 0.10)
                importe_total_bolivia=importe_auto+importe_auto_tele+importe_camion+importe_camion_tele+importe_moto_tele+importe_moto

        elif patente[0] in letras and patente[1] in letras and patente[2] in letras and patente[3] in numeros and \
                patente[4] in letras and patente[5] in numeros and patente[6] in numeros:
            cbra += 1
            if tipo == 0 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_moto += (300 * 0.50)
            elif tipo == 0 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_moto_tele += (300 * 0.50) - (300 * 0.10)
            elif tipo == 1 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_auto += 300
            elif tipo == 1 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_auto_tele += 300 - (300 * 0.10)
            elif tipo == 2 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_camion += 300 + (300 * 0.60)
            elif tipo == 2 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_camion_tele += 300 + (300 * 0.60) - (300 * 0.10)
            # brasil
            elif tipo == 0 and pago == 1 and cabina == 2:
                importe_moto += (400 * 0.50)
            elif tipo == 0 and pago == 2 and cabina == 2:
                importe_moto_tele += (400 * 0.50) - (400 * 0.10)
            elif tipo == 1 and pago == 1 and cabina == 2:
                importe_auto += 400
            elif tipo == 1 and pago == 2 and cabina == 2:
                importe_auto_tele += 400 - (400 * 0.10)
            elif tipo == 2 and pago == 1 and cabina == 2:
                importe_camion += 400 + (400 * 0.60)
            elif tipo == 2 and pago == 2 and cabina == 2:
                importe_camion_tele += 400 + (400 * 0.60) - (400 * 0.10)
            # bolivia
            elif tipo == 0 and pago == 1 and cabina == 1:
                importe_moto += (200 * 0.50)
            elif tipo == 0 and pago == 2 and cabina == 1:
                importe_moto_tele += (200 * 0.50) - (200 * 0.10)
            elif tipo == 1 and pago == 1 and cabina == 1:
                importe_auto += 200
            elif tipo == 1 and pago == 2 and cabina == 1:
                importe_auto_tele += 200 - (200 * 0.10)
            elif tipo == 2 and pago == 1 and cabina == 1:
                importe_camion += 200 + (200 * 0.60)
            elif tipo == 2 and pago == 2 and cabina == 1:
                importe_camion_tele += 200 + (200 * 0.60) - (200 * 0.10)
            importe_total_brasil=importe_moto+importe_moto_tele+importe_auto+importe_auto_tele+importe_camion+importe_camion_tele

        elif patente[0] in letras and patente[1] in letras and patente[2] in letras and patente[3] in letras and \
                patente[4] in numeros and patente[5] in numeros and patente[6] in numeros:
            cpar += 1
            if tipo == 0 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_moto += (300 * 0.50)
            elif tipo == 0 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_moto_tele += (300 * 0.50) - (300 * 0.10)
            elif tipo == 1 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_auto += 300
            elif tipo == 1 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_auto_tele += 300 - (300 * 0.10)
            elif tipo == 2 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_camion += 300 + (300 * 0.60)
            elif tipo == 2 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_camion_tele += 300 + (300 * 0.60) - (300 * 0.10)
            # brasil
            elif tipo == 0 and pago == 1 and cabina == 2:
                importe_moto += (400 * 0.50)
            elif tipo == 0 and pago == 2 and cabina == 2:
                importe_moto_tele += (400 * 0.50) - (400 * 0.10)
            elif tipo == 1 and pago == 1 and cabina == 2:
                importe_auto += 400
            elif tipo == 1 and pago == 2 and cabina == 2:
                importe_auto_tele += 400 - (400 * 0.10)
            elif tipo == 2 and pago == 1 and cabina == 2:
                importe_camion += 400 + (400 * 0.60)
            elif tipo == 2 and pago == 2 and cabina == 2:
                importe_camion_tele += 400 + (400 * 0.60) - (400 * 0.10)
            # bolivia
            elif tipo == 0 and pago == 1 and cabina == 1:
                importe_moto += (200 * 0.50)
            elif tipo == 0 and pago == 2 and cabina == 1:
                importe_moto_tele += (200 * 0.50) - (200 * 0.10)
            elif tipo == 1 and pago == 1 and cabina == 1:
                importe_auto += 200
            elif tipo == 1 and pago == 2 and cabina == 1:
                importe_auto_tele += 200 - (200 * 0.10)
            elif tipo == 2 and pago == 1 and cabina == 1:
                importe_camion += 200 + (200 * 0.60)
            elif tipo == 2 and pago == 2 and cabina == 1:
                importe_camion_tele += 200 + (200 * 0.60) - (200 * 0.10)
            importe_total_paraguay=importe_moto+importe_moto_tele+importe_auto+importe_auto_tele+importe_camion+importe_camion_tele

        elif patente[0] in letras and patente[1] in letras and patente[2] in letras and patente[3] in numeros and \
                patente[4] in numeros and patente[5] in numeros and patente[6] in numeros:
            curu += 1
            if tipo == 0 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_moto += (300 * 0.50)
            elif tipo == 0 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_moto_tele += (300 * 0.50) - (300 * 0.10)
            elif tipo == 1 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_auto += 300
            elif tipo == 1 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_auto_tele += 300 - (300 * 0.10)
            elif tipo == 2 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_camion += 300 + (300 * 0.60)
            elif tipo == 2 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_camion_tele += 300 + (300 * 0.60) - (300 * 0.10)
            # brasil
            elif tipo == 0 and pago == 1 and cabina == 2:
                importe_moto += (400 * 0.50)
            elif tipo == 0 and pago == 2 and cabina == 2:
                importe_moto_tele += (400 * 0.50) - (400 * 0.10)
            elif tipo == 1 and pago == 1 and cabina == 2:
                importe_auto += 400
            elif tipo == 1 and pago == 2 and cabina == 2:
                importe_auto_tele += 400 - (400 * 0.10)
            elif tipo == 2 and pago == 1 and cabina == 2:
                importe_camion += 400 + (400 * 0.60)
            elif tipo == 2 and pago == 2 and cabina == 2:
                importe_camion_tele += 400 + (400 * 0.60) - (400 * 0.10)
            # bolivia
            elif tipo == 0 and pago == 1 and cabina == 1:
                importe_moto += (200 * 0.50)
            elif tipo == 0 and pago == 2 and cabina == 1:
                importe_moto_tele += (200 * 0.50) - (200 * 0.10)
            elif tipo == 1 and pago == 1 and cabina == 1:
                importe_auto += 200
            elif tipo == 1 and pago == 2 and cabina == 1:
                importe_auto_tele += 200 - (200 * 0.10)
            elif tipo == 2 and pago == 1 and cabina == 1:
                importe_camion += 200 + (200 * 0.60)
            elif tipo == 2 and pago == 2 and cabina == 1:
                importe_camion_tele += 200 + (200 * 0.60) - (200 * 0.10)
            importe_total_uru=importe_moto+importe_moto_tele+importe_auto+importe_auto_tele+importe_camion+importe_camion_tele

        else:
            cotr += 1
            if tipo == 0 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_moto += (300 * 0.50)
            elif tipo == 0 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_moto_tele += (300 * 0.50) - (300 * 0.10)
            elif tipo == 1 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_auto += 300
            elif tipo == 1 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_auto_tele += 300 - (300 * 0.10)
            elif tipo == 2 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_camion += 300 + (300 * 0.60)
            elif tipo == 2 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_camion_tele += 300 + (300 * 0.60) - (300 * 0.10)
            # brasil
            elif tipo == 0 and pago == 1 and cabina == 2:
                importe_moto += (400 * 0.50)
            elif tipo == 0 and pago == 2 and cabina == 2:
                importe_moto_tele += (400 * 0.50) - (400 * 0.10)
            elif tipo == 1 and pago == 1 and cabina == 2:
                importe_auto += 400
            elif tipo == 1 and pago == 2 and cabina == 2:
                importe_auto_tele += 400 - (400 * 0.10)
            elif tipo == 2 and pago == 1 and cabina == 2:
                importe_camion += 400 + (400 * 0.60)
            elif tipo == 2 and pago == 2 and cabina == 2:
                importe_camion_tele += 400 + (400 * 0.60) - (400 * 0.10)
            # bolivia
            elif tipo == 0 and pago == 1 and cabina == 1:
                importe_moto += (200 * 0.50)
            elif tipo == 0 and pago == 2 and cabina == 1:
                importe_moto_tele += (200 * 0.50) - (200 * 0.10)
            elif tipo == 1 and pago == 1 and cabina == 1:
                importe_auto += 200
            elif tipo == 1 and pago == 2 and cabina == 1:
                importe_auto_tele += 200 - (200 * 0.10)
            elif tipo == 2 and pago == 1 and cabina == 1:
                importe_camion += 200 + (200 * 0.60)
            elif tipo == 2 and pago == 2 and cabina == 1:
                importe_camion_tele += 200 + (200 * 0.60) - (200 * 0.10)
            print("cantidad",cotr)
            importe_total_otra_patente=importe_moto+importe_moto_tele+importe_auto+importe_auto_tele+importe_camion+importe_camion_tele


    if es_chilena(patente):
        if patente[0] in letras and patente[1] in letras and patente[2] in letras and patente[3] in letras and \
                patente[4] in numeros and patente[5] in numeros:
            cchi += 1
            if tipo == 0 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_moto += (300 * 0.50)
            elif tipo == 0 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_moto_tele += (300 * 0.50) - (300 * 0.10)
            elif tipo == 1 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_auto += 300
            elif tipo == 1 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_auto_tele += 300 - (300 * 0.10)
            elif tipo == 2 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_camion += 300 + (300 * 0.60)
            elif tipo == 2 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_camion_tele += 300 + (300 * 0.60) - (300 * 0.10)
            # brasil
            elif tipo == 0 and pago == 1 and cabina == 2:
                importe_moto += (400 * 0.50)
            elif tipo == 0 and pago == 2 and cabina == 2:
                importe_moto_tele += (400 * 0.50) - (400 * 0.10)
            elif tipo == 1 and pago == 1 and cabina == 2:
                importe_auto += 400
            elif tipo == 1 and pago == 2 and cabina == 2:
                importe_auto_tele += 400 - (400 * 0.10)
            elif tipo == 2 and pago == 1 and cabina == 2:
                importe_camion += 400 + (400 * 0.60)
            elif tipo == 2 and pago == 2 and cabina == 2:
                importe_camion_tele += 400 + (400 * 0.60) - (400 * 0.10)
            # bolivia
            elif tipo == 0 and pago == 1 and cabina == 1:
                importe_moto += (200 * 0.50)
            elif tipo == 0 and pago == 2 and cabina == 1:
                importe_moto_tele += (200 * 0.50) - (200 * 0.10)
            elif tipo == 1 and pago == 1 and cabina == 1:
                importe_auto += 200
            elif tipo == 1 and pago == 2 and cabina == 1:
                importe_auto_tele += 200 - (200 * 0.10)
            elif tipo == 2 and pago == 1 and cabina == 1:
                importe_camion += 200 + (200 * 0.60)
            elif tipo == 2 and pago == 2 and cabina == 1:
                importe_camion_tele += 200 + (200 * 0.60) - (200 * 0.10)
            importe_total_chile=importe_moto+importe_moto_tele+importe_auto+importe_auto_tele+importe_camion+importe_camion_tele

        else:
            cotr += 1
            if tipo == 0 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_moto += (300 * 0.50)
            elif tipo == 0 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_moto_tele += (300 * 0.50) - (300 * 0.10)
            elif tipo == 1 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_auto += 300
            elif tipo == 1 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_auto_tele += 300 - (300 * 0.10)
            elif tipo == 2 and pago == 1 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_camion += 300 + (300 * 0.60)
            elif tipo == 2 and pago == 2 and (cabina == 0 or cabina == 3 or cabina == 4):
                importe_camion_tele += 300 + (300 * 0.60) - (300 * 0.10)
            # brasil
            elif tipo == 0 and pago == 1 and cabina == 2:
                importe_moto += (400 * 0.50)
            elif tipo == 0 and pago == 2 and cabina == 2:
                importe_moto_tele += (400 * 0.50) - (400 * 0.10)
            elif tipo == 1 and pago == 1 and cabina == 2:
                importe_auto += 400
            elif tipo == 1 and pago == 2 and cabina == 2:
                importe_auto_tele += 400 - (400 * 0.10)
            elif tipo == 2 and pago == 1 and cabina == 2:
                importe_camion += 400 + (400 * 0.60)
            elif tipo == 2 and pago == 2 and cabina == 2:
                importe_camion_tele += 400 + (400 * 0.60) - (400 * 0.10)
            # bolivia
            elif tipo == 0 and pago == 1 and cabina == 1:
                importe_moto += (200 * 0.50)
            elif tipo == 0 and pago == 2 and cabina == 1:
                importe_moto_tele += (200 * 0.50) - (200 * 0.10)
            elif tipo == 1 and pago == 1 and cabina == 1:
                importe_auto += 200
            elif tipo == 1 and pago == 2 and cabina == 1:
                importe_auto_tele += 200 - (200 * 0.10)
            elif tipo == 2 and pago == 1 and cabina == 1:
                importe_camion += 200 + (200 * 0.60)
            elif tipo == 2 and pago == 2 and cabina == 1:
                importe_camion_tele += 200 + (200 * 0.60) - (200 * 0.10)
            importe_total_otro2=importe_camion+importe_camion_tele+importe_moto_tele+importe_auto+importe_auto_tele+importe_moto
    importe_total_patente_desconocidas=importe_total_otra_patente+importe_total_otro2
imp_acu_total =importe_total_chile+importe_total_bolivia+importe_total_otro2+importe_total_brasil+importe_arg+importe_total_otra_patente+importe_total_paraguay+importe_total_uru
if importe_arg>importe_total_bolivia and importe_arg>importe_total_uru and importe_arg> importe_total_paraguay and importe_arg>importe_total_brasil and importe_arg>importe_total_chile and importe_arg> importe_total_patente_desconocidas:
   importe_mayor=importe_arg
   mayimp="ARGENTINA"
elif importe_total_bolivia>  importe_arg  and importe_total_bolivia > importe_total_uru and importe_total_bolivia > importe_total_paraguay and importe_total_bolivia > importe_total_brasil and importe_total_bolivia > importe_total_chile and importe_total_bolivia > importe_total_patente_desconocidas:
    importe_mayor=importe_total_bolivia
    mayimp="BOLIVIA"
elif importe_total_brasil > importe_total_bolivia and importe_total_brasil > importe_total_uru and importe_total_brasil > importe_total_paraguay and importe_arg < importe_total_brasil and importe_total_brasil > importe_total_chile and importe_total_brasil > importe_total_patente_desconocidas:
    importe_mayor=importe_total_brasil
    mayimp="BRASIL"
elif importe_total_chile > importe_arg and importe_total_chile  > importe_total_uru and importe_total_chile  > importe_total_paraguay and importe_total_chile  > importe_total_brasil and importe_total_bolivia < importe_total_chile and importe_total_chile  > importe_total_patente_desconocidas:
    importe_mayor=importe_total_chile
    mayimp="CHILE"
elif importe_total_uru > importe_arg and importe_total_bolivia < importe_total_uru and importe_total_uru > importe_total_paraguay and importe_total_uru > importe_total_brasil and importe_total_uru > importe_total_chile and importe_total_uru > importe_total_patente_desconocidas:
    importe_mayor=importe_total_uru
    mayimp="URUGUAY"
elif importe_total_patente_desconocidas > importe_arg and importe_total_patente_desconocidas > importe_total_uru and importe_total_patente_desconocidas > importe_total_paraguay and importe_total_patente_desconocidas > importe_total_brasil and importe_total_patente_desconocidas > importe_total_chile and importe_total_uru < importe_total_patente_desconocidas :
    importe_mayor=importe_total_otra_patente
    mayimp="PATENTE DESCONOCIDA"
patente2=importe_total_otra_patente
patente3=importe_total_otro2









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
print('(r5) - Mayor importe final cobrado:',importe_mayor , '- Patente a la que se cobró ese importe:', mayimp)

print()
print('(r6) - Porcentaje de patentes de otros países:', porc, '\b%')

print()
print('(r7) - Distancia promedio recorrida por vehículos argentinos pasando por cabinas brasileñas:', prom, '\bkm')
print(patente2)
print(patente3)
print(cotr)
