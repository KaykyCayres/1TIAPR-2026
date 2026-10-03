arquivo1 = input('Digite o nome do primeiro arquivo que deseja concatenar: ')
arquivo2 = input('Digite o nome do segundo arquivo que deseja concatenar: ')

with open(arquivo1,'r') as file:
    conteudo1 = file.read()

with open(arquivo2,'r') as file:
    conteudo2 = file.read()

with open(arquivo2,'r') as file:
    concatenado = file.write(conteudo1 + conteudo2)

print(concatenado)