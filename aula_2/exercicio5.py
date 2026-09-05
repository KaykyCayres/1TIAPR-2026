produto = 10
compra = int(input("Digite quantos produtos voce comprou: "))
valor_final = produto * compra

if compra >= 10:
    print(f"Como a sua compra foi de {compra}, voce ganhou um desconto de 10%")
    valor_final = valor_final * 0.9
    print(valor_final)
else:
    print(f"Esse é o valor da compra {valor_final}")