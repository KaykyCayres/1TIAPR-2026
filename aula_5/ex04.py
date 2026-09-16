idade = int(input("Digite a sua idade: "))

while True:
    match idade:
        case n if 0 <= n < 13:
            print("Você é uma criança")
            break
        case n if 12 < n < 18:
            print("Você é adolescente")
            break
        case n if n >= 18:
            print("Você é adulto")
            break
        case _:
            idade = int(input("Inválido. Digite novamente: "))