arquivo = input('Digite o nome do arquivo quue deseja contar as palavras: ')

with open(arquivo,'r') as file:
    conteudo = file.read()
    palavras = conteudo.split()
    print(f'A quantidade de palavras do arquivo {arquivo} é de: {len(palavras)}')