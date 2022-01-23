from cProfile import label
import matplotlib.pyplot as plt

from variados import obtenerAptitud


def crearGraficaDePuntos(mejor, peor, promedio):
    plt.close()
    # print("ESTOS SON LOS DATOS DE LA GRAFICA")
    # print("TAMAÑO", len(mejor))
    # print("TAMAÑO", len(peor))
    # print("TAMAÑO", len(promedio))
    plt.plot(
        mejor,
        label="Mejor caso",
        # marker="o",
        # markersize="5",
        # markeredgewidth="2",
        # markerfacecolor="black",
    )
    plt.plot(
        promedio,
        label="Caso promedio",
        # marker="o",
        # markersize="5",
        # markeredgewidth="2",
        # markerfacecolor="black",
    )
    plt.plot(
        peor,
        label="Peor Caso",
        # marker="o",
        # markersize="5",
        # markeredgewidth="2",
        # markerfacecolor="black",
    )
    plt.legend()
    plt.xlabel("Generaciones")
    plt.ylabel("Aptitud")
    plt.title("Evolucion de generaciones")
    plt.show()
    
def crearGrafica2D(mejor, peor, promedio,title):
    listX=[]
    listY=[]
    aux = 0
    for peo in peor:
        if(aux == 0):
            plt.plot(peo[0],peo[1], marker="o", color="red",label="Peor")
            aux = aux+1
        else:
            plt.plot(peo[0],peo[1], marker="o", color="red")
            
    aux = 0    
    for prom in promedio:
        if(aux == 0):
            plt.plot(prom[0],prom[1], marker="o", color="orange",label="Promedio")
            aux = aux+1
        else:
            plt.plot(prom[0],prom[1], marker="o", color="orange")
            
    aux = 0
    for mej in mejor:
        if(aux == 0):
            plt.plot(mej[0],mej[1], marker="o", color="green",label="Mejor")
            aux = aux+1
        else:
            plt.plot(mej[0],mej[1], marker="o", color="green")   
        listX.append(mej[0])
        listY.append(mej[1]) 
        
    listAptitud = obtenerAptitud(listX.copy(),listY.copy())
    valor = 0 
    if(title == "Maximo"):
        valor = max(listAptitud)
    else:
        valor = min(listAptitud)
    plt.plot(mejor[listAptitud.index(valor)][0] ,mejor[listAptitud.index(valor)][1], marker="o", color="blue",label="Mejor Valor")  
    leyenda =f"Mejor valor x = {mejor[listAptitud.index(valor)][0]} , y = {mejor[listAptitud.index(valor)][1]}"
    plt.legend()
    plt.xlabel(leyenda)
    # plt.ylabel("Aptitud")
    plt.title(title)
    plt.show()
    return leyenda
    
