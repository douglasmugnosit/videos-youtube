
# O(n!) Tempo fatorial

def permutacoes(lista):
    if len(lista) == 0:
        return []
    if len(lista) == 1:
        return [lista]
    
    resultado = []
    for i in range(len(lista)):
        m = lista[i]
        restante = lista[:i] + lista[i+1:]
        for p in permutacoes(restante):
            resultado.append([m] + p)
    
    return resultado

# Exemplo de uso:
resultado = permutacoes([1, 2, 3])
for perm in resultado:
    print(perm)
