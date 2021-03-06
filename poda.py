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
        fenotipoX = listaFenotipoX[index]
        fenotipoY = listaFenotipoY[index]
        suma = fenotipoX + fenotipoY
        if((fenotipoX>rangoMaximoX or fenotipoX<rangoMinimoX)or (fenotipoY<rangoMinimoY or fenotipoY>rangoMaximoY)):
            listaNecesitanPoda.append(index)
        else:
            if(suma>1 or suma<-1):
                listaNecesitanPoda.append(index)
            else:
                print("no necistio poda fenotipo x = ",listaFenotipoX[index]," y fenotiop y = ",listaFenotipoY[index],"total",{fenotipoX+fenotipoY})
    

    listaNecesitanPoda.reverse()

    for index in listaNecesitanPoda:
        listaFenotipoX.pop(index)
        listaFenotipoY.pop(index)
        listaIndividuos.pop(index)

    print("\n ESTOS SON LOS INDIVIDUOS QUE MANDAMOS DESPUES DE LA PODA")
    for i in range(len(listaIndividuos)):
        print(f"fenotipo x {listaFenotipoX[i]} fenotipo y {listaFenotipoY[i]} individuo {listaIndividuos[i]}")


    return listaIndividuos,listaFenotipoX,listaFenotipoY

def podaNoValidos(listaIndividuos:list,listaIndexInvalidos):
    pass

def separarXY(listaIndividuos:list,bitsX):
    listaIndividuosX = []
    listaIndividuosY = []
    # print(listaIndividuos[0])
    for index in range(len(listaIndividuos)):
        listaIndividuosX.append(listaIndividuos[index][0:bitsX])
        listaIndividuosY.append(listaIndividuos[index][bitsX:len(listaIndividuos)])
    
    return listaIndividuosX,listaIndividuosY

def podaMax(listaIndividuos,listaAptitud,poblacionMaxima,fenotiposX,fenotiposY):

    listaFenotipoX =[]
    listaFenotipoY =[]
    listaMejoresIndividuosIndex = []
    listaMejoresIndividuos = []
    if(len(listaAptitud)<= poblacionMaxima):
        return listaIndividuos,fenotiposX,fenotiposY
    else:
        for index in range(poblacionMaxima):
            valorMaximo = max(listaAptitud)
            indeiceMaximo = listaAptitud.index(valorMaximo)
            listaMejoresIndividuosIndex.append(indeiceMaximo)
            listaMejoresIndividuos.append(listaIndividuos[indeiceMaximo])
            listaFenotipoX.append(fenotiposX[indeiceMaximo])
            listaFenotipoY.append(fenotiposY[indeiceMaximo])
            listaAptitud.pop(indeiceMaximo)


    return listaMejoresIndividuos,listaFenotipoX,listaFenotipoY

def podaMin(listaIndividuos,listaAptitud,poblacionMaxima,fenotiposX,fenotiposY):

    listaFenotipoX =[]
    listaFenotipoY =[]
    listaMejoresIndividuos = []
    if(len(listaAptitud)<= poblacionMaxima):
        return listaIndividuos,fenotiposX,fenotiposY
    else:
        for index in range(poblacionMaxima):
            valorMaximo = min(listaAptitud)
            indeiceMaximo = listaAptitud.index(valorMaximo)
            listaMejoresIndividuos.append(listaIndividuos[indeiceMaximo])
            listaFenotipoX.append(fenotiposX[indeiceMaximo])
            listaFenotipoY.append(fenotiposY[indeiceMaximo])
            listaAptitud.pop(indeiceMaximo)


    return listaMejoresIndividuos,listaFenotipoX,listaFenotipoY

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
        listaFenotipo.append(fenotipo)
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
