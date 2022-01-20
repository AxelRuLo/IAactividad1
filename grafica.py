import matplotlib.pyplot as plt


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
    plt.xlabel("Generacione")
    plt.ylabel("Aptitud")
    plt.title("EvolucionGeneraciones")
    plt.show()
