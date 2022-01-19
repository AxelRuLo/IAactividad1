import random

def cruza(listaIndividuos,totalBits):
    listaHijos = []
    numeroIndividuos = range(len(listaIndividuos))
    listaIndividuosPorCruzar = list(numeroIndividuos)
    listaIndividuosPorCruzarAuxiliar = list(numeroIndividuos)
    listaParejas = []

    # se elije a quienes  se cruzaran
    while len(listaIndividuosPorCruzar) > 0:
        tuplaPareja = []
        numeroRandom1 = random.choice(listaIndividuosPorCruzar)
        listaIndividuosPorCruzar.remove(numeroRandom1)
        if len(listaIndividuosPorCruzar) == 0:
            numeroRandom2 = random.choice(listaIndividuosPorCruzarAuxiliar)
        else:
            numeroRandom2 = random.choice(listaIndividuosPorCruzar)
        tuplaPareja.append([numeroRandom1, numeroRandom2])
        listaParejas.append(tuplaPareja)
        
        # se estan empezanod a cruzar
    for parejas in listaParejas:
        # print(parejas)
        seleccionCruza = [random.randint(0, totalBits-1),random.randint(0, totalBits-1),random.randint(0, totalBits-1)]
        seleccionCruza.sort()
        seleccionCruza1 = seleccionCruza[0]
        seleccionCruza2 = seleccionCruza[1]
        seleccionCruza3 = seleccionCruza[2]
        
            
        padre = listaIndividuos[parejas[0][0]]
        madre = listaIndividuos[parejas[0][1]]
        hijo1, hijo2 = generarCruza(seleccionCruza1,seleccionCruza2,seleccionCruza3, padre, madre)
        listaHijos.append(hijo1)
        listaHijos.append(hijo2)

    return listaHijos

def generarCruza(corte1,corte2,corte3,padre,madre):
    hijo1 = []
    hijo2 = []
    for index in range(len(padre)):
        if index < corte1:
            hijo1.append(padre[index])
            hijo2.append(madre[index])
        elif(index>corte1 and index < corte2):
            hijo1.append(madre[index])
            hijo2.append(padre[index])
        elif(index>corte2) and index<corte3:
            hijo1.append(padre[index])
            hijo2.append(madre[index])
        else:
            hijo1.append(madre[index])
            hijo2.append(padre[index])


    return hijo1, hijo2
