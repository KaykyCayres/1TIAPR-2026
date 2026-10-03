busca = input('Digite uma palavra para buscar em um arquivo: ')
existe = False

with open('meuarquivo.txt','r') as file:
    conteudo = file.readlines()
    for i, conteudo in enumerate(conteudo,1):
        if busca in conteudo:
            print(f'A palavra {busca} se encontra na linha num {i}')
            existe = True
    if not existe:
        print('A palavra nao foi encontrada')