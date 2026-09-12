digito = int(input("Digite um numero par: "))

while digito % 2 != 0:
    digito = int(input("Invalido. Por favor digite um numero par: "))

print(f"O numero par é {digito}")