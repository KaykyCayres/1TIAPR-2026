dia = int(input("Digite um dia da semana (1 sendo segunda e 7 sendo domingo): "))

while True:
    match dia:
        case 1:
            print("Hoje é segunda-feira")
            break
        case 2:
            print("Hoje é terça-feira")
            break
        case 3:
            print("Hoje é quarta-feira")
            break
        case 4:
            print("Hoje é quinta-feira")
            break
        case 5:
            print("Hoje é sexta-feira")
            break
        case 6:
            print("Hoje é sabado")
            break
        case 7:
            print("Hoje é domingo")
            break
        case _:
            dia = int(input("Inválido. Tente novamente: "))