def bfs(matriz_adyacencia):
    
    camino = []    
    queue = [[0]] 
    vecinos = [[]]
    while len(queue) > 0:
     camino_actual = queue.pop(0)
     v = camino_actual[-1]
     if v == len(matriz_adyacencia)-1:
        break
     for w in range(len(matriz_adyacencia[v])):
        if matriz_adyacencia[v][w] != None and matriz_adyacencia[v][w][1]-matriz_adyacencia[v][w][0] > 0 and w not in vecinos[-1]:
                    nuevo_camino = camino_actual + [w]
                    queue.append(nuevo_camino)
                    vecinos.append(nuevo_camino)
    for i in vecinos:
        if len(matriz_adyacencia)-1 in i:
            camino = camino_actual
    return camino

def ford_fulkerson(matriz_ayacencia):

    flujo_maximo = 0
    camino = bfs(matriz_ayacencia)
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
        camino = bfs(matriz_ayacencia) 

    return flujo_maximo


def main():
    #cantidad_casos = int(input())
    #for _ in range(cantidad_casos):
        nodos_cantidad = int(input())
        matriz_adyacencia = [ [None for _ in range(nodos_cantidad)] for _ in range(nodos_cantidad) ]
        arcos_cantidad = int(input())
        for _ in range(arcos_cantidad):
            arco = input().split(" ")
            nodo_inicial, nodo_final, capacidad = int(arco[0]), int(arco[1]), int(arco[2])
            matriz_adyacencia[nodo_inicial][nodo_final] = [0, capacidad]
            matriz_adyacencia[nodo_final][nodo_inicial] = [0, 0]
        print(ford_fulkerson(matriz_adyacencia))

if __name__=='__main__':
    main()