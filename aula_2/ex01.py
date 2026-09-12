numero = float(input("Digite um numero: "))
if numero > 0:
    print(f"O numero {numero:.0f} é postivo")
elif numero < 0:
    print(f"O numero {numero:.0f} é negativo")
else:
    print(f"O numero {numero:.0f} é zero")