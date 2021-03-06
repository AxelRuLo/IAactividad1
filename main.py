import math
from cruza import cruza
from grafica import crearGraficaDePuntos
import inicializacion
from mutacion import mutacion, remplazarMutados
from poda import obtencionFenotipo, podaFueraLimites, podaMax, podaMin, separarXY
from variados import obtenerAptitud, obtenerDatosGraficaMax, obtenerDatosGraficaMin
#-------------------------------------------------------
# rangoMinimoX = 0
# rangoMinimoY = 0
# rangoMaximoX = 0
# rangoMaximoY = 0
# resolucionX = 0
# resolucionY = 0
# poblacionMaxima = 0
# poblacionInicial = 0
# pmiX = 0
# pmiY = 0
# pmgX = 0
# pmgY = 0
# generaciones = 0
#-------------------------------------------------------
generaciones = 100

rangoMinimoX = 10
rangoMinimoY = 10

rangoMaximoX = 20
rangoMaximoY = 20

resolucionX = 0.1
resolucionY = 0.1
poblacionMaxima = 50
poblacionInicial = 4

pmiX = 0.15
pmiY = 0.15
pmgX = 0.25
pmgY = 0.25

pmiProm = (pmiX + pmiY) /2
pmgProm = (pmgX + pmgY) /2

#-------------------------------------------------------
rangoTotalX = rangoMaximoX - rangoMinimoX
rangoTotalY = rangoMaximoY - rangoMinimoY
puntosNecesariosX =  math.ceil((rangoTotalX / resolucionX) + 1)
puntosNecesariosY =  math.ceil((rangoTotalY / resolucionY) + 1)
#-------------------------------------------------------
listaIndividuos = []
listaMejoresAptitudesGeneracionales = []
listaPeoresAptitudesGeneracionales = []
listaPromedioAptitudesGeneracionales = []
#-------------------------------------------------------
# NECESITAN UNA FUNCION PARA SACAR TODO
bitsIndividuoX = inicializacion.SacarBits(puntosNecesariosX)
bitsIndividuoY = inicializacion.SacarBits(puntosNecesariosY)
bitsTotal = bitsIndividuoX + bitsIndividuoY
#-------------------------------------------------------

# print(bitsIndividuoX,"bits de x")
# print(bitsIndividuoY,"bits de y")
# print(puntosNecesariosX,"puntosNecesariosX ")
# print(puntosNecesariosY ,"puntosNecesariosY ")

def main():
    global listaMejoresAptitudesGeneracionales,listaPromedioAptitudesGeneracionales,listaPeoresAptitudesGeneracionales
    listaMejoresGeneracion = []
    seleccion= 0
    listaIndividuos = inicializacion.generacionIndividuosIniciales(bitsIndividuoX,bitsIndividuoY,poblacionInicial,puntosNecesariosX,puntosNecesariosY)
    print("\n")
    for i in range(generaciones):
        print("\n")
        print(f"GENERACION {i}")
        print(f"individuos de esta generacion   {len(listaIndividuos)}")
        print("\n")

        listaHijos=cruza(listaIndividuos.copy(),bitsTotal)


        indexMutados, hijosMutados = mutacion(listaHijos.copy(),pmiProm,pmgProm)
        listaHijos = remplazarMutados(listaHijos.copy(),indexMutados.copy(),hijosMutados)
        listaIndividuos.extend(listaHijos)
        listaIndividuos=podaFueraLimites(listaIndividuos.copy(),rangoMaximoX,rangoMinimoX,rangoMaximoY,rangoMinimoY,bitsIndividuoX,bitsIndividuoY,resolucionX,resolucionY)

        listaIndividuosX,listaIndividuosY = separarXY(listaIndividuos.copy(),bitsIndividuoX)
        listaFenotiposX = obtencionFenotipo(listaIndividuosX,rangoMinimoX,resolucionX,bitsIndividuoX)
        listaFenotiposY = obtencionFenotipo(listaIndividuosY,rangoMinimoY,resolucionY,bitsIndividuoY)
        listaAptitud = obtenerAptitud(listaFenotiposX,listaFenotiposY)


        

        if(seleccion==0):
            listaIndividuos = podaMax(listaIndividuos.copy(),listaAptitud.copy(),poblacionMaxima)
            mejor,peor,promedio = obtenerDatosGraficaMax(listaAptitud.copy())
            listaMejoresAptitudesGeneracionales.append(mejor)
            listaPeoresAptitudesGeneracionales.append(peor)
            listaPromedioAptitudesGeneracionales.append(promedio)

            listaIndividuosX,listaIndividuosY = separarXY(listaIndividuos.copy(),bitsIndividuoX)
            listaFenotiposX = obtencionFenotipo(listaIndividuosX,rangoMinimoX,resolucionX,bitsIndividuoX)
            listaFenotiposY = obtencionFenotipo(listaIndividuosY,rangoMinimoY,resolucionY,bitsIndividuoY)
            listaAptitud = obtenerAptitud(listaFenotiposX,listaFenotiposY)

            mejorGeneracion = max(listaAptitud)
            indexMejorGeneracin = listaAptitud.index(mejorGeneracion)
            listaMejoresGeneracion.append([listaFenotiposX[indexMejorGeneracin],listaFenotiposY[indexMejorGeneracin]])
        
        else:
            listaIndividuos = podaMin(listaIndividuos.copy(),listaAptitud.copy(),poblacionMaxima)
            mejor,peor,promedio = obtenerDatosGraficaMin(listaAptitud.copy())
            listaMejoresAptitudesGeneracionales.append(mejor)
            listaPeoresAptitudesGeneracionales.append(peor)
            listaPromedioAptitudesGeneracionales.append(promedio)

            listaIndividuosX,listaIndividuosY = separarXY(listaIndividuos.copy(),bitsIndividuoX)
            listaFenotiposX = obtencionFenotipo(listaIndividuosX,rangoMinimoX,resolucionX,bitsIndividuoX)
            listaFenotiposY = obtencionFenotipo(listaIndividuosY,rangoMinimoY,resolucionY,bitsIndividuoY)
            listaAptitud = obtenerAptitud(listaFenotiposX,listaFenotiposY)

            mejorGeneracion = min(listaAptitud)
            indexMejorGeneracin = listaAptitud.index(mejorGeneracion)
            listaMejoresGeneracion.append([listaFenotiposX[indexMejorGeneracin],listaFenotiposY[indexMejorGeneracin]])
        
  
            


        print("FENOTIPOS E INDIVIDUOS")
        for i in range(len(listaFenotiposX)):
            print(f"individuo {listaIndividuos[i]} con fenotipo x = {listaFenotiposX[i]} con fenotipo y {listaFenotiposY[i]} {listaAptitud[i]}")
        
        


    print(f"Mejor aptitud por generaciones {listaMejoresGeneracion}")
    crearGraficaDePuntos(listaMejoresAptitudesGeneracionales,listaPeoresAptitudesGeneracionales,listaPromedioAptitudesGeneracionales)
    pass

if __name__ == "__main__":
    main()