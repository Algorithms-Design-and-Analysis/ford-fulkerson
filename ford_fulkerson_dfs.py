def dfs(matriz_adyacencia):
    camino = []
    visitados = [False] * len(matriz_adyacencia)
    stack = [0]
    while len(stack) > 0:
        entro = False
        v = stack.pop()
        if not visitados[v]:
            if v not in camino:
                camino.append(v)
            if v == len(matriz_adyacencia)-1:
                break
            visitados[v] = True
            for w in range(len(matriz_adyacencia[v])):
                if matriz_adyacencia[v][w] != None and matriz_adyacencia[v][w][1]-matriz_adyacencia[v][w][0] > 0 and not visitados[w]:
                    stack.append(w)
                    entro = True
                    break
            if not entro:
                camino.pop(-1)
                if len(camino)>0:
                    stack.append(camino[-1])
                    visitados[camino[-1]] = False

                camino_limpio = []
                for nodo in camino:
                    if nodo not in camino_limpio:
                        camino_limpio.append(nodo)
                camino = camino_limpio
            


    if len(matriz_adyacencia)-1 not in camino:
        camino = []
            
    camino_limpio = []
    for nodo in camino:
        if nodo not in camino_limpio:
            camino_limpio.append(nodo)
            
    return camino_limpio

def ford_fulkerson(matriz_ayacencia):

    flujo_maximo = 0
    camino = dfs(matriz_ayacencia)
    
    while len(camino) > 0:
        #print(camino)
        nodo_inicial_indice = 0
        nodo_final_indice = 1
        capacidades = []
        while nodo_final_indice < len(camino):
            capacidades.append(matriz_ayacencia[camino[nodo_inicial_indice]][camino[nodo_final_indice]][1]-matriz_ayacencia[camino[nodo_inicial_indice]][camino[nodo_final_indice]][0])
            nodo_inicial_indice += 1
            nodo_final_indice += 1
        bottleneck = min(capacidades)
        flujo_maximo += bottleneck
        nodo_inicial_indice = 0
        nodo_final_indice = 1
        while nodo_final_indice < len(camino):
            matriz_ayacencia[camino[nodo_inicial_indice]][camino[nodo_final_indice]][0] += bottleneck
            matriz_ayacencia[camino[nodo_final_indice]][camino[nodo_inicial_indice]][0] -= bottleneck
            nodo_inicial_indice += 1
            nodo_final_indice += 1
        camino = dfs(matriz_ayacencia) 

    return flujo_maximo


def main():
    cantidad_casos = int(input())
    for _ in range(cantidad_casos):
        nodos_cantidad = int(input())
        matriz_adyacencia = [ [None for _ in range(nodos_cantidad)] for _ in range(nodos_cantidad) ]
        arcos_cantidad = int(input())
        for _ in range(arcos_cantidad):
            arco = input().split(" ")
            nodo_inicial, nodo_final, capacidad = int(arco[0]), int(arco[1]), int(arco[2])
            matriz_adyacencia[nodo_inicial][nodo_final] = [0, capacidad]
            matriz_adyacencia[nodo_final][nodo_inicial] = [0, 0]
        #print(matriz_adyacencia)
        print(ford_fulkerson(matriz_adyacencia))

if __name__=='__main__':
    main()