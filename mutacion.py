import random


def mutacion(listaHijos,pmi,pmg):
    hijosMutadosIndex = []
    hijosMutados = []
    for index in range(len(listaHijos)):
        pmiActual = random.random()
        if pmiActual <= pmi:
            hijosMutadosIndex.append(index)
            # print(f"el hijo {index} mutara")
            hijoMutado = []
            for bit in listaHijos[index]:
                pmgActual = random.random()
                if pmgActual <= pmg:
                    if bit == 1:
                        hijoMutado.append(0)
                    else:
                        hijoMutado.append(1)
                else:
                    hijoMutado.append(bit)
            # print("hijo sin mutaciones")
            # print(listaHijos[index])
            # print("hijo con mutaciones")
            # print(hijoMutado)
            hijosMutados.append(hijoMutado)
    # print("estos son los index de los hijos mutados",hijosMutadosIndex)
    # print("estos son los hijos mutados",hijosMutados)
    return hijosMutadosIndex, hijosMutados

def remplazarMutados(listaHijos:list,indexMutados,listaMutados):
    indexMutados.reverse()
    # print("index que van a quitarse")
    # print(indexMutados)
    for index in indexMutados:
        listaHijos.pop(index)
    # print("hijos sin mutados")
    # print(listaHijos)
    listaHijos.extend(listaMutados)
    # print("hijos con mutados")
    # print(listaHijos)
    return listaHijos

