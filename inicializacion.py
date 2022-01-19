import random
import poda

def _generacionIndividuosInicialesX(bitsIndividuo):
    
    pass

def _generacionIndividuosInicialesY(bitsIndividuo):
    
    pass

def generacionIndividuosIniciales(bitsIndividuoX,bitsIndividuoY,poblacionInicial,puntosMaximosX,puntosMaximosY):
    listaInicialesX = []
    listaInicialesY = []
    listaIndividuosIniciales = []
    for i in range(poblacionInicial):
        # mienntras no te genere un valido no lo juntes
        individuoenX = generarIndividuo(bitsIndividuoX)
        individuoenY = generarIndividuo(bitsIndividuoY)
        listaInicialesX.append(individuoenX)
        listaInicialesY.append(individuoenY)
        

    
    listaInicialesY = poda.podaIncial(listaInicialesY.copy(),bitsIndividuoY,puntosMaximosY)
    listaInicialesX = poda.podaIncial(listaInicialesX.copy(),bitsIndividuoX,puntosMaximosX)

    listaFenotipoX = poda.obtencionFenotipo(listaInicialesX,3,0.4,5)
    listaFenotipoY = poda.obtencionFenotipo(listaInicialesY,15,0.4,7)

    print("ESTOS SON LOS FENOTIPOS INICIALES")
    for i in range(len(listaFenotipoX)):
        print(f"{listaFenotipoX[i]}  {listaFenotipoY[i]}")
    # print("este es la longitud de x",listaInicialesX)
    # print("este es la longitud de X",listaInicialesX)
    for i in range(len(listaInicialesX)):
        individuo = listaInicialesX[i] + listaInicialesY[i]
        listaIndividuosIniciales.append(individuo)

    return listaIndividuosIniciales

def generarIndividuo(tamaño: int):
    individuo = []
    for i in range(tamaño):
        individuo.append(round(random.uniform(0,1)))
    return individuo

def SacarBits(puntosNecesarios):
    contador = 0
    while True:
        contador += 1
        if puntosNecesarios <= 2 ** contador:
            return contador

