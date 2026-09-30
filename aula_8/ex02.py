with open('meuarquivo.txt', 'w+') as file:
    file.write('Olá, mundo!')
    file.write('\nEste é um arquivo de texto')
    file.write(f'\nCriado por {input('Digite seu nome: ')}')

with open('meuarquivo.txt', 'r') as ler:
    leitura = ler.read()
    print(leitura)