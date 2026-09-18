#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#NOME: Kayky Cayres Vicente da Silva    RM:575091

# ====================================== EX01 ======================================
# Crie um programa em Python que verifique se uma pessoa pode entrar em um evento 
# se for maior de 18 anos.

while True:
    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Digite apenas numero")
        continue

    if idade < 0:
        print("Invalido. Digite novamente")
        continue
    if idade >= 18:
        print("Você é maior de idade. Acesso ao evento liberado.")
    else:
        print("Você é menor de idade. Acesso ao evento negado.")
    break

# ==================================== FIM EX01 ====================================

# ====================================== EX02 ======================================
# Crie um programa em Python que compare dois números, peça ao usuario os numeros e
# compare se eles são iguais.

while True:
    try:
        num1 = int(input("Digite um numero: "))
        num2 = int(input("Digite mais um numero: "))
    except ValueError:
        print("Erro. Digite apenas numeros")
        continue
    if num1 == num2:
        print("Os numeros sao iguais!")
    else:
        print("Os numeros sao diferentes!")
    break

# ==================================== FIM EX02 ====================================

# ====================================== EX03 ======================================
# Crie um programa em Python que registre 3 notas de um aluno e determine 
# sua situação na disciplina, peça ao usuario as 3 notas e salve em uma lista, tire 
# a media e se for 7 ou maior ele passou na materia.



# ==================================== FIM EX03 ====================================

# ====================================== EX04 ======================================
# Crie um programa em Python que registre 5 produtos comprados em um mercado. 
# Use Listas, laço for e inputs.

# ==================================== FIM EX04 ====================================

# ====================================== EX05 ======================================
# Crie um programa em Python que registre 5 números digitados pelo usuário e 
# depois mostre algumas informações sobre eles, use laço For.
# 1 - A lista completa de números
# 2 - O maior número
# 3 - O menor número
# 4 - A soma de todos os números

# ==================================== FIM EX05 ====================================

# ====================================== EX06 ======================================
# Crie um programa em Python que peça números ao usuário e some todos eles.
# Use o laço while e receba numeros ate que uma condição seja atendida.

# ==================================== FIM EX06 ====================================

# ====================================== EX07 ======================================
# Crie um programa em Python que simule um sistema simples de login.
# Usar um primeiro laço while para pedir o nome de usuário até que 
# o usuário digite o valor correto, faça o mesmo para a senha.

# ==================================== FIM EX07 ====================================

# ====================================== EX08 ======================================
# Crie um programa em Python que registre 3 notas de alunos, garantindo que 
# cada nota seja válida, use as estruturas de laço for e while.

# ==================================== FIM EX08 ====================================

# ====================================== EX09 ======================================
# Crie um programa em Python que registre números digitados pelo usuário e 
# conte quantos são positivos. Use o laço while para registrar todas as entradas
# depois use o laço for para percorrer toda a lista e fazer a contagem.

# ==================================== FIM EX09 ====================================

# ====================================== EX10 ======================================
# Crie um programa em Python que registre as notas de 3 alunos em 4 provas usando
# uma matriz (lista de listas), calcule a media de cada aluno.
# Use seu conhecimento de laços para cumprir a tarefa.

# ==================================== FIM EX10 ====================================

