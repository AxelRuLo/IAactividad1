import tkinter as tk
import math
from turtle import back
from cruza import cruza
from grafica import crearGraficaDePuntos
import inicializacion
from mutacion import mutacion, remplazarMutados
from poda import obtencionFenotipo, podaFueraLimites, podaMax, podaMin, separarXY
from variados import obtenerAptitud, obtenerDatosGraficaMax, obtenerDatosGraficaMin

window = tk.Tk()
window.title("sintaxis")
window.geometry("820x800")
window.resizable(False, False)
window.config(bg="#ACD7F6")


generaciones = tk.IntVar()

rangoMinimoX = tk.IntVar()
rangoMinimoY = tk.IntVar()

rangoMaximoX = tk.IntVar()
rangoMaximoY = tk.IntVar()

resolucionX = tk.DoubleVar()
resolucionY = tk.DoubleVar()
poblacionMaxima =  tk.IntVar()
poblacionInicial = tk.IntVar()

pmiX = tk.DoubleVar()
pmiY = tk.DoubleVar()
pmgX = tk.DoubleVar()
pmgY = tk.DoubleVar()



# #-------------------------------------------------------
# rangoTotalX = rangoMaximoX - rangoMinimoX
# rangoTotalY = rangoMaximoY - rangoMinimoY
# puntosNecesariosX =  math.ceil((rangoTotalX / resolucionX) + 1)
# puntosNecesariosY =  math.ceil((rangoTotalY / resolucionY) + 1)
# #-------------------------------------------------------
# listaIndividuos = []
# listaMejoresAptitudesGeneracionales = []
# listaPeoresAptitudesGeneracionales = []
# listaPromedioAptitudesGeneracionales = []
# #-------------------------------------------------------
# # NECESITAN UNA FUNCION PARA SACAR TODO
# bitsIndividuoX = inicializacion.SacarBits(puntosNecesariosX)
# bitsIndividuoY = inicializacion.SacarBits(puntosNecesariosY)
# bitsTotal = bitsIndividuoX + bitsIndividuoY
#-------------------------------------------------------



# entrysvalue
exprecionR = tk.StringVar()
cadena = tk.StringVar()
resultado = tk.StringVar()

# functions
def resultadosMaximo():
    pmiProm = (pmiX.get() + pmiY.get()) /2
    pmgProm = (pmgX.get() + pmgY.get()) /2
    rangoTotalX = rangoMaximoX.get() - rangoMinimoX.get()
    rangoTotalY = rangoMaximoY.get() - rangoMinimoY.get()
    puntosNecesariosX =  math.ceil((rangoTotalX / resolucionX.get()) + 1)
    puntosNecesariosY =  math.ceil((rangoTotalY / resolucionY.get()) + 1)
    listaIndividuos = []
    listaMejoresAptitudesGeneracionales = []
    listaPeoresAptitudesGeneracionales = []
    listaPromedioAptitudesGeneracionales = []
    bitsIndividuoX = inicializacion.SacarBits(puntosNecesariosX)
    bitsIndividuoY = inicializacion.SacarBits(puntosNecesariosY)
    bitsTotal = bitsIndividuoX + bitsIndividuoY

    listaMejoresGeneracion = []
    seleccion= 0
    listaIndividuos = inicializacion.generacionIndividuosIniciales(bitsIndividuoX,bitsIndividuoY,poblacionInicial.get(),puntosNecesariosX,puntosNecesariosY)
    print("\n")
    for i in range(generaciones.get()):
        print("\n")
        print(f"GENERACION {i}")
        print(f"individuos de esta generacion   {len(listaIndividuos)}")
        print("\n")

        listaHijos=cruza(listaIndividuos.copy(),bitsTotal)


        indexMutados, hijosMutados = mutacion(listaHijos.copy(),pmiProm,pmgProm)
        listaHijos = remplazarMutados(listaHijos.copy(),indexMutados.copy(),hijosMutados)
        listaIndividuos.extend(listaHijos)
        listaIndividuos=podaFueraLimites(listaIndividuos.copy(),rangoMaximoX.get(),rangoMinimoX.get(),rangoMaximoY.get(),rangoMinimoY.get(),bitsIndividuoX,bitsIndividuoY,resolucionX.get(),resolucionY.get())

        listaIndividuosX,listaIndividuosY = separarXY(listaIndividuos.copy(),bitsIndividuoX)
        listaFenotiposX = obtencionFenotipo(listaIndividuosX,rangoMinimoX.get(),resolucionX.get(),bitsIndividuoX)
        listaFenotiposY = obtencionFenotipo(listaIndividuosY,rangoMinimoY.get(),resolucionY.get(),bitsIndividuoY)
        listaAptitud = obtenerAptitud(listaFenotiposX,listaFenotiposY)


        

        if(seleccion==0):
            listaIndividuos = podaMax(listaIndividuos.copy(),listaAptitud.copy(),poblacionMaxima.get())
            mejor,peor,promedio = obtenerDatosGraficaMax(listaAptitud.copy())
            listaMejoresAptitudesGeneracionales.append(mejor)
            listaPeoresAptitudesGeneracionales.append(peor)
            listaPromedioAptitudesGeneracionales.append(promedio)

            listaIndividuosX,listaIndividuosY = separarXY(listaIndividuos.copy(),bitsIndividuoX)
            listaFenotiposX = obtencionFenotipo(listaIndividuosX,rangoMinimoX.get(),resolucionX.get(),bitsIndividuoX)
            listaFenotiposY = obtencionFenotipo(listaIndividuosY,rangoMinimoY.get(),resolucionY.get(),bitsIndividuoY)
            listaAptitud = obtenerAptitud(listaFenotiposX,listaFenotiposY)

            mejorGeneracion = max(listaAptitud)
            indexMejorGeneracin = listaAptitud.index(mejorGeneracion)
            listaMejoresGeneracion.append([listaFenotiposX[indexMejorGeneracin],listaFenotiposY[indexMejorGeneracin]])
        
        else:
            listaIndividuos = podaMin(listaIndividuos.copy(),listaAptitud.copy(),poblacionMaxima.get())
            mejor,peor,promedio = obtenerDatosGraficaMin(listaAptitud.copy())
            listaMejoresAptitudesGeneracionales.append(mejor)
            listaPeoresAptitudesGeneracionales.append(peor)
            listaPromedioAptitudesGeneracionales.append(promedio)

            listaIndividuosX,listaIndividuosY = separarXY(listaIndividuos.copy(),bitsIndividuoX)
            listaFenotiposX = obtencionFenotipo(listaIndividuosX,rangoMinimoX.get(),resolucionX.get(),bitsIndividuoX)
            listaFenotiposY = obtencionFenotipo(listaIndividuosY,rangoMinimoY.get(),resolucionY.get(),bitsIndividuoY)
            listaAptitud = obtenerAptitud(listaFenotiposX,listaFenotiposY)

            mejorGeneracion = min(listaAptitud)
            indexMejorGeneracin = listaAptitud.index(mejorGeneracion)
            listaMejoresGeneracion.append([listaFenotiposX[indexMejorGeneracin],listaFenotiposY[indexMejorGeneracin]])
        print("FENOTIPOS E INDIVIDUOS")
        for i in range(len(listaFenotiposX)):
            print(f"individuo {listaIndividuos[i]} con fenotipo x = {listaFenotiposX[i]} con fenotipo y {listaFenotiposY[i]} {listaAptitud[i]}")
        
    print(f"Mejor aptitud por generaciones {listaMejoresGeneracion}")
    crearGraficaDePuntos(listaMejoresAptitudesGeneracionales,listaPeoresAptitudesGeneracionales,listaPromedioAptitudesGeneracionales)

def resultadoMinimo():
    pmiProm = (pmiX.get() + pmiY.get()) /2
    pmgProm = (pmgX.get() + pmgY.get()) /2
    rangoTotalX = rangoMaximoX.get() - rangoMinimoX.get()
    rangoTotalY = rangoMaximoY.get() - rangoMinimoY.get()
    puntosNecesariosX =  math.ceil((rangoTotalX / resolucionX.get()) + 1)
    puntosNecesariosY =  math.ceil((rangoTotalY / resolucionY.get()) + 1)
    listaIndividuos = []
    listaMejoresAptitudesGeneracionales = []
    listaPeoresAptitudesGeneracionales = []
    listaPromedioAptitudesGeneracionales = []
    bitsIndividuoX = inicializacion.SacarBits(puntosNecesariosX)
    bitsIndividuoY = inicializacion.SacarBits(puntosNecesariosY)
    bitsTotal = bitsIndividuoX + bitsIndividuoY

    listaMejoresGeneracion = []
    seleccion= 1
    listaIndividuos = inicializacion.generacionIndividuosIniciales(bitsIndividuoX,bitsIndividuoY,poblacionInicial.get(),puntosNecesariosX,puntosNecesariosY)
    print("\n")
    for i in range(generaciones.get()):
        print("\n")
        print(f"GENERACION {i}")
        print(f"individuos de esta generacion   {len(listaIndividuos)}")
        print("\n")

        listaHijos=cruza(listaIndividuos.copy(),bitsTotal)


        indexMutados, hijosMutados = mutacion(listaHijos.copy(),pmiProm,pmgProm)
        listaHijos = remplazarMutados(listaHijos.copy(),indexMutados.copy(),hijosMutados)
        listaIndividuos.extend(listaHijos)
        listaIndividuos=podaFueraLimites(listaIndividuos.copy(),rangoMaximoX.get(),rangoMinimoX.get(),rangoMaximoY.get(),rangoMinimoY.get(),bitsIndividuoX,bitsIndividuoY,resolucionX.get(),resolucionY.get())

        listaIndividuosX,listaIndividuosY = separarXY(listaIndividuos.copy(),bitsIndividuoX)
        listaFenotiposX = obtencionFenotipo(listaIndividuosX,rangoMinimoX.get(),resolucionX.get(),bitsIndividuoX)
        listaFenotiposY = obtencionFenotipo(listaIndividuosY,rangoMinimoY.get(),resolucionY.get(),bitsIndividuoY)
        listaAptitud = obtenerAptitud(listaFenotiposX,listaFenotiposY)


        

        if(seleccion==0):
            listaIndividuos = podaMax(listaIndividuos.copy(),listaAptitud.copy(),poblacionMaxima.get())
            mejor,peor,promedio = obtenerDatosGraficaMax(listaAptitud.copy())
            listaMejoresAptitudesGeneracionales.append(mejor)
            listaPeoresAptitudesGeneracionales.append(peor)
            listaPromedioAptitudesGeneracionales.append(promedio)

            listaIndividuosX,listaIndividuosY = separarXY(listaIndividuos.copy(),bitsIndividuoX)
            listaFenotiposX = obtencionFenotipo(listaIndividuosX,rangoMinimoX.get(),resolucionX.get(),bitsIndividuoX)
            listaFenotiposY = obtencionFenotipo(listaIndividuosY,rangoMinimoY.get(),resolucionY.get(),bitsIndividuoY)
            listaAptitud = obtenerAptitud(listaFenotiposX,listaFenotiposY)

            mejorGeneracion = max(listaAptitud)
            indexMejorGeneracin = listaAptitud.index(mejorGeneracion)
            listaMejoresGeneracion.append([listaFenotiposX[indexMejorGeneracin],listaFenotiposY[indexMejorGeneracin]])
        
        else:
            listaIndividuos = podaMin(listaIndividuos.copy(),listaAptitud.copy(),poblacionMaxima.get())
            mejor,peor,promedio = obtenerDatosGraficaMin(listaAptitud.copy())
            listaMejoresAptitudesGeneracionales.append(mejor)
            listaPeoresAptitudesGeneracionales.append(peor)
            listaPromedioAptitudesGeneracionales.append(promedio)

            listaIndividuosX,listaIndividuosY = separarXY(listaIndividuos.copy(),bitsIndividuoX)
            listaFenotiposX = obtencionFenotipo(listaIndividuosX,rangoMinimoX.get(),resolucionX.get(),bitsIndividuoX)
            listaFenotiposY = obtencionFenotipo(listaIndividuosY,rangoMinimoY.get(),resolucionY.get(),bitsIndividuoY)
            listaAptitud = obtenerAptitud(listaFenotiposX,listaFenotiposY)

            mejorGeneracion = min(listaAptitud)
            indexMejorGeneracin = listaAptitud.index(mejorGeneracion)
            listaMejoresGeneracion.append([listaFenotiposX[indexMejorGeneracin],listaFenotiposY[indexMejorGeneracin]])
        print("FENOTIPOS E INDIVIDUOS")
        for i in range(len(listaFenotiposX)):
            print(f"individuo {listaIndividuos[i]} con fenotipo x = {listaFenotiposX[i]} con fenotipo y {listaFenotiposY[i]} {listaAptitud[i]}")
        
    print(f"Mejor aptitud por generaciones {listaMejoresGeneracion}")
    crearGraficaDePuntos(listaMejoresAptitudesGeneracionales,listaPeoresAptitudesGeneracionales,listaPromedioAptitudesGeneracionales)
        

# labels
tk.Label(window,text="Introduce todos los campos necesesarios",font=('Calibri', 15),background="#ACD7F6").place(x=250,y=50)

tk.Label(window,text="generaciones",font=('Calibri', 14),background="#ACD7F6").place(x=40,y=150)
tk.Label(window,text="poblacion maxima",font=('Calibri', 14),background="#ACD7F6").place(x=240,y=150)
tk.Label(window,text="poblacion inicial",font=('Calibri', 14),background="#ACD7F6").place(x=440,y=150)

# Resoluci9ones
tk.Label(window,text="rango Minimo X",font=('Calibri', 14),background="#ACD7F6").place(x=40,y=250)
tk.Label(window,text="rango Minimo Y",font=('Calibri', 14),background="#ACD7F6").place(x=240,y=250)
tk.Label(window,text="rango Maximo X",font=('Calibri', 14),background="#ACD7F6").place(x=440,y=250)
tk.Label(window,text="rango Maximo Y",font=('Calibri', 14),background="#ACD7F6").place(x=640,y=250)


tk.Label(window,text="resolucion Y",font=('Calibri', 14),background="#ACD7F6").place(x=40,y=350)
tk.Label(window,text="resolucion X",font=('Calibri', 14),background="#ACD7F6").place(x=240,y=350)


tk.Label(window,text="pmi Y",font=('Calibri', 14),background="#ACD7F6").place(x=40,y=450)
tk.Label(window,text="pmi X",font=('Calibri', 14),background="#ACD7F6").place(x=240,y=450)
tk.Label(window,text="pmg Y",font=('Calibri', 14),background="#ACD7F6").place(x=440,y=450)
tk.Label(window,text="pmg X",font=('Calibri', 14),background="#ACD7F6").place(x=640,y=450)



# entrys
tk.Entry(window,textvariable=generaciones,font=('Calibri', 14),width=15).place(x=40,y=200)
tk.Entry(window,textvariable=poblacionMaxima,font=('Calibri', 14),width=15).place(x=240,y=200)
tk.Entry(window,textvariable=poblacionInicial,font=('Calibri', 14),width=15).place(x=440,y=200)

tk.Entry(window,textvariable=rangoMinimoX,font=('Calibri', 14),width=15).place(x=40,y=300)
tk.Entry(window,textvariable=rangoMinimoY,font=('Calibri', 14),width=15).place(x=240,y=300)
tk.Entry(window,textvariable=rangoMaximoX,font=('Calibri', 14),width=15).place(x=440,y=300)
tk.Entry(window,textvariable=rangoMaximoY,font=('Calibri', 14),width=15).place(x=640,y=300)


tk.Entry(window,textvariable=resolucionY,font=('Calibri', 14),width=15).place(x=40,y=400)
tk.Entry(window,textvariable=resolucionX,font=('Calibri', 14),width=15).place(x=240,y=400)


tk.Entry(window,textvariable=pmiY,font=('Calibri', 14),width=15).place(x=40,y=500)
tk.Entry(window,textvariable=pmiX,font=('Calibri', 14),width=15).place(x=240,y=500)
tk.Entry(window,textvariable=pmgY,font=('Calibri', 14),width=15).place(x=440,y=500)
tk.Entry(window,textvariable=pmgX,font=('Calibri', 14),width=15).place(x=640,y=500)

# buton
tk.Button(window,font=('Calibri', 14),text="minimo",command=resultadoMinimo,).place(x=450,y=700)
tk.Button(window,font=('Calibri', 14),text="maximo",command=resultadosMaximo,).place(x=250,y=700)

window.mainloop()