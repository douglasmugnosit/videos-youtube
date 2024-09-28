
# O(n log n): Tempo Linear-Logarítmico

# O(log n)
def linear_logaritmico_funcao(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = linear_logaritmico_funcao(lista[:meio])
    direita = linear_logaritmico_funcao(lista[meio:])
    return merge(esquerda, direita)

# O(n)
def merge(esquerda, direita):
    if not esquerda:
        return direita
    if not direita:
        return esquerda
    if esquerda[0] < direita[0]:
        return [esquerda[0]] + merge(esquerda[1:], direita)
    return [direita[0]] + merge(esquerda, direita[1:])

# Exemplo de uso:
print(linear_logaritmico_funcao([4, 2, 5, 1, 6, 3]))  # Saída: [1, 2, 3, 4, 5, 6]
