from heapq import heapify, heappop

def solve(n, arr):
    #Cuenta el numero de elementos.
    #Asi agregalos a un heap de la forma (#veces, elem)
    #Entonces mientras que el heap tenga al menos dos elementos.
    #Saca el del tope (tv, te) , aqui estara el de mayor numero de repeticiones.
    #Saca el siguiente, (sv, se) entonces puedes eliminar a te, tantas veces
    #como sv, entonces si sv == tv quiere decir que puedes eliminarlos todos
    #y se vuelve a la pregunta original.
    #no puede ser que sv > tv, entonces en otro caso elimina a te tantas veces
    #como se pueda y repite con el siguiente elemento en el heap.
    #Si todavia no te deshiciste del tv, entonces lo que le quede es el resultado
    #Si te quedaste con un elemento en el heap, entonces el numero de veces
    #que aparezca este es la respuesta, no puede haber mas de un elemento en el
    #heap
    d = {}
    for x in arr:
        if d.get(x) == None:
            d[x] = 1
        else:
            d[x] += 1
    heap = []
    for k in list(d.keys()):
        heap.append((d[k], k))
    heapify(heap)
    print(heap)
    # while len(heap) >= 2:
    #     tv, te = heappop(heap)
    #     sv, se = heappop(heap)
    #     while tv > sv and len(heap) > 0:
    #         tv -= sv
    #         sv, se = heappop(heap)
    # if len(heap) == 1:
    #     return heappop(heap)[0]
    # return 0
        
if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(n, arr))
