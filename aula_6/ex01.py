matriz_1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matriz_2 = [
    [11,21,31],
    [41,51,61],
    [71,81,91]
]

for l in range(len(matriz_1)):
    for c in range(len(matriz_1[l])):
        soma = matriz_1[l][c] + matriz_2[l][c]
        print(soma, end= ' ')
    print()