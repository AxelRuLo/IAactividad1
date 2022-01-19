import random
import inicializacion


def podaIncial(listaIndividuos: list, bitsIndividuo, puntosMaximos):
    listaPodados = []
    listaNuevaPoblacion = []
    for index in range(len(listaIndividuos)):
        puntosTotales = 0
        numeroElevacion = bitsIndividuo - 1
        for bit in listaIndividuos[index]:
            if bit == 1:
                puntosTotales += 2 ** numeroElevacion
            numeroElevacion -= 1
        if puntosTotales > puntosMaximos:
            listaPodados.append(index)

    if len(listaPodados) > 0:
        print(f"tiene invalidos {len(listaPodados)}")
        listaNuevaPoblacion = generacionIndividuoValido(
            bitsIndividuo, len(listaPodados), puntosMaximos
        )
        listaPodados.reverse()

        for index in listaPodados:
            listaIndividuos.pop(index)

        if len(listaPodados) > 1:
            listaIndividuos.extend(listaNuevaPoblacion)
        else:
            listaIndividuos.append(listaNuevaPoblacion)
        return listaIndividuos
    else:
        return listaIndividuos


def generacionIndividuoValido(bitsIndividuo, numeroGenerar, puntosMaximos):
    listaIndividuosValidos = []
    if numeroGenerar > 1:
        for i in range(numeroGenerar):
            individuo = inicializacion.generarIndividuo(bitsIndividuo)
            puntosTotales = 0
            numeroElevacion = bitsIndividuo - 1
            for bit in individuo:
                if bit == 1:
                    puntosTotales += 2 ** numeroElevacion
                numeroElevacion -= 1
            if puntosTotales > puntosMaximos:
                # print("individuo no valido")
                individuoValido = generacionIndividuoValido(
                    bitsIndividuo, 1, puntosMaximos
                )
                listaIndividuosValidos.append(individuoValido)
            else:
                listaIndividuosValidos.append(individuo)

        return listaIndividuosValidos.copy()
    else:
        individuo = inicializacion.generarIndividuo(bitsIndividuo)
        puntosTotales = 0
        numeroElevacion = bitsIndividuo - 1
        for bit in individuo:
            if bit == 1:
                puntosTotales += 2 ** numeroElevacion
            numeroElevacion -= 1
        if puntosTotales > puntosMaximos:
            # print("individuo no valido")
            individuoValido = generacionIndividuoValido(bitsIndividuo, 1, puntosMaximos)
            return individuoValido
        else:
            return individuo


def podaFueraLimites(listaIndividuos: list, rangoMaximoX, rangoMinimoX, rangoMaximoY, rangoMinimoY, bitsX,bitsY,resolucionX,resolucionY):
    listaNecesitanPoda = []
    listaIndividuosX ,listaIndividuosY = separarXY(listaIndividuos,bitsX)
    listaFenotipoX = obtencionFenotipo(listaIndividuosX,rangoMinimoX,resolucionX,bitsX)
    listaFenotipoY = obtencionFenotipo(listaIndividuosY,rangoMinimoY,resolucionY,bitsY)

    for index in range(len(listaFenotipoX)):
        if((listaFenotipoX[index]>rangoMaximoX or listaFenotipoX[index]<rangoMinimoX)or (listaFenotipoY[index]<rangoMinimoY or listaFenotipoY[index]>rangoMaximoY)):
            # print("este necesito poda porqeu fenotipo x = ",listaFenotipoX[index]," y fenotiop y = ",listaFenotipoY[index])
            listaNecesitanPoda.append(index)
    
    listaNecesitanPoda.reverse()
    for index in listaNecesitanPoda:
        listaIndividuos.pop(index)

    return listaIndividuos



def separarXY(listaIndividuos:list,bitsX):
    listaIndividuosX = []
    listaIndividuosY = []
    # print(listaIndividuos[0])
    for index in range(len(listaIndividuos)):
        listaIndividuosX.append(listaIndividuos[index][0:bitsX])
        listaIndividuosY.append(listaIndividuos[index][bitsX:len(listaIndividuos)])

    # print(listaIndividuosX[0])
    # print(listaIndividuosY[0])
    
    
    return listaIndividuosX,listaIndividuosY


def obtencionFenotipo(listaIndividuos, rangoMinimo, resolucion, bitsIndividuo):

    listaFenotipo = []
    for individuos in listaIndividuos:
        numeroElevacion = bitsIndividuo - 1
        puntosTotales = 0
        for bit in individuos:
            if bit == 1:
                puntosTotales += 2 ** numeroElevacion
            numeroElevacion -= 1
        fenotipo = (puntosTotales * resolucion) + rangoMinimo
        # print(f"este es el fonotippo de el individuo {individuos}: {fenotipo}")
        listaFenotipo.append(round(fenotipo, 3))
    return listaFenotipo

def podaCandtidad(listaIndividuos:list,poblacionMaximo):
    cantidadIndividuos = len(listaIndividuos)
    cantidadEliminados = cantidadIndividuos - poblacionMaximo
    # print(f"En esta poda se eliminaran {cantidadEliminados}")
    for i in range(cantidadEliminados):
        individuoEliminado = random.choice(listaIndividuos)
        # print(f"se eliminara el individuo {individuoEliminado}")
        listaIndividuos.remove(individuoEliminado)
    return listaIndividuos
