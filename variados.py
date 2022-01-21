import math
import statistics

# neceisita refactor
def obtenerAptitud(listaFenotiposXlist:list, listaFenotiposYlist:list):
    listaAptitud = []
    print(f"este es el tamaño de x {len(listaFenotiposXlist)} y {len(listaFenotiposYlist)}")

    for index in range(len(listaFenotiposXlist)):
        x = listaFenotiposXlist[index]
        y = listaFenotiposYlist[index]
        # ///////////////////////
        aux= (x**2 + y**2)
        print(f"fenotipo x {x} fenotipo y {y} {x+y} index {index}")
        # aux2 = math.asin(math.pi/(x+y))
        aux2 = math.asin(x+y)
        aux3 = aux * aux2
        listaAptitud.append(aux3)

        # ///////////////////////
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