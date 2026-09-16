estacao = int(input("Digite o mês que estamos (1 a 12): "))

while True:
    match estacao:
        case 12 | 1 | 2:
            print("Nossa estação é verão")
            break
        case 3 | 4 | 5:
            print("Nossa estação é outono")
            break
        case 6 | 7 | 8:
            print("Nossa estação é inverno")
            break
        case 9 | 10 | 11:
            print("Nossa estação é primavera")
            break
        case _:
            estacao = int(input("Inválido. Tente novamnete: "))