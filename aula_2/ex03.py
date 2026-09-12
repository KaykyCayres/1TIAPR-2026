ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"Esse ano {ano} é bissexto")
else:
    print(f"Esse ano {ano} nao é bissexto")