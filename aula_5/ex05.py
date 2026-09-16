nota = int(input("Digite a sua nota: "))

while True:
    match nota:
        case n if n >= 9:
            print("Excelente")
            break
        case n if n >= 7:
            print("Bom")
            break
        case n if n >= 5:
            print("Regular")
            break
        case n if 0 <= n < 5:
            print("Reprovado")
            break
        case _:
            nota = int(input("Invalido. Digite novamente: "))