menu = int(input("1- Ver perfil\n2- Editar perfil\n3- Sair\n\nSelecione uma opção: "))

while True:
    match menu:
        case 1:
            print("Você selecionou a opção 1- Ver perfil")
            break
        case 2:
            print("Você selecionou a opção 2- Editar perfil")
            break
        case 3:
            print("Você selecionou a opção 3- Sair")
            break
        case _:
            menu = int(input("Você selecionou uma opção inválida. Tente novamente: "))