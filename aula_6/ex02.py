matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

escalar = 3

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        soma = matriz[l][c] * escalar
        print(soma, end= ' ')
    print()