numero = int(input("Digite um numero pra tabuada: "))
contador = 1

while contador <= 10:
    resultado = numero * contador
    print(f"O resultado de {numero} X {contador} = {resultado}")
    contador += 1