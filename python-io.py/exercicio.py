# # Exercício 1: Faça um programa que solicite o nome de uma pessoa usuária e imprima-o na vertical. Exemplo:
# from operator import truediv


# NAME = input("Insira seu nome: ")

# for letter in NAME:
#     print(letter)

# # Exercício 2: Escreva um programa que receba vários números naturais e calcule a soma desses valores. Caso algum valor da entrada seja inválido (por exemplo uma letra), uma mensagem deve ser exibida na saída de erros no seguinte formato: “Erro ao somar valores, {valor} é um valor inválido”. Ao final, você deve imprimir a soma dos valores válidos.

# def soma_valores(list):
#     ok = False
#     sum = 0
#     valor = 0
#     while True:
#         n = str(input(list))
#         if n.isnumeric():
#             valor = int(n)
#             ok = True
#         else:
#             print('digite um número inteiro válido')
#         if ok:
#             break
#     sum += int(valor)
#     return print(f"A soma dos valores válidos é: {sum}")

# n = soma_valores('Digite um número: ')
# print(f'Você acabaou de digitar o número {n}')

def soma_valores(msg):
    ok = False
    valor = 0
    sum = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('digite um número inteiro válido')
        if ok:
            break
    sum += int(valor)
    return sum

n = soma_valores('Digite um número: ')
print(f'Você acabaou de digitar o número {n}')


# def leiaInt(msg):
#     ok = False
#     valor = 0
#     while True:
#         n = str(input(msg))
#         if n.isnumeric():
#             valor = int(n)
#             ok = True
#         else:
#             print('digite um número inteiro válido')
#         if ok:
#             break
#     return valor

# n = leiaInt('Digite um número: ')
# print(f'Você acabaou de digitar o número {n}')
