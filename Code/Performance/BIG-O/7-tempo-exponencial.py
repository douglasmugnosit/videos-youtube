
# O(2^n): Tempo Exponencial

def subsequencias(conjunto):
    resultado = []
    n = len(conjunto)
    for i in range(1 << n):
        subseq = [conjunto[j] for j in range(n) if (i & (1 << j))]
        resultado.append(subseq)
    return resultado

# Exemplo de uso:
conjunto = [1, 2, 3]
resultado = subsequencias(conjunto)
for seq in resultado:
    print(seq)
