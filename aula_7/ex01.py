# def soma(num1, num2):
#     return num1 + num2

# def sub(num1, num2):
#     return num1 - num2

# def div(num1, num2):
#     return num1 / num2

# def mult(num1, num2):
#     return num1 * num2

def calculadora(num1, num2):
    conta = f"soma: {num1 + num2}\nsubtracao: {num1 - num2}\ndivisao: {num1 / num2}\nmultiplicacao: {num1 * num2}"
    return conta

resultado = calculadora(3, 2)
print(resultado)