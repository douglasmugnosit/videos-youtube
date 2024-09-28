
# O(n^2): Tempo Quadrático

def quadratico_funcao(matriz):
    for linha in matriz:
        for elemento in linha:
            print(elemento)

# Exemplo de uso:
quadratico_funcao([[1, 2], [3, 4]])  # Saída: 1 2 3 4
