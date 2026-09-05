livro = 25
caneta = 5

qnt_livros = int(input("Quantos livros voce comprou? "))
qnt_canetas = int(input("Quantas canetas voce comprou? "))

total_compra = qnt_livros * livro + qnt_canetas * caneta

print(f"O total da sua compra com {qnt_livros} livros e {qnt_canetas} canetas é de R${total_compra}")