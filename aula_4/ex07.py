import random

numero_secreto = random.randint(1,10)

contador = 1

while contador <= 3:
    tentativa = int(input("Digite um numero entre 1 e 10: "))
    if 1 <= tentativa <= 10:
        if tentativa == numero_secreto:
            print("Parabens voce acertou!")
            break
        else:
            print("ERRADO. Digite outro numero entre 1 e 10: ")
            contador += 1
    else:
        contador += 1
        print("Invalido")