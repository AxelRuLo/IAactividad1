from cgi import print_directory
import math
import statistics
from cruza import cruza
from grafica import crearGraficaDePuntos
import inicializacion
from mutacion import mutacion, remplazarMutados
from poda import obtencionFenotipo, podaCandtidad, podaFueraLimites, podaMax, podaMin, separarXY
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

rangoMinimoX = 3
rangoMinimoY = 50

rangoMaximoX = 15
rangoMaximoY = 85

resolucionX = 0.4
resolucionY = 0.4
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

print(bitsIndividuoX,"bits de x")
print(bitsIndividuoY,"bits de y")
print(puntosNecesariosX,"puntosNecesariosX ")
print(puntosNecesariosY ,"puntosNecesariosY ")

def main():
    global listaMejoresAptitudesGeneracionales,listaPromedioAptitudesGeneracionales,listaPeoresAptitudesGeneracionales
    seleccion= 2
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

        

        if(seleccion==1):
            listaIndividuos = podaMax(listaIndividuos.copy(),listaAptitud.copy(),poblacionMaxima)
            mejor,peor,promedio = obtenerDatosGraficaMax(listaAptitud.copy())
            listaMejoresAptitudesGeneracionales.append(mejor)
            listaPeoresAptitudesGeneracionales.append(peor)
            listaPromedioAptitudesGeneracionales.append(promedio)
        else:
            listaIndividuos = podaMin(listaIndividuos.copy(),listaAptitud.copy(),poblacionMaxima)
            mejor,peor,promedio = obtenerDatosGraficaMin(listaAptitud.copy())
            listaMejoresAptitudesGeneracionales.append(mejor)
            listaPeoresAptitudesGeneracionales.append(peor)
            listaPromedioAptitudesGeneracionales.append(promedio)
        
  

        # print("LISTAS INDIVIDUOS X Y Y")
        # for i in range(len(listaIndividuosX)):
        #     print(" ")
        #     print(listaIndividuos[i]," con fenotipos ",listaFenotiposX[i],"  ",listaFenotiposY[i]," aptitud: ",listaAptitud[i])
        #     print(listaIndividuosX[i])
        #     print(listaIndividuosY[i])


        # print("lista de inidividuos despues poda")
        # for i in listaIndividuos:
        #     print(i)
    
    crearGraficaDePuntos(listaMejoresAptitudesGeneracionales,listaPeoresAptitudesGeneracionales,listaPromedioAptitudesGeneracionales)
    pass

if __name__ == "__main__":
    main()