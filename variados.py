import math
import statistics


def obtenerAptitud(listaFenotiposXlist:list, listaFenotiposYlist:list):
    listaAptitud = []
    for index in range(len(listaFenotiposXlist)):
        x = listaFenotiposXlist[index]
        y = listaFenotiposYlist[index]
        aux= (x**2 + y**2)
        aux2 = math.asin(math.pi/(x+y))
        listaAptitud.append(aux * aux2)
    return listaAptitud

def obtenerDatosGraficaMax(aptitudes):
    mejor= max(aptitudes)
    peor = min(aptitudes)
    promedio = statistics.mean(aptitudes)
    return mejor,peor,promedio

def obtenerDatosGraficaMin(aptitudes):
    mejor= min(aptitudes)
    peor = max(aptitudes)
    promedio = statistics.mean(aptitudes)
    return mejor,peor,promedio